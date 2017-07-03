from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://www.spinninrecords.com/releases/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

pre =[]
pre2 =[]
artist = []
title = []
url = []

p = soup.prettify()

for tit in soup.find_all("h2"):
   for link in tit.find_all("a"):
       title.append(link.text)
       url.append(link['href'])


for art in soup.find_all(class_="item music jscroll-content"):
    for art2 in art.find_all("p"):
        pre.append(art2.text)

for i in range(len(pre)):
    pre2.append(pre[i].replace("\n",""))

for i in range(len(pre2)):
     moji = re.sub('\s{2}',"",pre2[i]) #連続した空白の削除
     artist.append(moji)


print(len(title))
print(len(url))
print(artist)

