from bs4 import BeautifulSoup
import urllib.request
import re



anititle = []
link =[]
ajaurl = []
title_jp = []
season = ['Summer']#'Winter','Spring','Fall','Summer','Unknow']

for sea in season:
    url = 'https://9anime.to/filter?release[]=2015&language=subbed&season[]='+ str(sea)
    for page in range(1,3):
      url = url + '&page=' + str(page)
      req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
      response = urllib.request.urlopen(req)
      html = response.read()
      soup = BeautifulSoup(html, "lxml")


      for tit in soup.find_all(class_="name"):
         anititle.append(tit.text)
         link.append(tit['href'])

      for aja in soup.find_all(class_="poster"):
         ajaurl.append('https://9anime.to/'+aja['data-tip'])
     # time.sleep(1)

'''
for jptitle in ajaurl:
    url = jptitle
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")

    pre = []
    truetitle = ''

    for tit in soup.find_all("div",class_='meta'):
       for spa in tit.find_all("span"):
        pre.append(spa.text)

    pre2 = pre[4].replace("\n","")

    title = re.sub('\s{2}',"",pre2).split("; ")
    if len(title)>=2:
        if int(len(title[len(title)-1]))>=50:
            for tit in soup.find_all(class_="title"):
                tt = tit.text
            truetitle = re.sub('(\s2.+$)','',tt)
            title_jp.append(truetitle)
        else:
         title_jp.append(title[len(title)-1])

    else:
        if int(len(title[0]))>=50:
            for tit in soup.find_all(class_="title"):
              tt = tit.text
            truetitle = re.sub('(\s2.+$)','',tt)
            title_jp.append(truetitle)
        else:
         title_jp.append(title[0])
    #time.sleep(1)
'''
'''
print(len(ajaurl))
print(len(link))
print(title_jp)
print(len(title_jp))
print(len(anititle))
'''
for i in anititle:
    print(i)
'''
url = 'https://9anime.to/filter?release[]=2015&language=subbed&season[]=Winter'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

p =soup.prettify
print(p)
'''