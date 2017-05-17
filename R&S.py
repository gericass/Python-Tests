from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.randsrecords.com/releases'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

for art in soup.find_all(class_="artist"):
    artist.append(art.text)

for link in soup.find_all(class_="title"):
    url.append(link['href'])
    title.append(link.text)

print(url)
print(artist)
print(title)
