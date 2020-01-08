# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:34:01 2020

@author: ChangYeol
"""
# train size를 고정시킨 뒤, 정확도를 비교

def NV_BY():
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
    for i in range (1,50):

        seed = i
        tr, ts, tr_lb, ts_lb = train_test_split(TRAIN, LABEL, train_size = 0.6, 
                                                random_state = seed)                
        model = GaussianNB()
        model.fit(tr, tr_lb)
        acc = model.score(ts, ts_lb)
        result = result.append({'seed':i,'accuracy':acc},ignore_index=True)
    
    plt.figure(figsize=(12,6))
    plt.plot(result['seed'], result['accuracy'])
    plt.xticks(range(1,50,1),range(1,50,1))

NV_BY()                    
