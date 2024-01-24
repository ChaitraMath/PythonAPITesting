import json

import requests

url = "https://reqres.in/api/users"

def test_create_user():

    # Read input file
    file = open('C:\\Users\\Chaitra\\PycharmProjects\\APIAutomation\\CreateJson.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    #print(request_json)
    # Make post request with json input body
    response = requests.post(url, request_json)
    print(response.content)

    print(response.status_code)
    assert response.status_code == 201
    #Fetch header from response
    print(response.headers)
    print(response.headers.get('Content-Length'))
