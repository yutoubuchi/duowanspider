__author__ = 'wb.zsy'
import math,random
import binascii
from Crypto.Hash import MD5
from Crypto.Cipher import AES
import rsa
import requests,json


def createSecretKey(size):
    keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = ''
    for i in range(size):
        pos = random.random() * len(keys)
        pos = math.floor(pos)
        key = key + keys[int(pos)]
    return key

def aesEncrypt(text, secKey):
    iv=b'0102030405060708'
    seckey1=secKey.encode('utf-8')
    encrypted=AES.new(seckey1, AES.MODE_CBC, iv)
    ciphertext=encrypted.encrypt(text)
    return ciphertext

def rsaEncrypt(text, pubKey, modulus):
    rsaPublickey = int(modulus, 16)
    rsap=int(pubKey, 16)
    key=rsa.PublicKey(rsaPublickey,rsap)
    encryptedString=rsa.encrypt(text,key)
    return encryptedString

def encrypt(text, pubKey, modulus, nonce):
    result=[]
    secKey = createSecretKey(16)
    encText = aesEncrypt(text, nonce)
    result.append(aesEncrypt(encText, secKey))
    result.append(rsaEncrypt(secKey, pubKey, modulus))
    return result




if __name__ == "__main__":
    password='123123'
    h = MD5.new()
    h.update(password.encode('utf-8'))
    PS=h.hexdigest()
    print aesEncrypt(PS,'5tFZKN4bBeIg5a6A')
    # url_preEncryptData='https://x.163.com/common/preEncryptData'
    # headers={'Content-Type': 'application/json'}
    # data={}
    # preEncryptData=requests.post(url_preEncryptData,data=json.dumps(data),headers=headers)
    # data_login=preEncryptData.json()['result']
    # a=encrypt(PS,data_login['pubKey'],data_login['modulus'],data_login['nonce'])
    #
    # data={
    # "phoneArea":"86",
    # "phoneNumber":"15268521243",
    # "password":a[0],
    # "captcha":"",
    # "secKey":a[1],
    # "loginToken":data_login['loginToken']}
    # print data
    # url_login='https://x.163.com/common/fgadmin/login'
    # b=requests.post(url_login,data=data,headers=headers)
    # print b.text
