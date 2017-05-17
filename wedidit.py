from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.wediditcollective.com/releases/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

for link in soup.find_all(class_="releases-wrapper"):
    for link2 in link.find_all("a"):
        url.append(link2['href'])
    for art in link.find_all("h4"):
        artist.append(art.text)
    for tit in link.find_all("h3"):
        title.append(tit.text)


print(artist)
print(title)