import os
import helper_requests as r
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

def get_joke():
	try:
		data = r.get_JSON('https://official-joke-api.appspot.com/random_joke')

	except Exception as e:
		print(f'ERROR: joke: {e}')

		return 'Something went wrong..'

	else:
		return f'{data["setup"]}\n\n{data["punchline"]}'

@app.route('/', methods = ['POST'])
def bot():
	client = Client(os.environ['SID'], os.environ['TOKEN'])
	text = request.values.get('Body', '').lower()
	
	if text == 'joke':
		body = get_joke()

	client.messages.create(
			from_ = request.values.get('To', ''),
			body = body,
			to = request.values.get('From', '')
	)

	return 'WhatsApp Bot is live!'
