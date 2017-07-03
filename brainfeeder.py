from bs4 import BeautifulSoup
import urllib.request
import re

url = 'http://www.brainfeedersite.com/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

p = soup.prettify()

artist = []
title = []
url = []

pre = []
'''
for sl in soup.find_all(class_="slideshow"):
    for h2 in sl.find_all("h2"):
        pre.append(h2.text)
        for a in h2.find_all("a"):
            url.append(a['href'])
'''


for pc in soup.find_all(class_='list clear',id='loop'):
    for h2 in pc.find_all('h2'):
        for a in h2.find_all('a'):
            title.append(a.text)
            url.append(a['href'])



print(len(title))
print(len(url))
#print(p)
'''
at = pre[0].split(" – ")
artist.append(at[0])
title.append(at[1])
print(pre)
print(artist)
print(title)
'''