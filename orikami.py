from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://orikamirecords.bandcamp.com/music'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")


artist = []
title = []
url = []

p = soup.prettify()

for pn in soup.find_all('p',class_='title'):
    for ex in pn.find_all('span'):
        ex.extract()
    tit = re.sub('\s{2}',"",pn.text.replace("\n",''))
    title.append(tit)

for ol in soup.find_all('ol',class_="editable-grid music-grid columns-4 public"):
    for a in ol.find_all('a'):
        url.append('https://orikamirecords.bandcamp.com'+a['href'])


print(len(title))
print(url)
print(len(url))
#print(p)