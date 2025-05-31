from change_currency import api_request

currencies = list(api_request('USD')['rates'].keys())