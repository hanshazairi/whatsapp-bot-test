from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def bot():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()
	responded = False

	if 'joke' in incoming_msg:
		r = requests.get('https://official-joke-api.appspot.com/random_joke')

		if r.status_code == 200:
			data = r.json()
			joke = f'{data["setup"]}\n\n{data["punchline"]}'

		else:
			joke = f'{r.status_code} error occurred retrieving joke.'

		msg.body(joke)
		responded = True

	if not responded:
		msg.body('I do not recognise that command.')

	return str(resp)

#if __name__ == '__main__':
#	app.run()
