from bs4 import BeautifulSoup
import urllib.request

url = 'http://nowadaysrecords.com/catalog/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")


artist = []
title = []
url = []

p = soup.prettify()

print(p)