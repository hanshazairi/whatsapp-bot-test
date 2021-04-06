import requests

def get_JSON(URL):
	request = requests.get(URL)

	if request.status_code == 200:
		return request.json()

	else:
		raise Exception(f'{r.status_code} ERROR: get_JSON({URL})')
