#!/usr/bin/env python
#_coding_ utf-8
from sklearn.model_selection import GridSearchCV

from sklearn.datasets import make_multilabel_classification
def classify(cdata,ydata,label,k):
    datasize=len(ydata)
    data2=[]
    fdata=[]
    outdata=[]
    outdict={}
    for i in range(datasize):#将距离值和对应的标签组成一个列表的元素
        for n in range(len(cdata)):
            datan = (cdata[n] - ydata[i][n])**2
            datan+=datan
        datan2=datan**0.5# calculate distance
        fdata.append([datan2,label[i]])#distance =>class
        #data2.append(data1)
    fdata.sort()
    if k> len(fdata):
        print('data is not enought')
    else:
        outdata=fdata[:k]
        for x in range(k):#排序后的列表，取出前k个元素，将他们的标签，并统计标签出现的次数，因为字典有统计方法。
            cell=outdata[x][1]
            outdict[cell]=outdict.get(cell,0)+1#字典统计值的数量，出现则get返回1否则0
        pdata=sorted(outdict.items(), key=lambda x: x[1], reverse=True)
        return pdata[0][0]
def sk_forest(xx,yy):
    from sklearn.ensemble import RandomForestClassifier
    clf=RandomForestClassifier(n_estimators=10)
    clf.fit(xx,yy)

# this will generate a random multi-label dataset多标签是只有1或0但有多个，而多类别则是只有一个但是有多种类可选
# X, y = make_multilabel_classification(sparse = True,n_classes=10,n_labels=18,
# return_indicator = 'sparse', allow_unlabeled = False,n_features=4000,n_samples=10000)

# xx=X[:8000]
# yy=y[:8000]
# xt=X[8500:8510]
# yt=y[8500:8510]
from sklearn.ensemble import RandomForestClassifier as classfy
#forest train score is: 0.982601491301
# forest test score is: 0.94
from sklearn.model_selection import cross_val_score as sc
# clf=classfy(random_state=10)
# from sklearn.ensemble import AdaBoostClassifier as classfy
# param_test1= {'n_estimators':range(10,71,10)}
# gsearch1= GridSearchCV(estimator = classfy(min_samples_split=100,
#                                  min_samples_leaf=20,max_depth=8,max_features='sqrt' ,random_state=10),
#                        param_grid =param_test1, cv=5)
# gsearch1.fit(xx.toarray(),yy.toarray())
# param_test2= {'max_depth':range(3,14,2), 'min_samples_split':range(50,201,20)}
# gsearch2= GridSearchCV(estimator = classfy(n_estimators= 10,
#                                  min_samples_leaf=20,max_features='sqrt' ,oob_score=True,random_state=10),
#    param_grid = param_test2,iid=False, cv=5)
# gsearch2.fit(xx.toarray(),yy.toarray())
# clf=classfy(n_estimators=10,max_depth=3,min_samples_split=50)
import pandas as pd
from sklearn.utils import shuffle
import numpy as np
import operator
from functools import reduce
from sklearn.preprocessing import OneHotEncoder
tr_set = r'C:\Users\XUEJW\Desktop\yang_test\data_set\tensor_input_train_set.csv'
test_file = r'C:\Users\XUEJW\Desktop\yang_test\data_set\tensor_input_test_set.csv'
# pwd = os.getcwd()
# os.chdir(os.path.dirname(tr_set))
train_data = pd.read_csv(tr_set,header=None)#不能有中文出现
# os.chdir(os.path.dirname(test_file))
test_data = pd.read_csv(test_file,header=None)
temp_data=pd.concat([train_data,test_data])
shuf_data=shuffle(temp_data)
print('1:',len(shuf_data))
train_x = shuf_data.iloc[:, :-1].values
train_y_ =shuf_data.iloc[:, -1:].values
ohe = OneHotEncoder()
ohe.fit([[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]])

labels=ohe.transform(train_y_).toarray()
print('0:',len(train_x),len(train_y_),len(labels))
# train_2 = np.array(train_y_).tolist()
# labels=reduce(operator.add,train_2)
# one_hot = pd.get_dummies(labels)
# one_hot = one_hot.astype('float')
clf=classfy(random_state=10)
xx=train_x[:-100]

yy=labels[:-100]
xt=train_x[-100:]
yt=labels[-100:]
print('train data shape is %,test data shape is %:',%(xx.shape,xt.shape))
clf.fit(xx,yy)
# yc=clf.fit(xx.toarray(),yy.toarray()).predict(xt.toarray())
scores=sc(clf,xt,yt)

# print('0:',yc)
print('forest train score is:',clf.score(xx,yy))
print('forest test score is:',clf.score(xt,yt))
# # print('2:',yt.toarray())
# print('3:',scores.mean())
# print('4:',gsearch1.best_score_,gsearch1.best_params_)
# print('5:',gsearch2.best_score_,gsearch2.best_params_)#5: 0.514285714286 {'max_depth': 3, 'min_samples_split': 50}