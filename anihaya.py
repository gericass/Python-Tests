import json
import datetime
from urllib import request

day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']


def getjson():
     today = datetime.date.today()
     anijson = request.urlopen('http://nineanimeapi.herokuapp.com/api/?year='+str(today.year)+'&season=Winter')
     js = json.loads(anijson.read())
     #print(js)
     return js

def setTable():
      nameData = {
          'Mon':[],
          'Tue':[],
          'Wed':[],
          'Thu':[],
          'Fri':[],
          'Sat':[],
          'Sun':[],

      }
      urlData = {
          'Mon':[],
          'Tue':[],
          'Wed':[],
          'Thu':[],
          'Fri':[],
          'Sat':[],
          'Sun':[],
      }

      for anilist in getjson():
        for wkdy in day:
          if anilist['weekday']==wkdy:
              nameData[wkdy].append(anilist['title_jp'])
              urlData[wkdy].append(anilist['url'])

      maxDataNum = countDataNum(nameData)
      html = createTable(nameData,urlData,maxDataNum)
      #document.write(html);
      print(html)
      #print(str(maxDataNum))
      return maxDataNum


def countDataNum(nameData):
   max=0
   count=0
   soe=0
   for i in day:
    while count!=len(nameData[i]):#nameData[i][count]is (not None):
     count+=1
     if count>max:
      max=count
      soe=count
    count=0
   return soe





def createTable(nameData,urlData,maxDataNum):
         html=""
         for m in range(1,maxDataNum+1):#(var m=0;m<maxDataNum;m++)
            html+="<tr>"
            for i in day:#(var i=0;i<7;i++):
             if len(nameData[i])<m:
              html+="<td class=\"cell\"></td>"

             #elif urlData[i][m]=="":
              #   html+="<td class=\"cell\"></td>"

             elif len(nameData[i])>=m:
              html+="<td class=\"cell\"><a href=\""+urlData[i][m-1]+"\" target=\"brank\">"+nameData[i][m-1]+"</a></td>"

         return html

setTable()
#getjson()