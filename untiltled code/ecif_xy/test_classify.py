#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier as Rfc
from sklearn.model_selection import cross_val_score as cro_scor
import pandas as pd
import csv
import os
from sklearn.utils import shuffle
import numpy as np
from pandas import DataFrame
from sklearn.externals import joblib
import operator
from functools import reduce
from sklearn.ensemble import GradientBoostingClassifier as Gbf
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import roc_auc_score as roc
from sklearn.metrics import confusion_matrix  #混淆矩阵需要输入预测和实际标签的类名称
from sklearn.externals import joblib
tr_set = r'C:\Users\XUEJW\Desktop\yang_test\data_set\tensor_input_train_set.csv'
test_file = r'C:\Users\XUEJW\Desktop\yang_test\data_set\tensor_input_test_set.csv'
def add_label(tr_set,test_file):
    from sklearn.preprocessing import LabelEncoder as Le
    train_data = pd.read_csv(tr_set, header=None)
    test_data = pd.read_csv(test_file, header=None)
    shuf_data = shuffle(train_data)
    tr_x = shuf_data.iloc[:, :-1].values
    train_y_ = shuf_data.iloc[:, -1:].values
    train_y=pd.Series(train_y_)
    uni=train_y.unique
    print('te:',uni,type(uni),type(train_y_))
def get_data_onelabel(tr_set):
    train_data = pd.read_csv(tr_set, header=None)
    shuf_data = shuffle(train_data)

    _x = shuf_data.iloc[:, :-1].values
    _y = shuf_data.iloc[:, -1:].values  # 列表中列表 numpy.ndarray
    lt_x = len(train_data) * 0.1
    put_lt = int(lt_x)
    if put_lt == 0:
        put_lt = 1
    print('lth:', len(train_data), put_lt)
    out_tr = shuf_data[:-put_lt].values
    out_te=shuf_data[-put_lt:].values
    tr_x = _x[:-put_lt]
    tr_y = _y[:-put_lt]
    te_x = _x[-put_lt:]
    te_y = _y[-put_lt:]
    return tr_x, tr_y, te_x, te_y,out_tr,out_te
def sum_test(te_set,num):#针对get_dat_batch
    te_data = pd.read_csv(te_set, header=None)
    rownum=-1*num
    _x = te_data.iloc[:, :rownum].values
    _y = te_data.iloc[:, rownum:].values
    return _x,_y
def get_data(tr_set):#如果不是onehot 而是onelable则是-1
    train_data = pd.read_csv(tr_set,header=None)
    shuf_data=shuffle(train_data)
    _x = shuf_data.iloc[:, :-573].values
    _y =shuf_data.iloc[:, -573:].values#列表中列表 numpy.ndarray
    lt_x=len(train_data)*0.1
    put_lt=int(lt_x)
    if put_lt==0:
        put_lt=1
    print('lth:',len(train_data),put_lt)
    tr_x=_x[:-put_lt]
    tr_y=_y[:-put_lt]
    te_x=_x[-put_lt:]
    te_y=_y[-put_lt:]
    return tr_x,tr_y,te_x,te_y
def get_data_batch(tr_set,num):#get one label from  many files已分好训练及测试集
    from pandas import DataFrame
    rootdir = tr_set
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data=[]
    print(num)
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        # print(path)
        if os.path.isfile(path):
            train_data = pd.read_csv(path, header=None)
            # print('0:',len(train_data))
            if len(data)==0:
                data=train_data
            else:
                data=np.append(data,train_data,axis=0)#按行叠加
                # print('2:',len(data))
    sdata=DataFrame(data)
    shuf_data = shuffle(sdata)
    rownum=-1*num
    # print('3:',len(data),type(data),len(sdata),type(sdata))
    _x = shuf_data.iloc[:, :rownum].values
    _y = shuf_data.iloc[:, rownum:].values  # 列表中列表 numpy.ndarray
    tr_x = _x
    tr_y = _y

    return tr_x, tr_y
def Cart_tree():
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()#决策树对不均衡比较敏感，会偏向大类
    return clf
def Grboost():
    from sklearn.ensemble import GradientBoostingClassifier as Gbf
    clf=Gbf(random_state=10)
    return clf
def Rf():
    from sklearn.ensemble import RandomForestClassifier as Rfc
    # clf=Rfc(random_state=0,n_estimators=80,min_samples_leaf=1,oob_score=True)#oob_score=True是个小型的交叉验证train score is 0.9847554666482721,test score is 0.9080459770114943
    clf=Rfc(random_state=1)
    return clf
# clf=Cart_tree()
def Svm():
    from sklearn.svm import SVC
    clf=SVC()
    return clf
def search_best(x,y,para,model):
    from sklearn.model_selection import GridSearchCV
    clf=GridSearchCV(model,para)
    clf.fit(x,y)
    print('ss:',clf.best_params_)
    print('ss2:',clf.score(x,y))
def lower_dim(tr_x):
    from sklearn.decomposition import PCA
    pca = PCA(n_components='mle',svd_solver='full')
    print(len(tr_x))
    pca.fit(tr_x)
    print(pca.explained_variance_ratio_)
    print(pca.explained_variance_)
    print(pca.n_components_)
def find_label(pre_out):
    model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\model_input.csv'
    csvFile2 = open(model_path, "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)
    suml=[]
    out_str=[]
    ind_list = []
    for item in pre_out:
        ind = np.where(item == 1)
        ind_list.append(ind)  # ind_list[0] is a tuple ,ind_list is a list of tuple which is  a np.array
    #xp = ind_list[0][0].tolist()  # xp is a list of index

    for xx in reader2:
        if xx:
            suml.append(xx)
    tgt=suml[3]
    for id in ind_list:
        temp_id=id[0].tolist()
        for xx_id in temp_id:
            out_str.append(tgt[xx_id])
    csvFile2.close()
    return out_str
def batch_test(fpath):
    import os
    rootdir = fpath
    clf = Rf()
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        if os.path.isfile(path):
            tr_x, tr_y, te_x, te_y = get_data(path)
            clf.fit(tr_x, tr_y)
            # pre_out=clf.predict(te_x[:1])
            # pre_list=find_label(pre_out)
            # for xp in pre_list:
            #     print(xp)
            print('file name is {2},tr_score is {0},te_score is {1}'.format(clf.score(tr_x, tr_y), clf.score(te_x, te_y),lists[i]))
def batch_test_one_label(fpath):
    import os
    rootdir = fpath
    clf = Rf()
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path1 = os.path.join(rootdir, 'train_' + lists[i])
        new_path2 = os.path.join(rootdir, 'test_' + lists[i])
        if os.path.isfile(path):
            tr_x, tr_y, te_x, te_y,out_tr,out_te = get_data_onelabel(path)
            tr_csvFile= open(new_path1, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            tr_writer = csv.writer(tr_csvFile)
            te_csvFile = open(new_path2, 'w', newline='',
                              encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            te_writer = csv.writer(te_csvFile)
            for xx in out_tr:
                tr_writer.writerow(xx)
            for xy in out_te:
                te_writer.writerow(xy)
            # clf.fit(tr_x, tr_y.ravel())
            te_csvFile.close()
            tr_csvFile.close()
            # pre_out=clf.predict(te_x[:1])
            # pre_list=find_label(pre_out)
            # for xp in pre_list:
            #     print(xp)
            # print(
            #     'file name is {2},tr_score is {0},te_score is {1}'.format(clf.score(tr_x, tr_y), clf.score(te_x, te_y),lists[i]))
def get_model(path):
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    suml=[]
    for xx in reader:
        if len(xx)>0:
            for x in xx:
                if x.strip() not in suml:
                    suml.append(x.strip())

    csvFile.close()
    return suml
def new_find_label(pre_out,file_path):

    model_path = os.path.join(file_path, 'label model\\tgt_tb.csv')
    tgt =get_model(model_path)

    out_str = []
    ind_list = []
    for item in pre_out:
        ind = np.where(item == 1)
        ind_list.append(ind)  # ind_list[0] is a tuple ,ind_list is a list of tuple which is  a np.array
    # xp = ind_list[0][0].tolist()  # xp is a list of index

    for id in ind_list:
        temp_id = id[0].tolist()
        for xx_id in temp_id:
            out_str.append(tgt[xx_id])
    return out_str
def get_csv_lines(path):
    csvFile2 = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile2)

    lines = 0
    for item in reader:  # 读取每一行
        lines += 1
    line = lines  # 保存行数
    csvFile2.close()
    return line
def find_ten_class(pre_out):

    label_name = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T99', 'REF']

    for item in pre_out:
        ind = np.where(item == 1)

    id=ind[0].tolist()
    if len(id)>0:
        # print(label_name[id[0]])
        print('xx:',id,len(ind))
        result=label_name[id[0]]

    else:
        result='no'
        print('ind:',ind)
        # print('no class')
    return result
def new_batch_test_one_label(file_path,tgt_lh=None):#sum all and test seperate ,one label
    te_path=os.path.join(file_path,'te')
    tr_path=os.path.join(file_path,'tr')
    model_path=os.path.join(file_path,'model\\pca_union_model.pkl')

    if tgt_lh==None:
        label_ = os.path.join(file_path, 'label model\\tgt_tb.csv')
        line = get_csv_lines(label_)
    else:
        line=tgt_lh
    rootdir = te_path
    # print('te:',model_path)
    # model_p = r'E:\yang_xy_test\ten class\model\_model.pkl'
    # clf = joblib.load(model_p)

    clf = Rf()
    tr_x, tr_y = get_data_batch(tr_path,line)
    print('train length:',len(tr_y),len(tr_x[0]),len(tr_y[0]))
    clf.fit(tr_x, tr_y)#one hot 不用.ravel()

    # print('tr_score is {0}'.format(clf.score(tr_x, tr_y)))
    lists = os.listdir( te_path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])

        if os.path.isfile(path):
            te_x, te_y =  sum_test(path,line)
            pred = clf.predict(te_x)

            for x in range(len(pred)):
                pre_y = find_ten_class([pred[x]])  # 该函数需要输入列表中列表
                y_true = find_ten_class([te_y[x]])
                print('file is {2},y_true is {0},pre_y is {1}'.format(y_true, pre_y,lists[i]))
                print('yang:',pred[x],te_y[x])
            # print('00:',len(te_x[0]),len(te_x))
            # pro=clf.predict_proba(te_x)
            # print('0:',len(te_y[0]),len(te_y))
            # print('1:',type(pro))
            # pred=clf.predict(te_x)
            # print('y_t:',te_y[0])
            # pp=clf.predict_proba([te_x[0]])
            # print('xx:',te_y[0])
            # print('pp:',pp,type(pp))
            # print('3:', len(pred),len(pp))
            # for x in range(len(pred)):
            #     pre_y=new_find_label([pred[x]],file_path)#该函数需要输入列表中列表
            #     y_true=new_find_label([te_y[x]],file_path)
            #     print('y_true is {0},pre_y is {1}'.format(y_true,pre_y))
            #     print(pred[x])
            # print('file name is {1},te_score is {0}'.format(clf.score(te_x, te_y),lists[i]))

    joblib.dump(clf, model_path)

# clf=Rf()
# clf=Grboost()#要每个类做成一个分类器
# rain score is 0.5691114245416079,test score is 0.46
# batch_test(r'C:\Users\XUEJW\Desktop\yang_test\input data')#表名被拆开的数据
# batch_test_one_label(r'C:\Users\XUEJW\Desktop\yang_test\input data')#表名被拆开的数据且标签是一维的
# new_batch_test_one_label(r'E:\yang_xy_test\ten class',13)
# batch_test(r'C:\Users\XUEJW\Desktop\yang_test\tiny_train')#表名没被拆开的数据
model_path=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\yang_Rf_tinyclass_model.pkl'
# clf= joblib.load(model_path)
# tr_x,tr_y,te_x,te_y=get_data(r'C:\Users\XUEJW\Desktop\yang_test\one_label_input_train sum.csv')
# lower_dim(tr_x)# print('data:',type(tr_x))
para_0={'n_estimators':range(10,100,10)}#80
para_1= {'max_depth':range(80,120,10)}#
para_2={'min_samples_leaf':range(1,12,1)}#1  0.984755466648
# search_best(tr_x,tr_y,para_2,clf)
#clf.fit(tr_x,tr_y.ravel())#如果是onelabel则是ravel()变成(n_sample,1),如果onehot则不用
# clf.fit(tr_x,tr_y_svc)#svc的输入标签是一维,未成功,Rf可以接收独热码形式的标签,boost也不能
# print('0:',te_y_svc.shape)
# y_true=[]
# y_pre=[]
#
# for x in te_y_svc:
#     y_true.append(x[0])
#
# # pre_out2=clf.predict(te_x[:10])#返回列表中列表
# pre_out=clf.predict(te_x)#返回是列表中列表 n_sample*独热码
# # print('0:',type(pre_out2),type(te_y))
# for item in pre_out:
#     ind=np.where(item==1)
#
#     y_pre.append(ind[0])#ind[0]是个nuy.ndarray 要.tolist（）但是同时空集又会自动跳过
# print('3:',len(y_pre),type(y_pre),len(y_true),type(y_true))
# for x in range(len(y_true)):
#     print('{}:{}-->{},{}'.format(x,y_true[x],y_pre[x],type(y_pre[x])))
# print('3:',len(y_pre),type(y_pre),len(y_true),type(y_true))
# clf.score(te_x,te_y)Returns the mean accuracy on the given test data and labels.
#roc_auc报错only one class 是因为该方法需要多个标签样本，而数据集中并没有
# print('train score is {0},test score is {1}'.format(clf.score(tr_x,tr_y_svc)),clf.score(te_x,te_y_svc))
# print('train score is {0},test score is {1}'.format(clf.score(tr_x,tr_y),clf.score(te_x,te_y)))#一般得分
# model_path=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\classify model\yang_boost_model.pkl'#pickle.dumps(clf)
# print(confusion_matrix(y_true, y_pre))
# joblib.dump(clf,model_path)
def create_dataset(file_path):#单独制作分类的测试集和训练集
    te_path=os.path.join(file_path,'te')
    tr_path=os.path.join(file_path,'tr')
    rootdir = tr_path

    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        fi_na=lists[i][-13:-10]
        path = os.path.join(rootdir, lists[i])
        new_path=os.path.join(rootdir, 'new_'+lists[i])
        # print('na:',fi_na,lists[i])
        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)
            csvFile1 = open(new_path, 'w', newline='',
                              encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer1 = csv.writer(csvFile1)
            for item in reader:  # 读取每一行
                if item:
                    data=item
                    data.append(fi_na)
                    # print('1:',data)
                    writer1.writerow(data)
            csvFile.close()
            csvFile1.close()
