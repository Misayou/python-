import requests
import json


def get_json_data():
    js_file = open('1.json', 'r', encoding='utf-8')
    json_obj = json.load(js_file)
    return json_obj["content"]["positionResult"]["result"]


def add_data():

    return "hello"
