import json

import requests

url = "https://reqres.in/api/users"

# Read input file
file = open('../CreateJson.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
#print(request_json)

# Make post request with json input body
response = requests.post(url, request_json)
print(response.content)
print(response.status_code)

#Fetch header from response
print(response.headers)
print(response.headers.get('Content-Length'))
