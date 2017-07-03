from bs4 import BeautifulSoup
import urllib.request

url = 'https://anihayadjango.herokuapp.com/'#'http://ghostly.com/releases'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")


preurl = []
pretitle = []
preartist = []

artist = []
title = []
url = []

p = soup.prettify()
'''
for link in soup.find_all("dl",class_="artist-releases"):
    for link2 in link.find_all("a"):
        preurl.append(link2['href'])
    for art in link.find_all("dd",class_="artist"):
        preartist.append(art.text)
    for tit in link.find_all("dd",class_="title"):
        pretitle.append(tit.text)
'''

print(p)