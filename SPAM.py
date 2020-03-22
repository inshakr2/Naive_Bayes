# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:11:57 2020

@author: ChangYeol
"""

import pandas as pd
import re

text = pd.read_csv('c:/TM/sms_spam.csv', engine = 'python' )
text = text.reindex(columns = ['text','type'])

def tokenize(message):
    message = message.lower()   # 소문자로 전환
    word = re.findall('[\w]+')
    