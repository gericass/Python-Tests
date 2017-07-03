from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.altemarecords.jp/release/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

altema = {"title":"","artist":"","url":""}
title = [] #タイトル
artist = [] #アーティスト名
url = [] #リンク

tn = soup.find_all(class_='track_name')
ta = soup.find_all(class_ = 'track_artist')
link = soup.find_all('a',href=True)

dl = soup.find_all("dl")

#print(dl)

for i in soup.find_all('a',href=True):
    #print(i['href'])
    url.append(i['href'])

for i in range(5):
    url.pop(0)

#print(url)

for i in range(len(tn)):
    n = str(tn[i])
    n2 = n.replace('<li class="track_name">','').replace('</li>','').replace('[','').replace(']','').replace('<del>','').replace('</del>','')
    title.append(n2)
    a = str(ta[i])
    a2 = a.replace('<li class="track_artist">','').replace('</li>','').replace('[','').replace(']','').replace('<del>','').replace('</del>','')
    artist.append(a2)

title.remove("K2")#.remove("SCHOOL GIRL AKATHISIA").remove("dots")
title.remove("SCHOOL GIRL AKATHISIA")
title.remove("dots")

artist.remove("V.A")#.remove("PandaBoY")
artist.remove("V.A")#.remove("PandaBoY")
artist.remove("PandaBoY")


for i in range(len(url)):
    url[i] = 'http://www.altemarecords.jp/release/'+url[i].replace("./","")



for i in range(len(title)):
    print(title[i] + ' - ' +artist[i]+' - '+url[i])
