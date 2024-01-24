import requests
import json,jsonpath
import pytest
#API url

def test_fetch_user_details():
    url = "https://reqres.in/api/users?page=2"
    #Send get request
    response = requests.get(url)
    #Print content
    print(response.content)
    #Fetch response to json format
    json_response = json.loads(response.text)
    print(json_response)
    #fetch value using jsonpath
    pages = jsonpath.jsonpath(json_response,'total_pages')
    print(pages[0])
    #Fetch all first names
    for i in range(0,4):
        first_name1 = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
        print(first_name1[0])