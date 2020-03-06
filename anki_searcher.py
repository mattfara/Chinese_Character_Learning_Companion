#These methods check whether phrases and characters are in Anki
#It assumes the following about Anki:
#  -characters and phrases are in a deck "Chinese-all"
#  -phrases are in the 'reboot' subdeck
#  -characters are in the 'hanzi' subdeck

import requests
import sys

url = 'http://localhost:8765'

def has_result(data):
    r = requests.post(url, json=data)
    _json = r.json()
    result = _json["result"]
    error = _json["error"]
    return len(result)>0

def phrase_exists(phrase):
    query_str = f"deck:Chinese-all::reboot card:1 {phrase}"
    data = {'action':'findCards', 'version':6, 'params':{'query':query_str}}
    #the request body MUST be sent as JSON explicitly
    return has_result(data)

def character_exists(chr):
    query_str = f"deck:Chinese-all::hanzi character:{chr}"
    data = {'action':'findCards', 'version':6, 'params':{'query':query_str}}
    return has_result(data)
