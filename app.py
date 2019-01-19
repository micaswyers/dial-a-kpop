from datetime import datetime
import os
import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

SOTD_URL = os.environ['SOTD_URL']
SOTD_YT_URL = os.environ['SOTD_YT_URL']

@app.route("/")
def hello():
    return "Hello World"

@app.route("/voice", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()

    resp.say("Hi, here is your K-pop song of the day!")
    resp.say("안녕하세요! 오늘의 케이팦 노래입니다.", voice='Polly.Seoyeon')
    sotd = _get_song()
    if sotd:
        resp.say(f"{sotd.title} by {sotd.artist}")
        resp.say(f"{sotd.korean_artist}의 {sotd.title}", voice='Polly.Seoyeon')
        resp.play(sotd.asset_url)
    else:
        resp.play(SOTD_URL)
    resp.say("Thanks for listening!")
    resp.say("들어주셔서 감사합니다.", voice='Polly.Seoyeon')

    return str(resp)

def _get_song():
    today = datetime.now().timetuple().tm_yday
    # TODO: Replace magic # with count of songs in db
    query_id = (today % 19) + 1
    todays_song = Song.query.filter_by(id=query_id).first()
    return todays_song

@app.route("/sms", methods=['GET', 'POST'])
def answer_text():
    resp = MessagingResponse()

    sotd = _get_song()
    if sotd:
        resp.message(f"Hi! Here is your K-pop song of the day: '{sotd.title}' by {sotd.artist}'")
        resp.message(f"안녕하세요! 오늘의 케이팦 노래입니다: {sotd.korean_artist}의 {sotd.title}")
        resp.message(f"{sotd.video_url}")
    else:
        resp.message(f"Hi! Here is your K-pop song of the day:")
        resp.message(f"안녕하세요! 오늘의 케이팦 노래입니다:")
        resp.message(SOTD_YT_URL)
    return str(resp)

@app.route("/subway/voice", methods=['GET', 'POST'])
def reply_subway_voice():
    resp = VoiceResponse()
    resp.say("Hello, pretend you are on the Seoul subway.")
    resp.play(SUBWAY_JINGLE_URL)
    resp.say("Good-bye.")
    return str(resp)

@app.route("/subway/sms", methods=['GET', 'POST'])
def reply_subway_sms():
    resp = MessagingResponse()

    resp.message(f"Hello, pretend you are on the Seoul Subway: {SUBWAY_JINGLE_YT_URL}")
    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host='0.0.0.0')
