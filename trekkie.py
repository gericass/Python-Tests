from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.trekkie-trax.com/ep/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

for link in soup.find_all('div', style='text-align:center;'):
    link2 = link.find_all("a")
    for urls in link2:
        url.append(urls['href'])

print(url)