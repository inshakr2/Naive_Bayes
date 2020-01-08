# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:59:51 2020

@author: ChangYeol
"""
# train size를 변화시키면서 각 size당 입력값 : case 회만큼의 평균 정확도를 시각화
# default = 200

def NV_BY_acc(case=200):
                        ##### import section #####
                        
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    import pandas as pd
    import matplotlib.pylab as plt
    
                    ##### data load section #####
    
    data = pd.read_csv('c:/data/laptop.csv', encoding = 'cp949')
    data = pd.get_dummies(data)
    
    TRAIN = data.iloc[:,1:]
    LABEL = data.iloc[:,0]
    
                    ##### model #####
                    
    
    result = pd.DataFrame()
    for n in range(3,10):
        prob = n/10
        temp = list()
        
        for i in range (1,case):
            tr, ts, tr_lb, ts_lb = train_test_split(TRAIN, LABEL, train_size = prob)   
            model = GaussianNB()
            model.fit(tr, tr_lb)
            temp.append(model.score(ts, ts_lb))
            avr = sum(temp) / len(temp)
            
        result = result.append({'prob':prob,'avr_acc':avr},ignore_index=True)
    
    plt.figure(figsize=(12,6))
    plt.plot(result['prob'], result['avr_acc'])

NV_BY_acc(1000)
