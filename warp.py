from bs4 import BeautifulSoup
import urllib.request
import re
url = 'https://warp.net/releases/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

pre = []
pre2 = []

artist = []
title = []
url = []

for art in soup.find_all("p",class_="GridItem-title"):
    pre.append(art.text)

for i in range(len(pre)):
   b =  pre[i].replace('\n','')
   pre2.append(b)

for i in range(1,int((len(pre2)+2)/2)):
    title.append(pre2[i*2-1])
    #print(title[i])

for i in range(0,int((len(pre2))/2)):
    artist.append(pre2[i*2])

for i in range(len(title)):
    for link in soup.find_all("a",class_="GridItem-link",href=True,title=title[i]):
        url.append('https://warp.net' + link['href'])


for i in range(len(url)):
    print(url[i])

for i in range(len(artist)):
    print(artist[i])