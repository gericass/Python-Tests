from bs4 import BeautifulSoup
import urllib.request
import re

url = 'http://www.edbangerrecords.com/site/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

pre = []

for h2 in soup.find_all("h2",class_="entry-title"):
    for art in h2.find_all("a"):
        pre.append(art.text)
        url.append(art['href'])


for i in range(len(pre)):
    if "“" in pre[i]:
      p = pre[i].split(" “")
      artist.append(p[0])
      q = p[1].replace("”","")
      title.append(q)
    elif "« " in pre[i]:
      p = pre[i].split("« ")
      artist.append(p[0])
      q = p[1].replace(" »","")
      title.append(q)
    else:
      artist.append("")
      title.append(pre[i])

print(pre)

print(len(artist))
print(len(title))
print(len(url))
