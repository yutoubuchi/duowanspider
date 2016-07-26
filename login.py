__author__ = 'wb.zsy'
import math,random
import binascii
from Crypto.Hash import MD5
from Crypto.Cipher import AES
import rsa
import requests,json
import base64

def pad(s): return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
def createSecretKey(size):
    keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = ''
    for i in range(size):
        pos = random.random() * len(keys)
        pos = math.floor(pos)
        key = key + keys[int(pos)]
    return key

def aesEncrypt(text, secKey):
    iv='0102030405060708'
    encrypted=AES.new(secKey, AES.MODE_CBC, iv)
    source=pad(text)
    ciphertext=encrypted.encrypt(source)
    return base64.b64encode(ciphertext)

def rsaEncrypt(text, pubKey, modulus):
    rsaPublickey = int(modulus,16)
    rsap=int(pubKey,16)
    key=rsa.PublicKey(rsaPublickey,rsap)
    encryptedString=rsa.encrypt(text,key)
    return binascii.b2a_hex(encryptedString)

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
    # encText=aesEncrypt('4297f44b13955235245b2497399d7a93','A3gnOdB0mcHl0JNO')
    # print encText
    # encText1=aesEncrypt(encText,'jfsu61kVDi0WAqAD')
    # print encText1
    # encText2=rsaEncrypt("jfsu61kVDi0WAqAD","010001",'00e31eb0e0d178706d97342f9c4c6d4fdb000e32ef177534639a5d2b0cfebff7222e0cbb98daf891fbe071f82a4880f24979142c86f9c7b6bb58973fbf4c257fd87f281a3e965f20454e8d570cd570d23cc52c3d2214a69f7caf230646339ccfd05cfc53030067ea947f72517b3da8183e37b4a8cb4f6f34cecf44fce835ad2cf5')
    # print encText2
    # print aesEncrypt('4297f44b13955235245b2497399d7a93','5tFZKN4bBeIg5a6A')
    url_preEncryptData='https://smartcameratest2.x.163.com/common/preEncryptData'
    headers={'Content-Type': 'application/json'}
    data={}
    preEncryptData=requests.post(url_preEncryptData,data=json.dumps(data),headers=headers)
    data_login=preEncryptData.json()['result']
    a=encrypt(PS,data_login['pubKey'],data_login['modulus'],data_login['nonce'])

    data={
    "phoneArea":"86",
    "phoneNumber":"15268521243",
    "password":a[0],
    "captcha":"",
    "secKey":a[1],
    "loginToken":data_login['loginToken']}
    print data
    url_login='https://smartcameratest2.x.163.com/common/fgadmin/login'
    b=requests.post(url_login,data=data,headers=headers)
    print b.text
