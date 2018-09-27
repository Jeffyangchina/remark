#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import numpy as np
import re
import csv
import jieba
import os
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier as Rfc
from sklearn.model_selection import cross_val_score as cro_scor
import pandas as pd
from sklearn.utils import shuffle
import numpy as np
import operator
from functools import reduce
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import roc_auc_score as roc
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)
    return lis
def out_num(instr):
    outstr = re.sub("[^\D]", "", instr)
    return outstr
def del_stop(alist):
    filepath = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\stopword.txt'
    def stopwordslist(filepath):
        stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
        return stopwords
    stopwords = stopwordslist(filepath)
    # print('st:',stopwords)
    tstr = []
    for word in alist:
        sw = word.strip().lower()
        if sw not in stopwords:
            if word != '\t':
                wword=word.strip().upper()
                wnstr=out_num(wword)
                tstr.append(wnstr)
    rm_null(tstr)
    return tstr
def fill_matrix(alist,astr):#fenci fill the matrix
    import numpy as np
    import re
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    jfc_add = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    astr=out_num(astr)
    src_tb_word = re.sub(r, '', astr)
    cutlist = list(jieba.cut(src_tb_word))
    cutlist = del_stop(cutlist)
    zero_matrix = np.zeros(len(alist))
    for tcell in cutlist:
        if tcell in alist:
            h = alist.index(tcell)
            zero_matrix[h] = 1.
    return zero_matrix
def data_input(alist):
    import numpy as np
    if len(alist)<3:
        print('You may input 3 strings as Source name,Source table name,Source table column')
        r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input dataset\dnn_model.csv'#内含所有的分词结果，作了初步优化，去单个词，及一些错误的词，在停用词表内stopword.txt，可以再优化
    csvFile2 = open(model_path, "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)
    suml=[]
    src=[]
    src_tb=[]
    src_col=[]
    for xx in reader2:
        if xx:
            suml.append(xx)
    src=suml[0]#所有源名称
    src_tb=suml[1]#所有源表名分词结果
    src_col=suml[2]#所有源源字段分词结果
    csvFile2.close()
    # print('lth:',len(src),len(src_tb),len(src_col))#78 565+2120 =2763
    src_0 = np.zeros(len(src))
    try:
        src_word = alist[0].strip().upper()
        if src_word in src:
            i = src.index(src_word)
            src_0[i] = 1.
    except:
        print('You may need Source Name')
    try:
        temp_word = alist[1].strip()
        src_1 = fill_matrix(src_tb, temp_word)
    except:
        src_1= np.zeros(len(src_tb))
        print('You may need Source Table Name')
    try:
        col_word = alist[2].strip()
        src_2 = fill_matrix(src_col, col_word)
    except:
        src_2 = np.zeros(len(src_col))
        print('You may need Source Column Name')
    union = src_0.tolist() + src_1.tolist() + src_2.tolist()
    return union
def define_type(union):
    from sklearn.externals import joblib
    clf= joblib.load('lr.pkl')
    print(clf.predict_proba(union))

def add_label(tr_set, test_file):
    from sklearn.preprocessing import LabelEncoder as Le
    train_data = pd.read_csv(tr_set, header=None)

    shuf_data = shuffle(train_data)
    tr_x = shuf_data.iloc[:, :-1].values
    train_y_ = shuf_data.iloc[:, -1:].values
    train_y = pd.Series(train_y_)
    uni = train_y.unique
    lecode=Le()
    lecode.fit(uni)
    tr_y = lecode.transform(train_y_).toarray()
    print('te:', uni, type(uni), type(train_y_))
    print('te2:',tr_y)
tr_set = r'C:\Users\XUEJW\Desktop\yang_test\test.csv'
# add_label(tr_set)