import http.client
import hashlib
import json
import urllib
import random
import pandas as pd
import numpy as np
# 调用百度翻译API将英文翻译成 冰岛语 ice 丹麦语 dan 德语 de 荷兰语 nl  挪威语 nor 瑞典语 swe
def baidu_translate(content):
    appid = '20210903000934312'
    secretKey = 'nvL8sV0MLaADkhGl7wr7'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'en'  # 源语言
    toLang = 'de'  # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        # print(dst)  # 打印结果
        return dst
    except Exception as e:
        print('err:' + e)
    finally:
        if httpClient:
            httpClient.close()

def baidu_translate_back(content):
    appid = '20210903000934312'
    secretKey = 'nvL8sV0MLaADkhGl7wr7'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'de'  # 源语言
    toLang = 'en'  # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        # print(dst)  # 打印结果
        return dst
    except Exception as e:
        print('err:' + e)
    finally:
        if httpClient:
            httpClient.close()



if __name__ == '__main__':

    df = pd.read_csv('essays10.csv', encoding='UTF-8-sig')
    print("原始数据data", df.shape, type(df))
    print(df.head())

    print([column for column in df])

    print(df['text'][0:])
    print(type(df['text'][0:]))

    df2 = df['text'][0:].map(baidu_translate).map(baidu_translate_back)

    newAUTHID = pd.DataFrame(np.repeat(df['#AUTHID'].values, 1, axis=0))
    newcEXT = pd.DataFrame(np.repeat(df['cEXT'].values, 1, axis=0))
    newcNEU = pd.DataFrame(np.repeat(df['cNEU'].values, 1, axis=0))
    newcAGR = pd.DataFrame(np.repeat(df['cAGR'].values, 1, axis=0))
    newcCON = pd.DataFrame(np.repeat(df['cCON'].values, 1, axis=0))
    newcOPN = pd.DataFrame(np.repeat(df['cOPN'].values, 1, axis=0))

    df2 = pd.concat([df2, newAUTHID], axis=1)
    df2 = pd.concat([df2, newcEXT], axis=1)
    df2 = pd.concat([df2, newcNEU], axis=1)
    df2 = pd.concat([df2, newcAGR], axis=1)
    df2 = pd.concat([df2, newcCON], axis=1)
    df2 = pd.concat([df2, newcOPN], axis=1)

    df2.columns = ['text', '#AUTHID', 'cEXT', 'cNEU', 'cAGR', 'cCON', 'cOPN']
    cols = list(df2)
    cols.insert(1, cols.pop(cols.index('text')))  # 2是将d放在哪一列，cols.pop(cols.index('d')) 是要换的d列
    df2 = df2.loc[:, cols]  # 开始按照两列互换
    print(df2.head())

    df2.to_csv('BT_dan.csv', encoding="utf-8", header=True,index=False)
    # 将翻译后的英文写入文件
    # with open('huiyi', 'a', encoding="utf-8") as f:
    #     contents = ' '
    #     translate_en = baidu_translate(contents)
    #     print(translate_en)
    #     f.write('\t' + translate_en + '\n')


