from bs4 import BeautifulSoup
import urllib.request

url = 'http://bunkai-kei.com/release/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

for ri2 in soup.find_all(class_='ri2'):
    ta = ri2.text
    artist.append(ta)

for ri3 in soup.find_all(class_='ri3'):
    tn = ri3.text
    title.append(tn)

for href in soup.find_all(class_='side_content'):
    link = href.find_all('a',href=True)
    for urls in link:
        url.append(urls['href'])

