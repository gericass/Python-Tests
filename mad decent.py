from bs4 import BeautifulSoup
import urllib.request

url = 'http://maddecent.com/music/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

p = soup.prettify()

for link in soup.find_all("a",class_="thumb-link"):
    url.append(link['href'])

for tit in soup.find_all("h1",itemprop="name"):
    title.append(tit.text)

for art in soup.find_all("h2",class_="artist-name"):
    artist.append(art.text)

print(len(url))
print(len(title))
print(len(artist))

#print(p)