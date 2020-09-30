#!/usr/bin/python3

import requests


def main():
    apodresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()
    
    for item in apodresp['photos']:
        print(item['rover']['name'])
        print(item['earth_date'])
        print(item['img_src'])

if __name__ == "__main__":
    main()  
