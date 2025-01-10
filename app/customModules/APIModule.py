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
        word = "flood"
        file.close()
        with open('words.txt', 'r') as file:
            for line in file:
                word = line.strip()
                url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={content}"
                API = urllib.request.urlopen(url)
                data = json.loads(API.read())[0]
                definition = data['shortdef'][0]
                word = data['meta']['id']
                syn_list = data['meta']['syns'][0]
                print([word, definition, syn_list]) # Not FINISHED DON'T RUN
    except Exception as e:
        print(e)

getDict()
