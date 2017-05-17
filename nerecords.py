from bs4 import BeautifulSoup
import urllib.request

url = 'http://nerecords.tokyo/release.html'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")


artist = []
title = []
url = []

for ul in soup.find_all(class_='box'):
    for a in ul.find_all('a'):
      try:
        url.append('http://nerecords.tokyo/'+a['href'])
      except:
        pass
    for tit in ul.find_all(class_='title'):
     title.append(tit.text)



#print(p)
print(url)
print(title)