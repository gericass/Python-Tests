from bs4 import BeautifulSoup
import urllib.request

url = 'http://planet.mu/releases/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

for bbr in soup.find_all(class_="box-inner"):
    ra = bbr.find_all(class_="release-artist")
    rt = bbr.find_all(class_="release-title")

    for art in ra:
     artist.append(art.text)
    for tit in rt:
     title.append(tit.text)
     for link in tit.find_all("a"):
         url.append(link['href'])



