from bs4 import BeautifulSoup
import urllib.request
import re

url = 'http://www.otographicmusic.com/tagged/releases'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

p = soup.prettify()

artist = []
title = []
url = []

for st in soup.find_all('strong'):
    rep = st.text.split("“")
    if len(rep)>1:
        artist.append(rep[0])
        title.append(rep[1].replace('"','').replace('”',''))
    else:
        pass

for ul in soup.find_all(class_='read_more'):
    url.append(ul['href'])


print(len(url))