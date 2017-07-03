from bs4 import BeautifulSoup
import urllib.request

url = 'https://pform.thebase.in/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

pre = []

artist = []
title = []
url = []


for tit in soup.find_all(class_="itemTitle"):
    pre.append(tit.text)

for i in range(len(pre)):
    b = pre[i].replace("\n","")
    title.append(b)

for link in soup.find_all(class_="itemImg"):
    link2 = link.find_all("a")
    for urls in link2:
        url.append(urls['href'])

print(artist)