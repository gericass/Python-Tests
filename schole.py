from bs4 import BeautifulSoup
import urllib.request

url = 'http://schole-inc.com/?page_id=18694'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

preartist = []

artist = []
title = []
url = []

p = soup.prettify()

for vc in soup.find_all(class_="vc_col-sm-3"):
    for a in vc.find_all("a"):
        url.append(a['href'])

    for ptag in vc.find_all("p"):
        for strong in ptag.find_all("strong"):
          title.append(strong.text)
          strong.extract()

        preartist.append(ptag.text.replace("\n",""))


for art in preartist:
    if art != '':
        artist.append(art)


#print(p)
print(len(title))
print(len(artist))
print(len(url))