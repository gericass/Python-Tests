from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://luckyme.bleepstores.com/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

p = soup.prettify()

artist = []
title = []
url = []

pre = []
for id in soup.find_all(id="module-8209"):
    for dd in id.find_all("dd",class_="artist"):
        for a in dd.find_all("a"):
            artist.append(a['title'])

    for dd2 in id.find_all("dd",class_="release-title"):
        for a2 in dd2.find_all("a"):
            title.append(a2['title'])
            url.append("https://luckyme.bleepstores.com"+a2['href'])




print(title)
print(artist)
print(url)
print(len(title))
print(len(artist))
print(len(url))
#print(p)