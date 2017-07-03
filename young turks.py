from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://theyoungturks.co.uk/catalogue/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = [h2.text.split(' - ')[1] for h2 in soup.find_all('h2')]
title = [h3.text for h3 in soup.find_all('h3')]
url = ['https://theyoungturks.co.uk'+u['href'] for fig in soup.find_all(class_='front') for u in fig.find_all('a')]

print(len(title))
print(len(artist))
print(url)