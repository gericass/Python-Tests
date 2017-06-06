import urllib.request
import time


import requests
import json

page2 = ["1/","2/"]
year = ["2017/"]#,"2016/","2015/","2014/","2013/"]
season = ["Winter/","Spring/","Summer/","Fall/","Unknow/"]
page = ["1/","2/","3/","4/","5/"]


def getanime(): #全件取得
    start = time.time()
    for i in year:
        for j in season:
            for k in page:
                url = 'https://nineanimeapi.herokuapp.com/'+i+j+k
                urllib.request.urlopen(url)
                for p in page2:
                    url2 = 'https://nineanimeapi.herokuapp.com/week/'+p+i+j+k
                    urllib.request.urlopen(url2)
                    print(p+i+j+k)
                    #time.sleep(0.3)
    print(time.time()-start)


def gettitle(): #全タイトル取得
    start = time.time()
    for i in year:
        for j in season:
            for k in page:
               try:
                url = 'https://nineanimeapi.herokuapp.com/'+i+j+k
                urllib.request.urlopen(url)
                print(i+j+k)
               except:
                   print(i+j+k+" error")
    print(time.time()-start)


def dow():#曜日取得
    start = time.time()
    for i in page2:
        for j in year:
            for k in season:
                for m in page:
                   try:
                    url = 'https://nineanimeapi.herokuapp.com/week/'+i+j+k+m
                    urllib.request.urlopen(url)
                    print(i+j+k+m)
                   except:
                       print(i+j+k+m+" error")
    print(time.time()-start)

#gettitle()
dow()




'''
class test:

    def labelname(self):
        self.label = self.label + 'Records'


    def prints(self):
        self.labelname()
        return self.label

    def setLabel(self,label):
        self.label=label
        if label=='Altema':
           p = self.prints()
           return p

    def __init__(self):
        self.label=""

#a = test()
#print(test().setLabel('Maltine'))

'''

ACCESS_TOKEN = "VfiERPUAyZgGItiV0P7xYRuJLPL1krT9jB81YbK1V4hFoxDbMSSwRvTJzG4K7+eFFH0mobhsF5tcXtLtlSGWKq0uho67eg3Dh6Z6eImDBo8WKnwD63Do+Nfwa/PN9UQnG9c01HJgTk07RX0mquWUBQdB04t89/1O/w1cDnyilFU="

USER_EP = 'https://api.line.me/v2/bot/profile/'

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

id = ['U9cffcfa9f62705b889bfc4470efea951',
       'U292356a3876e7fabe5a7fd102fcf8ca4',
        'U7570a122c56eeaca11ac66c17d3c0758',
        'U2f800e64532b5ff37848c539c4717773',
        'U8ba475636ef0f000c5ce878fa54b0dbe',
        'U88b51781f95b55cdd9d4bdef5b475b9f',
        'U30bb59fa02f538c3e8c30da4ccd4a458',
        'Ud4dc78ca5fd9c8f01b3dd01ebfcfe959',
        'Uc4713d8f47518ab1c0831b4d7a20d771',
        'U7570a122c56eeaca11ac66c17d3c0758',
        'U862442f6f6026959239de28cda0e34a5',
        'U9cffcfa9f62705b889bfc4470efea951',
          'Ubf6cc15475b96604c7642a721acbe76b']

id2 = [
    'Uc3442fc507b0676154bde63fe3881be8',
    'U9cffcfa9f62705b889bfc4470efea951',
    'U292356a3876e7fabe5a7fd102fcf8ca4',
    'U7570a122c56eeaca11ac66c17d3c0758',
    'U2f800e64532b5ff37848c539c4717773',
    'U8ba475636ef0f000c5ce878fa54b0dbe',
    'U753686c9b984dfcd733d05d8884fe65c',
    'U88b51781f95b55cdd9d4bdef5b475b9f',
    'U30bb59fa02f538c3e8c30da4ccd4a458',
    'Ud4dc78ca5fd9c8f01b3dd01ebfcfe959',
    'Uc4713d8f47518ab1c0831b4d7a20d771',
    'U862442f6f6026959239de28cda0e34a5',
    'U582c93dbf5a97ab4affa4259f5068a33',
    'Ubf6cc15475b96604c7642a721acbe76b'
]
id3 = [
       'Ucb4a52b33a2aa39263ab5b9ff72dd86a',
       'U646c48e6007f672ed2adc993eab06b20',
       'U1502e942cd44806b72d271394ccd8218',
       'Uc3442fc507b0676154bde63fe3881be8',
       'U9cffcfa9f62705b889bfc4470efea951',
       'U292356a3876e7fabe5a7fd102fcf8ca4',
       'U7570a122c56eeaca11ac66c17d3c0758',
       'U2f800e64532b5ff37848c539c4717773',
       'U8ba475636ef0f000c5ce878fa54b0dbe',
       'U753686c9b984dfcd733d05d8884fe65c',
       'U88b51781f95b55cdd9d4bdef5b475b9f',
       'U30bb59fa02f538c3e8c30da4ccd4a458',
       'Ud4dc78ca5fd9c8f01b3dd01ebfcfe959',
       'Uc4713d8f47518ab1c0831b4d7a20d771',
       'U582c93dbf5a97ab4affa4259f5068a33',
       'Ubf6cc15475b96604c7642a721acbe76b'
]
'''
for i in id3:
 USER_EP = USER_EP + i
 p = requests.get(USER_EP,headers=HEADER)
 print(p.text)
 USER_EP = 'https://api.line.me/v2/bot/profile/'
'''
