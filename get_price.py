import requests
from bs4 import BeautifulSoup
import json

class MyScraper:
    def __init__(self):
        # URL of the coin
        self.url = 'https://www.binance.com/en/price/'
    def scraper(self, dat):

        parseUrl = self.url+dat['name']
        response = requests.get(parseUrl)
        html_content = response.content
        # find the element and get the content
        soup = BeautifulSoup(html_content, 'html.parser')
        price_element = soup.find('div', {'class': 'css-zo19gu'})

        price = price_element.text.strip()
        price = price.replace("USD $", "").replace(",", "")

        payload = json.dumps({
            "name": dat['name'],
            "coin_code": dat['coin_code'],
            "price": price,
        })
        return self.sendRequest(payload)
    
    def sendRequest(seld, payload):
        url = "http://127.0.0.1:8000/api/store"
        headers = {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.content)
    
    def loadjson(self,jsonfile):
        with open(jsonfile) as f:
            data = json.load(f)
        for dat in data:
            self.scraper(dat)

myscrap = MyScraper()
btc = myscrap.loadjson("currency.json")



