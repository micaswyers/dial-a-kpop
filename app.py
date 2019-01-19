import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse


SOTD_URL = os.environ.get('SOTD_URL')
SOTD_YT_URL = os.environ.get('SOTD_YT_URL')
SUBWAY_JINGLE_URL = os.environ.get('SUBWAY_JINGLE_URL')
SUBWAY_JINGLE_YT_URL = os.environ.get('SUBWAY_JINGLE_YT_URL')


app = Flask(__name__)
# Move this to app config file
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#from models import Song

@app.route("/")
def hello():
    return "Hello World"

@app.route("/voice", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()

    resp.say("Hi, here is your K-pop song of the day!")
    resp.say("안녕하세요! 오늘의 케이팦 노래입니다.", voice='Polly.Seoyeon')
    resp.play(SOTD_URL)
    resp.say("Thanks for listening!")
    resp.say("들어주셔서 감사합니다.", voice='Polly.Seoyeon')

    return str(resp)

@app.route("/sms", methods=['GET', 'POST'])
def answer_text():
    resp = MessagingResponse()

    resp.message("안녕하세요! 오늘의 케이팦 노래입니다!")
    resp.message(f"Hi! Here is your K-pop song of the day: {SOTD_YT_URL}")
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
