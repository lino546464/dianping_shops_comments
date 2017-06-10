# -*- coding : utf-8 -*-
import pymongo
import jieba
from collections import Counter
import pandas as pd
import re
import csv
import codecs
import pandas as pd

client = pymongo.MongoClient('127.0.0.1',27017)
db = client['耶里夏丽']
collection = db['1星']
shops = collection.find()
shop_words = []
shop_p = ''
for shop in shops:
    shop_i = dict(shop).get('comment')
    shop_s = str(shop_i).strip().replace('\xa0','')
    shop_p += shop_s
shop_l = jieba.lcut(shop_p.encode('utf-8'))
shopd = pd.DataFrame(shop_l,columns=['words'])


# print(shopd)
stopwords = pd.read_csv('stopwords.txt',encoding='utf-8',sep='\t\n',header=None,names=['stop'])
shop_df = shopd[~shopd.isin(list(stopwords['stop']))]
# print(shop_df)
wors = dict(Counter(list(shop_df['words'])))
# for word in wors:
print(wors)
for key in wors.keys():
    if len(str(key)) >1:
        value = str(wors.get(key))
        keys = str(key)
        pr = keys + ' ' +value
        print(key,wors.get(key))
        with open('commentseg.txt','a+',encoding='utf-8') as f:
            f.write(pr+'\n')
            # f.write(str(value))
# shop_c = shop_df.groupby(by=['words'])
# print(wors.keys())
# print(wors.values())

    # shop_l = shop_s.replace("'",'').replace('[','').replace(']','').strip()
    # for s in shop_j:
    #     print(s)