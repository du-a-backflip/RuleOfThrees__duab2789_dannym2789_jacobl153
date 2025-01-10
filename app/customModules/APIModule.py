# Colyi Chen, Dua Baig, Jacob Lukose, Daniel M__
# RuleOfThrees
# SoftDev
# P02
# 2024-01-10

# import requests
import json, random, requests, urllib.request
from urllib.request import Request, urlopen

def getDict():
    try:
        file = open('../keys/wordAPI.txt', 'r')
        content = file.read().strip()
        word = "anything"
        file.close()
        url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={content}"
        API = urllib.request.urlopen(url)
        data = json.loads(API.read())
        print(data)
    except Exception as e:
        print(e)
        
getDict()