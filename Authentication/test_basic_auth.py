import requests
from requests.auth import HTTPBasicAuth

def test_with_auth():
    url = "https://api.github.com/user"
    username = 'ChaitraMath'
    password = 'C@m1102#'
    api_token = "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"
    response = requests.get(url, auth=HTTPBasicAuth(username, api_token))
    print(response.text)