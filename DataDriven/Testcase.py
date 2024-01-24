import openpyxl
import requests
import json
import jsonpath
from DataDriven import Library

def test_add_multiple_students():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/Chaitra/PycharmProjects/APIAutomation/addNewSt.json",'r')
    json_requests = json.loads(f.read())

    obj = Library.Common("C:/Users/Chaitra/Desktop/pytest/TestData.xlsx","Sheet1")
    col =obj.fetch_column_count()
    row =obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2,row+1):
        updated_json_request = obj.update_request_with_data(i,json_requests,keyList)
        response = requests.post(api_url,updated_json_request)
        #print(response.text)
        print(response)