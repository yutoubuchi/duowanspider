import requests
<<<<<<< HEAD
import json
import time
=======
>>>>>>> cd45aebe00cf03c07432f06a4a271df19a94291d
import pymongo
from bs4 import  BeautifulSoup
client = pymongo.MongoClient('localhost',27017)
duowan = client['duowan']
duowan_jiongtu = duowan['duowan_jiongtu']


<<<<<<< HEAD
client =pymongo.MongoClient('localhost',27017)
duowan = client['duowan']
duowan_jiongtu = duowan['duowan_jiongtu']
=======
>>>>>>> cd45aebe00cf03c07432f06a4a271df19a94291d
def get_url(url):
    duowan_data = requests.get(url)
    duowan_urllist = []
    soup = BeautifulSoup(duowan_data.text, 'lxml')
    for duowan_url in soup.select('#pic-list > li > em > a'):
        duowan_urllist.append(duowan_url.get('href'))
    return duowan_urllist

def get_id(url):
    duowan_id = []
    for duowan_ID in get_url(url):
        duowan_id.append(duowan_ID.split('/')[-1].split('.')[0])
    return duowan_id

def get_data(gid,data=None):
    respones = requests.get('http://tu.duowan.com/index.php?r=show/getByGallery/&gid='+str(gid)).json()
    duowan_newdata=[]
    for lens in range(0,len(respones['picInfo'])):
        data = {
            'pic_url':respones['picInfo'][lens]['source'],
            'ding':respones['picInfo'][lens]['ding'],
            'old':respones['picInfo'][lens]['old'],
            'cai': respones['picInfo'][lens]['cai'],
            'yema':lens,
            'id':gid,
        }
        #duowan_ceshi.insert_one(data)
    # return duowan_newdata
        print data

<<<<<<< HEAD

for id in get_id('http://tu.duowan.com/tag/5037.html'):
    print get_data(id)
    # duowan_jiongtu.insert_one(get_data(id))
# for item in duowan_jiongtu.find():
#     print item['ding']
=======
if __name__=='__main__':

    duowan_ceshi = duowan['duowan_ceshi']
    # for item in get_id('http://tu.duowan.com/tag/5037.html'):
    #     get_data(item)
    li=[]
    for item in duowan_ceshi.find():
        li.append(item)
    print sorted(li,key=lambda li:int(li['ding']))
    # print sorted(li,key=lambda li:li['ding'],reverse=True)

    # li=get_data(126343)
    # print sorted(li,key = lambda li:li['ding'])



#
# for item in duowan_jiongtu.find():
#     print item
# ding = respones.json()['picInfo'][1]['ding']
# url = 'http://tu.duowan.com/gallery/126187.html'''
# print url.split('/')[-1].split('.')[0]
>>>>>>> cd45aebe00cf03c07432f06a4a271df19a94291d
