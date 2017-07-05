from bs4 import BeautifulSoup
import urllib.request

url = 'http://schole-inc.com/?page_id=18694'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

artist = []

p = soup.prettify()

url = [a['href'] for vc in soup.find_all(class_="vc_col-sm-3") for a in vc.find_all("a")]
title = [strong.text for vc in soup.find_all(class_="vc_col-sm-3") for ptag in vc.find_all("p")  for strong in ptag.find_all("strong")]

for vc in soup.find_all(class_="vc_col-sm-3"):
    for ptag in vc.find_all("p"):
        for strong in ptag.find_all("strong"):
          strong.extract()
        artist.append(ptag.text.replace("\n",""))

#artist = [art for art in preartist if art != '']

artist = list(filter(lambda x:x!='',artist))

#print(p)
print(len(title))
print(artist)
print(len(url))