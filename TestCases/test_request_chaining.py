import json

import jsonpath
import requests

def test_add_new_student():
    global id
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/Chaitra/PycharmProjects/APIAutomation/AddStudent.json")
    json_request = json.loads(f.read())
    response = requests.post(API_URL,json_request)
    print(response.text)
    id = jsonpath.jsonpath(response.json(),"id")
    print(id[0])

def test_get_details():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(API_URL)
    print(response.text)