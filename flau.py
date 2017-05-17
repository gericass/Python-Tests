from bs4 import BeautifulSoup
import urllib.request

url = 'http://flau.jp/releases.html'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

for tit in soup.find_all("section",class_="unit"):
    for h3 in tit.find_all("h3"):
        title.append(h3.text)
    for p in tit.find_all("p"):
        if p.text!='\xa0' and p.text!=' ' and p.text!='':
            artist.append(p.text)

    for link in tit.find_all("a",href=True):
        if link['href'] != '':
            if  'http://' in link['href']:
                url.append(link['href'])
            else:
                url.append('http://flau.jp/' + link['href'])


print(url)

