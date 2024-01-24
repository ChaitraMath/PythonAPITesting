import requests
import json,jsonpath
#API url
url = "https://reqres.in/api/users?page=2"

#Send get request
response = requests.get(url)

print(response)
#Print content
print(response.content)

#print status code
print(response.status_code)

#validate status code
assert response.status_code == 200

#Print response header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

#Fetch cookies
print(response.cookies)
#Fetch encoding
print(response.encoding)
#Fetch timelapse
print(response.elapsed)

#Fetch response to json format
json_response = json.loads(response.text)
print(json_response)

#fetch value using jsonpath
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])

#Fetch name
first_name = jsonpath.jsonpath(json_response,'data[0].first_name')
print(first_name[0])

#Fetch all first names
for i in range(0,4):
    first_name1 = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(first_name1[0])