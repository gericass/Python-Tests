from bs4 import BeautifulSoup
import urllib.request
import re

url = 'http://fentplates.co.uk/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

url = [a['href'] if "http" in a['href'] else "http://fentplates.co.uk"+a['href'] for mgi in soup.find_all(class_="music-grid-item") for a in mgi.find_all('a')]
title = []

for msg in soup.find_all(class_="music-grid-item"):
    for tit in msg.find_all("p",class_="title"):
        for ex in tit.find_all('span'):
            ex.extract()
        moji = re.sub('\s{2}',"",tit.text.replace('\n','')) #連続した空白の削除
        title.append(moji)


'''
for mgi in soup.find_all(class_="music-grid-item"):
    for a in mgi.find_all('a'):
        print(a["href"])
'''