from flask import Flask, request
from twilio.rest import Client
import os
import requests

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def bot():
	client = Client(os.environ['SID'], os.environ['TOKEN'])
	msg = request.values.get('Body', '').lower()
	responded = False
	
	if 'joke' in msg:
		r = requests.get('https://official-joke-api.appspot.com/random_joke')

		if r.status_code == 200:
			data = r.json()
			body = f'{data["setup"]}\n\n{data["punchline"]}'

		else:
			body = f'{r.status_code} error occurred retrieving joke.'

		responded = True

	if not responded:
		body = "Say 'joke' and I shall tell you a joke."

	message = client.messages.create(
									from_ = 'whatsapp:+14155238886',
									body = body,
									to = request.values.get('From', '')
									)

	return body
