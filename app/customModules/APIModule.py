# Colyi Chen, Dua Baig, Jacob Lukose, Daniel M__
# RuleOfThrees
# SoftDev
# P02
# 2024-01-10

import json, random, urllib.request, requests
from urllib import request, parse

def getDict():
    try:
        file = open('keys/wordAPI.txt', 'r')
        content = file.read().strip()
        word = "flood"
        file.close()
        dictionary = []
        with open('customModules/words.txt', 'r') as file:
            print(1)
            for line in file:
                word = line.strip()
                url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={content}"
                API = urllib.request.urlopen(url)
                data = json.loads(API.read())[0]
                definition = data['shortdef'][0]
                syn_list = str(data['meta']['syns'][0]).replace("[", "").replace(']', "").replace('\'', "")
                dictionary.append(word + "+" + definition + "+" + syn_list)
        return(dictionary)
    except Exception as e:
        print(e)

def getQuote():
    try:
        file = open('keys/quotesAPI.txt', 'r')
        content = file.read().strip()
        file.close()
        url = f'https://api.api-ninjas.com/v1/quotes/'
        response = requests.get(url, headers={'X-Api-Key': content})
        i = 12
        while response.text[i]!= "\"":
            i += 1
        return(response.text[12:i])
    except Exception as e:
        print(e)

def getGif():
    try:
        file = open('keys/giphyAPI.txt', 'r')
        content = file.read().strip()
        file.close()
        url = f'http://api.giphy.com/v1/gifs/search'

        params = parse.urlencode({
        "q": "win",
        "api_key": content,
        "limit": "1"
        })

        with request.urlopen("".join((url, "?", params))) as response:
            data = json.loads(response.read())

        all_info=json.dumps(data, sort_keys=True, indent=2)
        i = 0
        while all_info[i:i+8]!= "original":
            i += 1
        j =i
        while all_info[j: j+5] != ".gif\"":
            if all_info[j: j +3] == "url":
                k = j+6
            j += 1
        return(all_info[k: j+5])

    except Exception as e:
        print(e)

getGif()