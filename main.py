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
	text = request.values.get('Body', '').lower()
	
	if text == 'joke':	
		body = f.get_joke()

	elif text == '1' or text == '🔢' or text == 'latest':
		body = r.reply_1_latest

	elif text == '2' or text == '💉' or text == 'vaccine':
		body = r.reply_2_vaccine

	elif text == '21':
		body = r.reply_21

	elif text == '22':
		body = r.reply_22

	elif text == '23':
		body = r.reply_23

	elif text == '24':
		body = r.reply_24

	elif text == '25':
		body = r.reply_25

	elif text == '26':
		body = r.reply_26

	elif text == '27':
		body = r.reply_27

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
