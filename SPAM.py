# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:11:57 2020

@author: ChangYeol
"""

import pandas as pd
import re
from collections import defaultdict

text = pd.read_csv('c:/TM/sms_spam.csv', engine = 'python' )
text = text.reindex(columns = ['text','type'])



def tokenize(message):
    
    message = message.lower()           # 소문자로 전환
    word = re.findall('[\w]+', message) # 알파벳, 숫자만 추출
    return set(word)


a = defaultdict(lambda: [0, 0])
a

dic = {'a':1, 'b':3, 'c':7}
dic.setdefault('d',22)
dic.setdefault('a',9898)
dic.setdefault(1243,'asf')
dic.setdefault('abc',{123,124,125})
dic

dic1 = defaultdict()
dic1[0] = 1
dic1

dic2 = defaultdict(lambda: [0, 0])
dic2[0] = 1
print(dic2[0])

dic2[3]=1
print(dic2[3])

dic2[1][1]
dic2[1] 

dic2[4][2] = 4
dic2

dic2 = defaultdict(lambda: [0, 0])
dic2[2][0] = 5
dic2


defaultdict()
