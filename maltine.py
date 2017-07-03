from bs4 import BeautifulSoup
import urllib.request

url = 'http://maltinerecords.cs8.biz/release.html'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

release = []
url = []

h2tag = soup.find("h2")

text = h2tag.text.replace('\n','rep').split('rep')

for i in range(4):
 text.remove('')


#print(text)


for i in h2tag.find_all("a",href=True):
    link = i['href']
    #link.
    if 'http://' in link:
        url.append(link)

    if not 'http://' in link:
        if not '/'in link:
         link = 'http://maltinerecords.cs8.biz/' + link
         url.append(link)
        else:
         link = 'http://maltinerecords.cs8.biz' + link
         url.append(link)
    #print(link)

#for i in range(len(url)):
 #print(url[i])

for i in range(len(url)):
 print(text[i]+' - '+url[i])