#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
from sklearn.datasets import fetch_20newsgroups as f20
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as TF
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
tr_data=f20(subset='train',categories=['comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale'])#
tr_data_x=tr_data.data
tr_data_y=tr_data.target
te_data=f20(subset='test',categories=['comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale'])#
te_data_x=tr_data.data
te_data_y=tr_data.target
target_name=tr_data.target_names
from sklearn.svm import SVC
# def feature_work(data=None,vb=None,stop_words=None,max_df=1):
#     cv=CV(stop_words=stop_words,max_df=max_df,vocabulary=vb)
#     #print(cv.vocabulary)
#     tr_vb=cv.vocabulary_
#
#     tf=TF()
#     tf_idf=tf.fit_transform(cv.fit_transform(data))#词频和tfidf值
#     print('0:',cv.fit_transform(data).shape)
#     print('1:', tf_idf.shape)
#     #word=cv.get_feature_names()#词文本的关键字
#     #weight=tf_idf.toarray()
#     return tr_vb,tf_idf
cv=CV(stop_words='english',max_df=0.8)
tf=TF()
tr_idf=tf.fit_transform(cv.fit_transform(tr_data_x))#词频和tfidf值
print('0:',cv.fit_transform(tr_data_x).shape)
te_idf=tf.fit_transform(cv.fit_transform(te_data_x))#词频和tfidf值
print('1:',cv.fit_transform(te_data_x).shape)
#train feature tf_tr是训练输入从tr_data_x处理得来，tr_data_y训练目标没有修改
#tr_vb,tf_tr=feature_work(tr_data_x,stop_words='english',max_df=0.5)
#test feature
#te_vb,tf_te=feature_work(te_data_x,vb=tr_vb)

def getaccuracy(model=None,x=None,y_test=None,tar_name=None):

    y_pre=model.predict(x)
    print(classification_report(y_test,y_pre,target_names=tar_name))
    print(accuracy_score(y_test,y_pre))

#clf=MultinomialNB()
clf=SVC(kernel='linear')
clf.fit(tr_idf,tr_data_y)
getaccuracy(model=clf,x=te_idf,y_test=te_data_y,tar_name=target_name)