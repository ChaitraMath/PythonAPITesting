import pytest
import json, jsonpath
import requests

def test_Add_new_data():
    App_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/Chaitra/PycharmProjects/APIAutomation/Requestjson.json",'r')
    request_json = json.loads(f.read())
    response = requests.post(App_url, request_json)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    f = open("C:/Users/Chaitra/PycharmProjects/APIAutomation/TechDetails.json", 'r')
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    addr_api_url = "https://thetestingworldapi.com/api/addresses"
    f = open("C:/Users/Chaitra/PycharmProjects/APIAutomation/address.json", 'r')
    request_json = json.loads(f.read())
    request_json['stId'] = id[0]
    response = requests.post(addr_api_url, request_json)
    print(response.text)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(final_details)
    print(response.text)