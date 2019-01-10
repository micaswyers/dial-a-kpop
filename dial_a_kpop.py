import os

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse


SOTD_URL = os.environ.get('SOTD_URL')
SOTD_YT_URL = os.environ.get('SOTD_YT_URL')

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()

    resp.say("Hi, here is your K-pop song of the day!")
    resp.say("안녕하세요! 오늘의 케이팦 노래입니다.", voice='Polly.Seoyeon')
    resp.play(SOTD_URL)
    resp.say("Thanks for listening!")
    resp.say("들어주셔서 감사합니다.", voice='Polly.Seoyeon')

    return str(resp)

@app.route("/sms", methods=['GET', 'POST'])
def reply_text():
    resp = MessagingResponse()

    resp.message(f"Hi! Here is your K-pop song of the day: {SOTD_YT_URL}")
    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host='0.0.0.0')
