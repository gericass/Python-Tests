
from bs4 import BeautifulSoup
import urllib.request
import re

url = 'http://kingdeluxe.ca/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

p = soup.prettify()

artist = []
title = []
url = []

for tit in soup.find_all(class_="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-780"):
    for ul in tit.find_all('li'):
        for a in ul.find_all('a'):
            sp = a.text.split(' – ')
            if len(sp)<2:
                title.append(sp[0])
                artist.append("")
            else:
                title.append(sp[1])
                artist.append(sp[0])
            url.append(a['href'])


print(len(title))
print(len(artist))
print(url)
