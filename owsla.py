from bs4 import BeautifulSoup
import urllib.request

url = 'http://owsla.com/releases/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

#artist = []
#title = []
url = []

p = soup.prettify()

for link in soup.find_all(class_="view option valign"):
 url.append(link['href'])



