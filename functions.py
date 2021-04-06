import requests_ as r

def get_joke():
	URL = 'https://official-joke-api.appspot.com/random_joke'

	try:
		data = r.get_JSON(URL)

	except Exception as e:
		print(f'ERROR: get_joke(): {e}')

		return 'Something went wrong..'

	else:
		return f'{data["setup"]}\n\n{data["punchline"]}'
