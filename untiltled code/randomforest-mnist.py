#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
from sklearn.datasets import load_boston
from sklearn.datasets import load_digits
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import LinearSVR
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline as pl
import numpy as np
def diabets_get():#regress
    #data=load_diabetes()
    data=load_boston()
    ss = StandardScaler()
    xx=ss.fit_transform(data.data)
    #pca=PCA(n_components=1)
    #td=pca.fit_transform(data.data)
    x_tr, x_test, y_tr, y_test = train_test_split(xx, data.target.ravel(), test_size=0.05, random_state=33)
    print('0:',x_tr.shape,y_tr.ravel().shape)
    return (x_tr, x_test, y_tr, y_test)
def datainput():#classify
    digits=load_digits()
    x_tr,x_test,y_tr,y_test=train_test_split(digits.data,digits.target,test_size=0.2,random_state=33)
    ss=StandardScaler()
    x_tr=ss.fit_transform(x_tr)
    x_test=ss.fit_transform(x_test)
    target_name=digits.target_names.astype(str)
    return (x_tr ,x_test, y_tr, y_test,target_name)

x_tr,x_test,y_tr,y_test,tar_name=datainput()
x_,t_x,y_,t_y=diabets_get()
algo={'rf':RandomForestClassifier(n_estimators=191,min_samples_split=3),'svm':SVC(kernel='linear',gamma='auto')}
parameters={'kernel':('rbf','linear'),'C':range(1,4,1),'gamma':[0.125,0.25,0.5,1,2,4]}

regress_algo={'svm':LinearSVR(),'gb':GradientBoostingRegressor(n_estimators=70,learning_rate=0.1,max_depth=4,min_samples_leaf=4,max_features=0.5)}
#clf=algo['svm']
clf=regress_algo['gb']
def searchgrid(x=x_tr,y=y_tr,para=None,model=clf):

    para={'subsample':range(2,20,1),'min_samples_leaf':range(1,5,1)}
    clf=GridSearchCV(model,para)
    clf.fit(x,y)
    print('0:',clf.best_params_)
clf.fit(x_,y_)
#print(clf.coef_)
print(clf.score(t_x,t_y))
def getaccuracy(model=clf,x=x_test,y_test=y_test,tar_name=None):

    y_pre=model.predict(x)
    #print(classification_report(y_test,y_pre,target_name=tar_name))
    print(accuracy_score(y_test,y_pre))

#searchgrid(x_,y_)
#getaccuracy(x=t_x,y_test=t_y)
plt.plot(range(len(t_y)),t_y,color='black',label='actual')
plt.plot(range(len(clf.predict(t_x))),clf.predict(t_x),color='blue',linewidth=3,label='predict')
# plt.xticks(())
# plt.yticks(())
plt.show()