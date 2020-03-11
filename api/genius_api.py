import requests

BEARER_TOKEN = 'MXMu0djQ9_K1P-BwGX0Lhi4wtAb8NtBCP6513DVMvBZL1T2nSjHzJId67ILe2TDz'


def search(term):
    url = 'http://api.genius.com/search?q={}'.format(term)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + BEARER_TOKEN
    }
    return requests.get(url=url, headers=headers)

def create_response(api_response):
    content = api_response.json()['response']['hits']
    return [music['result']['full_title'] for music in content]
