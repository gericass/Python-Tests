from bs4 import BeautifulSoup
import urllib.request

url = 'http://schole-inc.com/?page_id=18694'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []
title = []
url = []

p = soup.prettify()

print(p)