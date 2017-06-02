from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://www.whitepeachrecords.com/recordlabel/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

p = soup.prettify()

artist = []
title = []
url = []

print(p)