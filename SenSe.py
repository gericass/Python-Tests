from bs4 import BeautifulSoup
import urllib.request

url = 'http://sense-sapporo.jp/release'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

for cts in soup.find_all(class_="content_title_single"):
    title.append(cts.text)

for sh in soup.find_all(class_="subtitle_head"):
    artist.append(sh.text)

for link in soup.find_all(class_="hover-content"):
    link2 = link.find_all("a")
    for urls in link2:
        url.append(urls['href'])

print(title)