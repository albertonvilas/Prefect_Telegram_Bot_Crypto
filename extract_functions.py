import requests
import datetime
import config_public


def api_call():
    result = []
    for pair in config_public.pairs:
        req = requests.get('https://api.coinbase.com/v2/prices/'+ pair +'/spot').json()
        result.append(req['data'])
    return result



def extract_method():

    resp = api_call()
    return resp

extract_method()