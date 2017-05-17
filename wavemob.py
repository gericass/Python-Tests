from bs4 import BeautifulSoup
import urllib.request
import re
url = 'https://wavemob.net/releases/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

info =  {"label":"wavemob","title":"","url":"","artist":"","key":0}

title = []
url = []

pretitle = [re.sub('\n','',a.text) for ent in soup.find_all('h6') for a in ent.find_all('a') if a.text != '\n']
preurl = [a['href']  if 'https://' in a['href'] else 'https://wavemob.net'+a['href'] for ent in soup.find_all('h6') for a in ent.find_all('a')]
rel = {}

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not(x in seen or seen_add(x))]

preurl2 = f7(preurl)

for i in range(len(preurl2)):
    rel[preurl2[i]] = pretitle[i]

#print(title)
#print(url)
#print(len(url))
#print(title)
print(rel)
#print(p)