import json

import jsonpath
import requests

url = "https://reqres.in/api/users/2"

# Read input file
file = open('../CreateJson.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
#print(request_json)

# Make post request with json input body
response = requests.put(url, request_json)
print(response.content)
print(response.status_code)

#PArse content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li)