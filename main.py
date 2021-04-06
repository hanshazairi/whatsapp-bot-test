import os
import constants as c
import functions as f
import replies as r
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)
client = Client(os.environ['SID'], os.environ['TOKEN'])

@app.route('/', methods = ['POST'])
def bot():
	text = request.values.get('Body', '')
	
	if text == 'joke':	
		body = f.get_joke()

	elif text == '1' or text.lower() == 'latest':
		body = r.reply_1_latest

	else:
		body = r.start
		media_url = c.start

	message = client.messages.create(
			from_ = request.values.get('To', ''),
			body = body,
#			media_url = media_url,
			to = request.values.get('From', '')
	)

	return message.sid
