import pytest
import json,jsonpath
import requests


def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/Chaitra/PycharmProjects/APIAutomation/Requestjson.json",'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10057040"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 10057040

def test_update_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10057040"
    f = open("C:/Users/Chaitra/PycharmProjects/APIAutomation/Requestjson.json",'r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

def test_delete_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10057040"
    response = requests.delete(API_URL)
    print(response.text)