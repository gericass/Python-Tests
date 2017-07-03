from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.revealedrecordings.com/releases/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

pre =[]

#artist = []
#title = []
url = []

p = soup.prettify()



for link in soup.find_all(class_="releaseblock"):
    for link2 in link.find_all("a"):
        pre.append(link2['href'])

for i in range(len(pre)):
    if 'http://www.revealedrecordings.com' in pre[i]:
        url.append(pre[i])

for i in range(len(url)):
    print(url[i])