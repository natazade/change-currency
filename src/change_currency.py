import requests
from cachetools import TTLCache, cached


cache = TTLCache(maxsize=100 , ttl=3*60*60)

@cached(cache)
def api_request(base_currency):
    # time.sleep(3)
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code !=200:
        return None
    data = response.json()
    return data

def convert_currency(amount , change_rate):
    return amount * change_rate
