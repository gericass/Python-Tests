from bs4 import BeautifulSoup
import urllib.request


url = 'http://www.moose-records.com/releases/'

key = True
while key:
  try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read()
    key = False
  except:
    pass

soup = BeautifulSoup(html, "lxml")



artist = []
title = []
url = []

p = soup.prettify()

for ul in soup.find_all(class_='image-slide-anchor content-fit'):
    if 'www.moose-records' in ul['href']:
      url.append(ul['href'])
    else:
      url.append('http://www.moose-records.com'+ul['href'])




print(p)
