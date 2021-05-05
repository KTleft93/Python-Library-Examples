import urllib.request as urllib2
import csv
import re
from bs4 import BeautifulSoup
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
rank_page = 'https://coinmarketcap.com/'
request = urllib2.Request(rank_page, headers={'User-Agent': 'your user-agent'})
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

coinNames = soup.find_all("p", class_="sc-AxhUy fqrLrs")


# write title row

for name in coinNames:
    
    print(name.get_text())

  


