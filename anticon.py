from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.anticon.com/store/music/anticon-releases'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")


preurl = []
pretitle = []
preartist = []

artist = []
title = []
url = []

p = soup.prettify()

for tit in soup.find_all(class_='product-meta'):
    for h3 in tit.find_all('h3'):
        artist.append(h3.text)
    for h4 in tit.find_all('h4'):
        title.append(h4.text)

for ul in soup.find_all(class_='product-image'):
    for a in ul.find_all('a'):
        url.append('https://www.anticon.com'+a['href'])



