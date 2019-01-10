from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()

    resp.say("Here's your K-Pop song of the day!", voice='alice')
    resp.play("https://vanilla-snowshoe-2871.twil.io/assets/red_flavor_short.mp3")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
