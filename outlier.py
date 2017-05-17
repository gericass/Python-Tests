from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://outlierrecordings.bandcamp.com/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

title = []
url = []

p = soup.prettify()

for tit in soup.find_all("p",class_="title"):
    for ex in tit.find_all('span'):
        ex.extract()
    moji = re.sub('\s{2}',"",tit.text.replace('\n','')) #連続した空白の削除
    title.append(moji)

for link in soup.find_all("div",class_="leftMiddleColumns"):
    for link2 in link.find_all("a"):
        url.append('https://outlierrecordings.bandcamp.com'+link2['href'])



print(len(url))
print(len(title))
#print(p)