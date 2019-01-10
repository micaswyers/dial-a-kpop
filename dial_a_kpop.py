import os

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

SOTD_URL = os.environ.get('SOTD_URL')

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()

    resp.say("Here's your K-Pop song of the day!", voice='alice')
    resp.play(SOTD_URL)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host='0.0.0.0')
