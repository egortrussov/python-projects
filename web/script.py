import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://steamcommunity.com/market/listings/730/XM1014%20%7C%20Seasons%20%28Minimal%20Wear%29'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

stspan = soup.findAll('span', { 'class': 'market_commodity_orders_header_promote' })
stspan1 = soup.findAll('div', { 'id': 'market_commodity_buyreqeusts_table' })
mydivs = soup.findAll("span", {"class": "market_listing_price market_listing_price_with_publisher_fee_only"})

#stpr = str(stspan[0])
print(mydivs)
s = str(mydivs[0])
ss = str(mydivs[1])
print(s, ss, 'jj')
pr = s[s.find('>') + 1 : s.rfind('<') - 1]
pr1 = ss[ss.find('>') + 1 : ss.rfind('<') - 1]

pp = 0
pp1 = 0
for i in pr:
    if i == ',':
        break
    if i >= '0' and i <= '9':
        pp = pp * 10 + int(i)
for i in pr1:
    if i == ',':
        break
    if i >= '0' and i <= '9':
        pp1 = pp1 * 10 + int(i)

print(pp, pp1)

q = (max(pp, pp1) * 0.87 - min(pp, pp1)) / min(pp, pp1) * 100
print(q)

