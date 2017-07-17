from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://www.futureclassic.com.au/releases/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

title = []
url = []
artist = []

for a in soup.find_all(class_="artist-name"):
    title.append(a['title'])
    url.append(a['href'])

print(len(title))
print(len(url))