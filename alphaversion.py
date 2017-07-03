from bs4 import BeautifulSoup
import urllib.request
import re

url = 'http://alphaversion.tv/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

for titw in soup.find_all(class_='works'):
    for name in titw.find_all(class_='name'):
        title.append(name.text)
    for cd in titw.find_all(class_='cdweb'):
        for a in cd.find_all('a'):
            if 'alphaversion.tv' in a['href']:
              url.append(a['href'])
            else:
              pass

for titf in soup.find_all(class_='freedl'):
    for name in titf.find_all(class_='name'):
        title.append(name.text)
    for cd in titf.find_all(class_='web'):
        for a in cd.find_all('a'):
            if 'alphaversion.tv' in a['href']:
                url.append(a['href'])
            else:
                pass





print(len(url))