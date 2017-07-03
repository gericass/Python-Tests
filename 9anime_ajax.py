from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://9anime.to/ajax/film/tooltip/r92p?v21482059226'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

p = soup.prettify()

pre = []

tt = ''

for tit in soup.find_all("div",class_='meta'):
    for spa in tit.find_all("span"):
        pre.append(spa.text)

pre2 = pre[4].replace("\n","")

title = re.sub('\s{2}',"",pre2)

for tit in soup.find_all(class_="title"):
  tt = tit.text

tt2 = re.sub('(\s2.+$)','',tt)



print(pre)
#print(p)
print(tt2)
print(title)