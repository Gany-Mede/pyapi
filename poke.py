#!/usr/bin/python3

import requests

json2python={}

def api_pull():
    global json2python
    begin_url = 'https://pokeapi.co/api/v2/pokemon/'
    choice = input("What Pokepond would you like a picture of? ")
    end_api = begin_url + choice
    info = requests.get(end_api).json()
    json2python = info
    return info

def api_slice(json2python):
    poke_pic = json2python['sprites']['front_default']
    return poke_pic

def main():
    api_pull()
    api_slice(json2python)

if __name__ == "__main__":
    main()

