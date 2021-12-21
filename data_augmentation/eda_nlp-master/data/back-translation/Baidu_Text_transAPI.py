# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5
import pandas as pd
import numpy as np

# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def translation(query):
    # Set your own appid/appkey.
    appid = '20210903000934312'
    appkey = 'cDHzrX88JNEf8wIJvblM'

    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    # 调用百度翻译API将英文翻译成 冰岛语 ice 丹麦语 dan 德语 de 荷兰语 nl  挪威语 nor 瑞典语 swe
    from_lang = 'en'
    to_lang = 'dan'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    print(result)
    print(type(result))

    dst = str(result["trans_result"][0]["dst"])  # 取得翻译后的文本结果
    print(dst)
    return dst

def back_translation(query):
    # Set your own appid/appkey.
    appid = '20210903000934312'
    appkey = 'cDHzrX88JNEf8wIJvblM'

    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'dan'
    to_lang = 'en'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    print(result)
    print(type(result))

    dst = str(result["trans_result"][0]["dst"])  # 取得翻译后的文本结果
    print(dst)
    return dst

#数据输入
df = pd.read_csv('essays10.csv', encoding='UTF-8-sig')
print("原始数据data", df.shape, type(df))
print(df.head())
print([column for column in df])

print(df['text'][0:])
print(type(df['text'][0:]))

df2 = df['text'][0:1].map(translation).map(back_translation)
df2.to_csv('BT_dan.csv', encoding="utf-8", header=True,index=False)



