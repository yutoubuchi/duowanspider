import requests
import json
import time
import pymongo
from bs4 import  BeautifulSoup

client =pymongo.MongoClient('localhost',27017)
duowan = client['duowan']
duowan_jiongtu = duowan['duowan_jiongtu']
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
    for lens in range(1,len(respones['picInfo'])):
        data = {
            'pic_url':respones['picInfo'][lens]['cmt_url'],
            'ding':respones['picInfo'][lens]['ding'],
            'old':respones['picInfo'][lens]['old'],
            'cai': respones['picInfo'][lens]['cai'],
        }
        print data


for id in get_id('http://tu.duowan.com/tag/5037.html'):
    print get_data(id)
    # duowan_jiongtu.insert_one(get_data(id))
# for item in duowan_jiongtu.find():
#     print item['ding']