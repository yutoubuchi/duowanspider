import requests
import json
from bs4 import  BeautifulSoup

# url = 'http://tu.duowan.com/tag/5037.html'
# duowan_data = requests.get(url)
# duowan_urllist=[]
# duowan_id = []
# soup = BeautifulSoup(duowan_data.text,'lxml')
# duowan_urllabel = soup.select('#pic-list > li > em > a')
# for duowan_url in soup.select('#pic-list > li > em > a'):
#     duowan_urllist.append(duowan_url.get('href'))
# #
# for duowan_ID in duowan_urllist:
#     duowan_id.append(duowan_ID.split('/')[-1].split('.')[0])
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
    get_data(id)
# ding = respones.json()['picInfo'][1]['ding']
# url = 'http://tu.duowan.com/gallery/126187.html'''
# print url.split('/')[-1].split('.')[0]