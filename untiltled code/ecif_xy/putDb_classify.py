#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import sqlite3
import csv
import re
import os
import numpy as np
import jieba
from sklearn.externals import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import PCA
import tensorflow as tf
import time
from tensorflow.contrib import learn
import csv
from sklearn.preprocessing import OneHotEncoder
conn=sqlite3.connect(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\总集\Db_classify.db')
# conn=sqlite3.connect(r'C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\xy_zh_en.db')
def init(tb_name):
    sql_init1='drop table if EXISTS '+tb_name
    sql_init2='''create table '''+tb_name+''' (zh text PRIMARY KEY,en INT )'''
    cursor=conn.cursor()
    cursor.execute(sql_init1)
    cursor.execute(sql_init2)
    conn.commit()
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
def rm_puc(line):
    from zhon.hanzi import punctuation as zh_puc
    from string import punctuation as en_puc
    line=re.sub("[%s]+" % en_puc, "", line)
    line=re.sub("[%s]+" % zh_puc, "", line)
    return line
def rm_same(alist):
    outlis=[]
    for item in alist:
        if item not in outlis:
            outlis.append(item)
    return outlis
def rm_same_str(astr):
    alist=list(astr.split(' '))
    alist=rm_null(alist)
    alist=rm_same(alist)
    out_str=' '.join(alist)
    return out_str
def rm_space(astr):
    out_=re.sub(' ','',astr)
    return out_
def init_sp_tb():
    sql_init1 = 'drop table if EXISTS sampl_tb'
    sql_init2 = '''create table sampl_tb (src text,src_tb text,src_col text,tgt_tb text )'''
    cursor = conn.cursor()
    cursor.execute(sql_init1)
    cursor.execute(sql_init2)
    conn.commit()

def out_en(astr):
    outstr = re.sub("[a-zA-Z]", "", astr)
    outstr=outstr.strip()
    return outstr
def get_en(astr):
    outstr = re.sub("[^a-zA-Z]", "", astr)
    outstr = outstr.strip().upper()
    return outstr
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)
    return lis
def clean_input(instr):#only for new input
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    line = re.sub(r, '', instr)
    outstr = re.sub("[^\D]", "", line)
    outstr=out_en(outstr)
    return outstr
def put_in(filepath,tb_name):#file csv put into Db
    cursor=conn.cursor()
    # init(tb_name)
    csvFile = open(filepath, "r",encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    rows1=[]
    rows2=[]
    rows3=[]
    i=2
    h=0
    for row in reader:#row is a list,row[0] is a str,rows1 is a list
        if row:
            cell=row[0].strip().upper()
            # cel=out_num(cell)
            cel=cell
            en=row[1].strip()
            sql = 'insert into '+tb_name+' VALUES(?,?) '
            try:
                cursor.execute(sql,(cel,en))

            except Exception as e :
                # print('err:',e)
                h+=1
    print('unique is {}'.format(h))
    csvFile.close()
    conn.commit()
    cursor.close()

def add_tb(tb_name,astr):
    cursor = conn.cursor()
    sql = 'insert into ' + tb_name + ' VALUES(?,?) '
    try:
        cursor.execute(sql, (astr, 1))
    except Exception as e:
        print('err:', e)

    conn.commit()
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)
    return lis
def out_num(instr):
    outstr = re.sub('[0-9]+$', '', instr)
    outstr = re.sub('^[0-9]+', '', outstr)

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
                # wnstr=out_num(wword)
                wnstr=wword
                tstr.append(wnstr)
    rm_null(tstr)
    return tstr#is a list
def like_fill(astr):#fenci create list只分词及一般处理
    import numpy as np
    import re
    command = 'select * from fenci'
    sql = command
    cursor = conn.cursor()
    res = cursor.execute(sql)
    tempx = res.fetchall()
    fenci = []
    if tempx:
        for x in tempx:
            if x not in fenci:
                fenci.append(x[0])
    fenci_set = set(fenci)
    jieba.load_userdict(fenci_set)
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # jfc_add = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    # if os.path.isfile(jfc_add):
    #     jieba.load_userdict(jfc_add)
    # astr=out_num(astr)
    src_tb_word = re.sub(r, '', astr)
    cutlist = list(jieba.cut(src_tb_word))
    # cutlist = del_stop(cutlist)

    return cutlist
def read_fr_db(tb_name,astr):#输入查询的表名和名称,返回一个np的矩阵，用了tolist最后是数组
    command='select cell from '+tb_name
    sql = command
    cursor = conn.cursor()
    res=cursor.execute(sql)
    tempx = res.fetchall()
    astr=astr.strip().upper()
    if tempx:
        lth=len(tempx)
        out_list=np.zeros(lth)
        cell_list = [x[0].strip().upper() for x in tempx]
        if astr=='':
            return out_list.tolist()
        if tb_name=='Db_src':
            astr=get_en(astr)
            if astr in cell_list:
                i = cell_list.index(astr)
                out_list[i] = 1.
        else:
            stlist=like_fill(astr)#input a str output a jieba list
            for st in stlist:
                if st in cell_list:
                    i = cell_list.index(st)
                    out_list[i] = 1.
    else:
        print('no such column')

    fi_list=out_list.tolist()
    return fi_list
def deal_new_samp(astr):#处理一个新的名称，产生一个分词后的数组，且字数大于2
    command = 'select * from fenci'
    sql = command
    cursor = conn.cursor()
    res = cursor.execute(sql)
    tempx = res.fetchall()
    fenci = []
    if tempx:
        for tx in tempx:  # is a tuple
            fc=tx[0].strip()
            if fc not in fenci:
                fenci.append(fc)
        fenci_set=set(fenci)
    out_list=[]
    alist=like_fill(astr)
    for al in alist:
        if len(al)>1 or al in fenci:
            out_list.append(al)
    return out_list
def add_new_samptb(source=None):#source should be a list[src,src_tb,src_col,tgt]用于新增的分类
    if source:
        if len(source)>4:
            for x in range(4):
                if x==0:
                    data=get_en(source[x])
                    add_tb('Db_src',data)
                if x==1:
                    data_list=deal_new_samp(source[x])
                    for dl in data_list:
                        add_tb('Db_tb',dl)
                if x==2:
                    data_list = deal_new_samp(source[x])
                    for dl in data_list:
                        add_tb('Db_col', dl)


def data_input(alist):#由输入的数组，根据已有的模型预测分类结果
    import numpy as np
    if len(alist)<3:
        print('You may input 3 strings as Source name,Source table name,Source table column')
        r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    try:
        src_word = get_en(alist[0])
        src_word = src_word.strip().upper()
        src_0=read_fr_db('Db_src',src_word)#is src list[0,0,..] 76x1
    except:
        src_0 = read_fr_db('Db_src', '')
        print('You may need Source Name')
    try:
        src_word = alist[1].strip()
        src_1 = read_fr_db('Db_tb',src_word)#is src_tb list[0,0,..] 566x1
    except:
        src_1= read_fr_db('Db_tb','')
        print('You may need Source Table Name')
    try:
        src_word = alist[2].strip()
        src_2 = read_fr_db('Db_col',src_word)
    except:
        src_2 =  read_fr_db('Db_col','')
        print('You may need Source Column Name')
    union = src_0+ src_1 + src_2
    return union
def like_data_input(alist):#由样本表建模
    import numpy as np
    if len(alist)==4:
        r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
        try:
            src_word = get_en(alist[0])
            src_word = src_word.strip().upper()
            src_0=read_fr_db('Db_src',src_word)#is src list[0,0,..] 76x1
        except:
            src_0 = read_fr_db('Db_src', '')
        try:
            src_word = alist[1].strip()
            src_1 = read_fr_db('Db_tb',src_word)#is src_tb list[0,0,..] 566x1
        except:
            src_1= read_fr_db('Db_tb','')

        try:
            src_word = alist[2].strip()
            src_2 = read_fr_db('Db_col',src_word)# 2124
        except:
            src_2 =  read_fr_db('Db_col','')
        tgt_word = alist[3].strip().upper()

        if 'T00' in tgt_word  :
            tgt = [0]
        if 'T01' in tgt_word  :
            tgt = [1]
        if 'T02' in tgt_word  :
            tgt = [2]
        if 'T03' in tgt_word  :
            tgt = [3]
        if 'T04' in tgt_word  :
            tgt = [4]
        if 'T05' in tgt_word  :
            tgt = [5]
        if 'T06' in tgt_word  :
            tgt = [6]
        if 'T07' in tgt_word  :
            tgt = [7]
        if 'T08' in tgt_word  :
            tgt = [8]
        if 'T09' in tgt_word  :
            tgt = [9]
        if 'T10' in tgt_word  :
            tgt = [10]
        if 'T99' in tgt_word  :
            tgt = [11]
        if 'REF' in tgt_word  :
            tgt = [12]
        union = src_0+ src_1 + src_2+tgt
        # union =  src_1 + src_2+tgt
    return union

def jieba_cut(astr):#最终用于处理输入，常用词标点去除,返回空格连接的字符串
    command = 'select * from fenci'
    sql = command
    cursor = conn.cursor()
    res = cursor.execute(sql)
    tempx = res.fetchall()
    fenci = []
    data=[]
    if tempx:
        for x in tempx:
            if x not in fenci:
                fenci.append(x[0])
    fenci_set=set(fenci)
    jieba.load_userdict(fenci_set)
    # jieba.load_userdict(r"E:\兴业银行\中文翻译英文最终数据集\切词时用\分词库.txt")
    astr = astr.strip()
    ostr = rm_puc(astr)
    olist = list(jieba.cut(ostr))
    olist=rm_same(olist)
    olist = rm_null(olist)
    stopwords = stopwordslist(r'E:\yang_xy_test\ten class\stopword_zh_en.txt')
    for item in olist:
        if item:
            try:
                line = out_num(item).upper()
                line = rm_space(line)
                pt = out_en(line)
                if line not in stopwords:
                    if line != '\t' and len(line) > 0 and len(pt) > 0:
                        if line not in data:
                            data.append(line)


            except:
                print(item)

    zh_out = ' '.join(data)
    return zh_out
def samp_tb():
    command = 'select * from cleaned_temp_train'
    sql = command
    cursor = conn.cursor()
    res = cursor.execute(sql)
    tempx = res.fetchall()
    train_data=[]
    if tempx:
        for tx in tempx:#is a tuple

            train_data.append(like_data_input(list(tx)))
    # print('0:',type(train_data),train_data[0])#是个列表中列表
    return train_data#列表中列表
def data_input_allvocab(alist):#由输入的数组，根据已有的模型预测分类结果with src all vocab用这个
    import numpy as np
    if len(alist)<3:
        print('You may input 3 strings as Source name,Source table name,Source table column')
        r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    try:
        src_word = get_en(alist[0])
        src_word = src_word.strip().upper()
        src_0=read_fr_db('Db_src',src_word)#is src list[0,0,..] 76x1
    except:
        src_0 = read_fr_db('Db_src', '')
        print('You may need Source Name')
    try:
        src_word = alist[1].strip() + alist[2].strip()
        src_1 = read_fr_db('all_vocab', src_word)  # is src_tb list[0,0,..] 566x1
    except:
        src_1 = read_fr_db('all_vocab', '')


    union = src_0+ src_1
    return union
def temp_like_data_input(alist):#由样本表建模,
    import numpy as np
    if len(alist)==4:
        try:
            src_word = get_en(alist[0])
            src_word = src_word.strip().upper()
            src_0=read_fr_db('Db_src',src_word)#is src list[0,0,..] 76x1
        except:
            src_0 = read_fr_db('Db_src', '')
        try:
            src_word = alist[1].strip()+alist[2].strip()
            src_1 = read_fr_db('all_vocab',src_word)#is src_tb list[0,0,..] 566x1
        except:
            src_1= read_fr_db('all_vocab','')
        tgt_word = alist[3].strip().upper()

        if 'T00' in tgt_word:
            tgt = [0]
        if 'T01' in tgt_word:
            tgt = [1]
        if 'T02' in tgt_word:
            tgt = [2]
        if 'T03' in tgt_word:
            tgt = [3]
        if 'T04' in tgt_word:
            tgt = [4]
        if 'T05' in tgt_word:
            tgt = [5]
        if 'T06' in tgt_word:
            tgt = [6]
        if 'T07' in tgt_word:
            tgt = [7]
        if 'T08' in tgt_word:
            tgt = [8]
        if 'T09' in tgt_word:
            tgt = [9]
        if 'T10' in tgt_word:
            tgt = [10]
        if 'T99' in tgt_word:
            tgt = [11]
        if 'REF' in tgt_word:
            tgt = [12]

        # print('src0:',len(src_0))
        union =  src_0+src_1+tgt
    return union
def temp_samp_tb():
    command = 'select * from cleaned_temp_train'#这个表去掉了测试集
    sql = command
    cursor = conn.cursor()
    res = cursor.execute(sql)
    tempx = res.fetchall()
    train_data=[]
    i=0
    if tempx:
        for tx in tempx:#is a tuple
            train_data.append(temp_like_data_input(list(tx)))

    # print('00:',len(train_data))#是个列表中列表
    return train_data#列表中列表
def temp_src_emdb(shuf_data,pca):

    src_x_ = [x[:76] for x in shuf_data]
    tr_x_ = [x[76:-1] for x in shuf_data]

    src_x = pca.transform(src_x_)  # 输出np数组,就是数组中套数组
    tr_x = np.concatenate((src_x, tr_x_), axis=1)
    print('11:', len(tr_x[0]), len(src_x[0]))

    return tr_x
def src_embd(shuf_data):
    src_x_ = [x[:76] for x in shuf_data]
    tr_x_ = [x[76:-1] for x in shuf_data]
    print('0:', len(tr_x_[0]))
    pca = PCA(n_components=20)

    src_x = pca.fit_transform(src_x_)  # 输出np数组,就是数组中套数组
    tr_x = np.concatenate((src_x, tr_x_), axis=1)
    print('1:', len(tr_x[0]), len(src_x[0]))

    return tr_x,pca
def temp_create_model(model_path=None):

    train_data=temp_samp_tb()
    from sklearn.ensemble import RandomForestClassifier as Rfc

    import pandas as pd
    from sklearn.utils import shuffle
    shuf_data = shuffle(train_data)
    # tr_x_=[x[:-1] for x in shuf_data]
    # tr_x = tr_x_#输出np数组,就是数组中套数组
    tr_x,pca=src_embd(shuf_data)

    # tr_x = shuf_data.iloc[:, :-1].values#pandas读取的dataframe数据用该方法
    # train_y_ = shuf_data.iloc[:, -1:].values
    train_y_ = [[y[-1]] for y in shuf_data]
    # print('2:',len(tr_x),type(train_y_[0]))
    ohe = OneHotEncoder()
    ohe.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
    label_name = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T99', 'REF']
    tr_y = ohe.transform(train_y_).toarray()#这个输入必须是ohe.fit里格式
    clf = Rfc(random_state=0)  # oob_score
    # model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\classify model\yang_Rf_model.pkl'
    clf.fit(tr_x, tr_y)
    print('train score is {0}'.format(clf.score(tr_x, tr_y)))
    joblib.dump(clf, model_path)
    return ohe,pca
def create_model(model_path):

    train_data=samp_tb()
    from sklearn.ensemble import RandomForestClassifier as Rfc

    import pandas as pd
    from sklearn.utils import shuffle
    shuf_data = shuffle(train_data)
    tr_x=[x[:-1] for x in shuf_data]
    # tr_x = shuf_data.iloc[:, :-1].values
    # train_y_ = shuf_data.iloc[:, -1:].values
    train_y_ = [[y[-1]] for y in shuf_data]
    # print('2:',train_y_[0],type(train_y_[0]))
    ohe = OneHotEncoder()
    ohe.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
    label_name = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T99', 'REF']
    tr_y = ohe.transform(train_y_).toarray()#这个输入必须是ohe.fit里格式
    clf = Rfc(random_state=0)  # oob_score
    # model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\classify model\yang_Rf_model.pkl'
    clf.fit(tr_x, tr_y)
    print('train score is {0}'.format(clf.score(tr_x, tr_y)))
    joblib.dump(clf, model_path)
def get_rown():#检测样本和特征有没有增加，如果增加修改记录表
    tb_name=['Db_src','Db_tb','Db_col','samp_tb']
    rowli = []
    for x in tb_name:
        command = 'select count(*) from ' + x
        sql = command
        cursor = conn.cursor()
        res = cursor.execute(sql)
        tempx = res.fetchall()

        if tempx:
            rown=tempx[0][0]
            rowli.append(rown)
    # print('tt:',rowli)
    get_sql='select * from mark'
    getres = cursor.execute(get_sql)
    existed = getres.fetchall()
    if existed:
        ex_temp=list(existed[0])
    ex_temp=list(map(int,ex_temp))
    print(ex_temp)
    if rowli!=ex_temp:#数据有变化，从新训练
        for x in range(4):
            sqls = 'update mark set '+tb_name[x]+'='+str(rowli[x])
            res=cursor.execute(sqls)
            conn.commit()
        # create_model( r'E:\yang_xy_test\ten class\model\2018-05-08_model.pkl')

def do_class(alist,model):#最后用于分类with all vocab即合并了表和字段名
    union=[data_input_allvocab(alist)]
    label_name = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T99', 'REF']

    clf = joblib.load(model)
    pre_out=clf.predict(union)
    prob_out=clf.predict_proba(union)
    # print(pre_out)
    for item in pre_out:
        ind = np.where(item == 1)
    id=ind[0].tolist()
    if len(id)>0:
        print(label_name[id[0]])
        print('pro:',prob_out[id[0]][0][1])
        score_pre=prob_out[id[0]][0][1]
        if score_pre>0.9:
            return label_name[id[0]]
        else:
            return 'Null'
    else:
        # print('no class')
        return 'Null'
def temp_data_input(path):#由输入的数组，根据已有的模型预测分类结果

    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    te_data=[]
    for item in reader:  # 读取每一行
        if item:

            te_data.append(temp_like_data_input(item))
    print('te_len:', len(te_data),len(te_data[0]))  # 是个列表中列表
    return te_data  # 列表中列表
def final_batch_test(file_path, tgt_lh=None):  # sum all and test seperate ,one label
    from sklearn.utils import shuffle
    te_path = os.path.join(file_path, 'te')
    tr_path = os.path.join(file_path, 'tr')
    model_path = os.path.join(file_path, 'model\\union_model.pkl')
    # ohe,pca=temp_create_model(model_path)
    ohe,pca=temp_create_model(model_path)
    rootdir = te_path
    clf = joblib.load(model_path)
    lists = os.listdir(te_path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])

        if os.path.isfile(path):

            te_data=temp_data_input(path)
            shufte_data = shuffle(te_data)
            te_x=temp_src_emdb(shufte_data,pca)
            # te_x_ = [x[:-1] for x in shufte_data]
            # te_x=te_x_

            te_y_ = [[y[-1]] for y in shufte_data]
            # print('2:', te_y_[0], type(te_y_[0]))
            te_y = ohe.transform(te_y_).toarray()  #

            print('file name is {1},te_score is {0}'.format(clf.score(te_x, te_y), lists[i]))
def temp_tensor_get():
    command = 'select * from cleaned_temp_train'#这个表去掉了测试集
    sql = command
    cursor = conn.cursor()
    res = cursor.execute(sql)
    tempx = res.fetchall()
    train_data=[]
    out_y=[]
    i=0
    ohe = OneHotEncoder()
    ohe.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])

    if tempx:
        for tx in tempx:
            src0=tx[0].strip().upper()
            src1=tx[1].strip()
            src2=tx[2].strip()

            if len(src0)!=0 or len(src1)!=0 or len(src2)!=0 :
                src_sum=src1+src2
                temp_src_li=jieba_cut(src_sum)
                src_li=src0+' '+temp_src_li
                tgt_word=tx[3].strip()
                if tgt_word == 'T00':
                    tgt = [0]
                if tgt_word == 'T01':
                    tgt = [1]
                if tgt_word == 'T02':
                    tgt = [2]
                if tgt_word == 'T03':
                    tgt = [3]
                if tgt_word == 'T04':
                    tgt = [4]
                if tgt_word == 'T05':
                    tgt = [5]
                if tgt_word == 'T06':
                    tgt = [6]
                if tgt_word == 'T07':
                    tgt = [7]
                if tgt_word == 'T08':
                    tgt = [8]
                if tgt_word == 'T09':
                    tgt = [9]
                if tgt_word == 'T10':
                    tgt = [10]
                if tgt_word == 'T99':
                    tgt = [11]
                if tgt_word == 'REF':
                    tgt = [12]
                union=[src_sum]+tgt
                out_y.append(union)

    return out_y


def only_test(file_path):
    from sklearn.utils import shuffle
    te_path = os.path.join(file_path, 'te')
    rootdir = te_path
    model_path = os.path.join(file_path, 'model\\union_model.pkl')
    clf = joblib.load(model_path)
    lists = os.listdir(te_path)  # 列出文件夹下所有的目录与文件
    ohe = OneHotEncoder()
    ohe.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])

        if os.path.isfile(path):
            te_data = temp_data_input(path)
            shufte_data = shuffle(te_data)
            te_x_ = [x[:-1] for x in shufte_data]
            te_x = te_x_
            # te_x=pca.transform(te_x_)

            te_y_ = [[y[-1]] for y in shufte_data]
            # print('2:', te_y_[0], type(te_y_[0]))
            te_y = ohe.transform(te_y_).toarray()  #

            print('file name is {1},te_score is {0}'.format(clf.score(te_x, te_y), lists[i]))

def tiny_class_deal(fpath):  # 处理文字，去重去空格,去除尾部数字

    suml = []
    i = 1
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'CleanForTiny_' + lists[i])
        if os.path.isfile(path) and '.csv' in path:
            data_in = {}
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            for item in reader:
                if item:
                    src=item[0].strip().upper()
                    src_tb=item[1].strip()
                    tgt_col=item[3].strip()
                    src_col=item[2].strip()
                    tgt=item[4].strip()
                    if len(tgt)>0:
                        # wor = src_tb  + src_col#只取源系统名、源表名和字段名，目标的都不放
                        # wor = tgt_col  + tgt#只取目标表名和字段名，其他源不放
                        # wor = src_tb + tgt_col + src_col + tgt#源和目标都放在一起

                        temp_vocab = jieba_cut(tgt_col)+' '+jieba_cut(tgt)
                        tgt_vocab = temp_vocab
                        # temp_vocab = jieba_cut(src_tb)+' '+jieba_cut(src_col)
                        # tgt_vocab = src + ' ' + temp_vocab

                        tgt_vocab=rm_same_str(tgt_vocab)
                        list_vocab=list(tgt_vocab.split(' '))

                        list_vocab=rm_null(list_vocab)
                        if tgt not in data_in:
                            data_in[tgt]=list_vocab
                        else:
                            for cell in list_vocab:
                                if cell not in data_in[tgt]:
                                    data_in[tgt].append(cell)
            for xt in data_in:
                writer3.writerow([xt]+data_in[xt])
            csvFile.close()
            csvFile3.close()
def rm_zero(alist):
    nu=len(alist)
    for i in range(len(alist)):
        if alist[i][1]<0.05:
            if i>0:
                nu=i-1
            else:
                nu=0
            break
    return alist[:nu]
def get_biggest(alist):#求一个列表最大的前n项,输出是下标的数组
    st=[]
    out={}

    for i in range(len(alist)):
        st.append((i,alist[i]))
    st.sort(key=lambda x: x[1] ,reverse = True)
    in_list=rm_zero(st)
    for i in range(len(in_list)):
        out[in_list[i][0]]=in_list[i][1]
    return out
def sort_list(alist,blist):#对一个列表，排序后输出一个列表，元素是元组,(下标,数值）
    st=[]
    out=[]
    for i in range(len(alist)):
        st.append((i,alist[i]))
    st.sort(key=lambda x: x[1] ,reverse = True)#第一位是下标
    for xx in st:
        if  xx[1]<0.05:
            tyc='Null'
            tys=0.
        else:
            tyc=blist[xx[0]]
            tys=xx[1]
        out.append((tyc,tys))#列表元素是个元组，(类别，得分 )
    return out
def tf_idf(fpath):#求取关键字
    from sklearn.feature_extraction.text import TfidfVectorizer
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'tfIdf_' + lists[i])
        csvFile = open(path, "r", encoding='UTF-8')
        reader = csv.reader(csvFile)  # 返回的是迭代类型
        csvFile3 = open(new_path, 'w', newline='',
                        encoding='UTF-8')  # 设置newline，否则两行之间会空一行
        writer3 = csv.writer(csvFile3)
        typeName=[]
        typeWord=[]

        for item in reader:
            if item:
                typeName.append(item[0])
                temp_li=item[1:]
                temp_wo=' '.join(temp_li)
                typeWord.append(temp_wo)
        tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")#表示不考虑停用词
        weight = tfidf.fit_transform(typeWord).toarray()#返回每个样本对应每行一个列表，长度为词汇表长，对应样本中词汇的权重
        word = tfidf.get_feature_names()#获取词汇表
        # print('w:', len(weight[0]),len(weight[2]))
        for i in range(len(weight)):
            keyW = []
            keyW_P=get_biggest(weight[i])#是个字典，键是下标索引，值是得分

            for x in keyW_P:
                in_d=word[x].upper()+':'+str(keyW_P[x])
                keyW.append(in_d)

            writer3.writerow([typeName[i]]+keyW)
        csvFile.close()
        csvFile3.close()
# tiny_class_deal(r'E:\yang_xy_test\tiny_train\T01数据')
# final_batch_test(r'E:\yang_xy_test\ten class\test', 13)
# only_test(r'E:\yang_xy_test\ten class\test')
# temp_create_model()
# tf_idf()
def split_item(item):
    itm = list(item.split(':'))
    inx = float(itm[1])
    wnx = itm[0]
    return wnx,inx
def get_score_dic(adic,alist):
    score=0.
    for item in alist:
        if item in adic:
            score+=adic[item]
    return score

def test_tiny_class(src,src_tb,src_col):
    src=get_en(src.strip()).upper()
    temp_vocab = jieba_cut(src_tb) + ' ' + jieba_cut(src_col)
    tgt_vocab = rm_same_str(temp_vocab)
    list_vocab = list(tgt_vocab.split(' '))
    score1=[]
    score2=[]
    typeName = []
    csvFile0 = open(r'E:\yang_xy_test\tiny_train\T01数据\keyWord0.csv', "r", encoding='UTF-8')
    reader0 = csv.reader(csvFile0)
    csvFile1 = open(r'E:\yang_xy_test\tiny_train\T01数据\keyWord1.csv', "r", encoding='UTF-8')
    reader1 = csv.reader(csvFile1)  # 返回的是迭代类型
    i=0
    for item in reader0:#item 是一行是一个数组，每个元素是字符串类型,'word:0.01'
        if item:
            lth=len(item)
            sWordPro={}
            typeName.append(item[0])
            for xi in range(1,lth):
                wx,nx=split_item(item[xi])
                sWordPro[wx]=nx#字典，键是单词，值是他的分数
            sc1 = get_score_dic(sWordPro, list_vocab)#输入的样本，求得属于一个类的分数
            score1.append(sc1)

    for item in reader1:#item 是一行是一个数组，每个元素是字符串类型,'word:0.01'
        if item:
            lth=len(item)
            tWordPro={}
            # typeName.append(item[0])
            for xi in range(1,lth):
                wx,nx=split_item(item[xi])
                tWordPro[wx]=nx#字典，键是单词，值是他的分数
            sc2=get_score_dic(tWordPro,list_vocab)
            score2.append(sc2)
    score_sum=[]
    for i in range(len(score1)):
        score_sum.append(score1[i]+score2[i])
    class_pro = sort_list(score_sum, typeName)

    csvFile1.close()
    csvFile0.close()
    return class_pro[0]
def batch_tiny_class(rootdir):
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'ClassForTiny_' + lists[i])

        csvFile = open(path, "r", encoding='UTF-8')
        reader = csv.reader(csvFile)  # 返回的是迭代类型
        csvFile3 = open(new_path, 'w', newline='',
                        encoding='UTF-8')  # 设置newline，否则两行之间会空一行
        writer3 = csv.writer(csvFile3)
        for item in reader:
            if item:
                src = item[0].strip().upper()
                src_tb = item[1].strip()
                tgt_col = item[2].strip()
                src_col = item[3].strip()
                tgt = item[4].strip()
                final_class=test_tiny_class(src,src_tb,src_col)
                writer3.writerow([src,src_tb,src_col,tgt_col,tgt,final_class])
        csvFile.close()
        csvFile3.close()
def sp_rm_same(alist):#因为每个元素是个字符串，要分开比较单词及分数部分
    out=[]

    wor_sco={}
    for xx in alist:
        lx=list(xx.split(':'))
        wod=lx[0]
        sro=lx[1]
        if wod not in wor_sco:
            wor_sco[wod]=sro
        else:
            if float(sro)>float(wor_sco[wod]):
                wor_sco[wod]=sro
    for item in wor_sco:
        out_str=item+':'+wor_sco[item]
        out.append(out_str)
    return out
def union_2w():#合并两个excel表

    csvFile0 = open(r'E:\yang_xy_test\tiny_train\T99数据\dataset\tfIdf_CleanForSrc_T99.csv', "r", encoding='UTF-8')
    reader0 = csv.reader(csvFile0)
    csvFile1 = open(r'E:\yang_xy_test\tiny_train\T99数据\dataset\tfIdf_CleanForTgt_T99.csv', "r", encoding='UTF-8')
    reader1 = csv.reader(csvFile1)
    csvFile3 = open(r'E:\yang_xy_test\tiny_train\T99数据\dataset\keyWord_sum.csv', 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer3 = csv.writer(csvFile3)
    className=[]
    wordKey0=[]
    wordKey1=[]
    for item in reader0:
        if item:
            className.append(item[0])
            wordKey0.append(item[1:])
    for item in reader1:
        if item :
            wordKey1.append(item[1:])
    for xx in range(len(className)):
        cln=className[xx]
        wln=wordKey0[xx]+wordKey1[xx]
        wln_in=sp_rm_same(wln)
        writer3.writerow([cln]+wln_in)
    csvFile3.close()
    csvFile1.close()
    csvFile0.close()
def get_tbName_list(cursor):
    out_li=[]
    sql0 = "SELECT name FROM sqlite_master WHERE type='table'"
    res = cursor.execute(sql0)
    tempx = res.fetchall()
    for xx in tempx:
        out_li.append(xx[0])
    return out_li
def get_rownm(tb_name,cursor):#获取一个表的总行数
    sql0 = 'select count(*) from '+tb_name
    res = cursor.execute(sql0)
    tempx = res.fetchall()
    if tempx:
        row_sum = tempx[0][0]
    return row_sum
def get_col_word(tb_name,col_name,cursor):#获取表中一列所有字段
    out_li=[]
    sql0 = 'select '+col_name+' from '+tb_name
    res = cursor.execute(sql0)
    tempx = res.fetchall()
    for xx in tempx:
        out_li.append(xx[0])
    return out_li
def get_score_sub(WoP_list,inlist):#输入元组为元素的列表，分割成字典并由该字典求得分
    lth=len(WoP_list)
    out_dic={}
    for xi in range(lth):
        wx, nx = split_item(WoP_list[xi])
        out_dic[wx] = nx  # 字典，键是单词，值是他的分数
    sc_out=get_score_dic(out_dic,inlist)
    return sc_out
def get_score_fr_db(item,tb_name,cursor,inlist):#获取输入Inlist在表中某行类别的得分
    command = 'select * from '+tb_name+' where (class like ?)'
    res = cursor.execute(command, (item,))
    tempx = res.fetchall()
    WoP_list_ = [x for x in tempx[0] if x]#获得单个类别下单词及其权重值,['word:value',..]
    WoP_list=WoP_list_[1:]
    sc_out=get_score_sub(WoP_list,inlist)#计算inlist的得分
    return sc_out
def tiny_class_fr_db(src,src_tb,src_col,preClass):#细分类主接口
    src=get_en(src.strip()).upper()
    temp_vocab = src+' '+jieba_cut(src_tb) + ' ' + jieba_cut(src_col)
    tgt_vocab = rm_same_str(temp_vocab)
    list_vocab = list(tgt_vocab.split(' '))
    WordPro=[]
    typeName = []
    db_path=r'E:\yang_xy_test\tiny_train\tiny_classify.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    tbName_list=get_tbName_list(cursor)
    if preClass in tbName_list:
        row_num=get_rownm(preClass,cursor)
        typeName=get_col_word(preClass,'class',cursor)
        for item in typeName:
            score_value= get_score_fr_db(item,preClass,cursor,list_vocab)#对每个类别统计得分
            WordPro.append((item,score_value))
        WordPro.sort(key=lambda x: x[1], reverse=True)
        if WordPro[0][1] <0.1:
            class_pro=''
        else:
            class_pro = WordPro[0][0]
    else:
        class_pro=''
    print(class_pro)
    return class_pro

def pre_class_use_ml(src,src_tb,src_col):
    model_clf = './cnn-text-classification-tf-master/with src all vocab.pkl'
    alist=[src,src_tb,src_col]
    Tenclass=do_class(alist,model_clf)
    if Tenclass!='Null':
        TinyClass=tiny_class_fr_db(src,src_tb,src_col,Tenclass)
    else:
        TinyClass=''
    print('BClass is {0},TClass is {1}'.format(Tenclass,TinyClass))
    return Tenclass,TinyClass

checkpoint_file = r'./cnn-text-classification-tf-master/run/checkpoints/model-79200'
meta_graph=r'./cnn-text-classification-tf-master/run/checkpoints/model-79200'
parent_path=r'./cnn-text-classification-tf-master/run'
def singal_test(x_raw):#注意输入的格式,数组中数组
    vocab_path = os.path.join(parent_path, "vocab")
    vocab_processor = learn.preprocessing.VocabularyProcessor.restore(vocab_path)
    graph = tf.Graph()
    with graph.as_default():
        session_conf = tf.ConfigProto(
            allow_soft_placement=True,
            log_device_placement=False)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            saver = tf.train.import_meta_graph("{}.meta".format(meta_graph))
            saver.restore(sess, checkpoint_file)
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]
            scores=graph.get_operation_by_name("output/scores").outputs[0]

            predictions = graph.get_operation_by_name("output/predictions").outputs[0]

            x_test = np.array(list(vocab_processor.transform(x_raw)))
            sco=sess.run(scores, {input_x: x_test, dropout_keep_prob: 1.0})#是np.ndarray
            print('scores0:', sco,type(sco))

            predict_out= sess.run(predictions, {input_x: x_test, dropout_keep_prob: 1.0})
            print('scores1:', sco[0][predict_out[0]])
            return predict_out
def pre_class_use_dl(src,src_tb,src_col):
    src=src.strip().upper()
    src_tb=jieba_cut(src_tb.strip())
    src_col=jieba_cut(src_col)
    src_sum=src+' '+src_tb+' '+src_col
    src_instr = rm_same_str(src_sum)
    PreOut=singal_test([src_instr])
    print('y:',PreOut)
    if PreOut:
        label_name = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T99', 'REF']
        out_label = label_name[PreOut[0]]
    else:
        out_label = 'Null'
    if out_label != 'Null':
        tiny_label = tiny_class_fr_db(src, src_tb, src_col, out_label)
    else:
        tiny_label = ''
    return out_label, tiny_label
    return out_label
def main_interface(atable):#表进入接口
    src=[]
    src_tb=[]
    src_col=[]
    for item in atable:
        src.append(item[0])
        src_tb.append(item[1])
        src_col.append(item[2])

# print(pre_class_use_ml('T','','帐号'))
# print(pre_class_use_dl('T','客户资料表','姓名'))
# print(tiny_class_fr_db('','',''))
# union_2w()
# batch_tiny_class(r'E:\yang_xy_test\tiny_train\T01数据\test')
# test_()
# tb_name='Db_tgt'#每个属性对应一个表，表内有两列，第二列作为权重
# filepath=r"C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\总集\out_one_word用于输入数据库\one_word_tgt_sum_vocab.csv"
# init(tb_name)
# put_in(r'E:\兴业银行\中文翻译英文最终数据集\合并产生字典库\from_tb_trans.csv','zh_en_0')
#先执行samp_tb()从样本表制作输入数据，create_model后生成模型,再执行do_class 可以进行输入的分类
# import time
# tm=time.strftime('%Y-%m-%d',time.localtime(time.time()))
# model_path = r'E:\yang_xy_test\ten class\model'+'\\'+tm+'_model.pkl'
model_path = r'E:\yang_xy_test\ten class\model\05-24_seperate_model.pkl'
create_model(model_path)
input=['T','帐户登记表','帐号']

# do_class(input,model_path)
# get_rown()

# tiny_class_deal(r'E:\yang_xy_test\tiny_train\T99数据')#每次需要修改取源还是取目标,
# tf_idf(r'E:\yang_xy_test\tiny_train\T99数据\dataset')#每次修改目录就可以，目录下是两个csv文件
# union_2w()#融合源和目标产生的表，每次需要改表名
conn.close()