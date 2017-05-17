from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://never-slept.bandcamp.com/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")


pre =[]
pre2 =[]
#artist = []
title = []
url = []

p = soup.prettify()

for tit in soup.find_all("p",class_="title"):
  title.append(tit.text)


#for i in range(len(title)):
#    title[i] = title[i].replace("\n","")

#for i in range(len(title)):
#    title[i] = re.sub("\s{2}","",title[i])



for link in soup.find_all("div",class_="leftMiddleColumns"):
    for link2 in link.find_all("a"):
        url.append(link2['href'])

#print(len(artist))
print(title)
print(p)