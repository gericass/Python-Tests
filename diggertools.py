from bs4 import BeautifulSoup
import urllib.request

url = 'https://salty-lake-16271.herokuapp.com/results/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

pre = []
artist = []
title = []
url = []

for art in soup.find_all(class_="type02"):
    for cla in art.find_all(class_='cell'):
        pre.append(cla.text)
    for tex in art.find_all(class_='text'):
        title.append(tex.text)

for i in range(int(len(pre)/2)):
    url.append(pre[i])

print(len(title))