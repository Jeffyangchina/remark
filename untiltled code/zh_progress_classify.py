#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import bson
import csv
import os
import argparse
import re
import jieba
from time import ctime
print('begin job:', ctime())
# from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import sys

# ps = PorterStemmer()
# ps = PorterStemmer()
import nltk.stem
ps=nltk.stem.SnowballStemmer('english')#other stem method
def get_lab_lth(alab):
    tmp=list(alab.split('.'))
    tmp=[x.strip() for x in tmp]
    tmp=rm_null(tmp)
    lth=len(tmp)
    return lth
def get_head_lab(lab,n):
    lab=lab.strip()
    nlab=list(lab.split('.'))
    nlab=[str(x.strip()) for x in nlab]
    nlab=rm_null(nlab)
    try:
        out='.'.join(nlab[:n])

    except:
        out='.'.join(nlab)
    return out
def rm_null(lis):
    out_li=[]
    for cel in lis:
        if len(cel)>0:
            out_li.append(cel)
    return out_li
def finalload_model(model_path,lb=0,wod=1):
    # new_path='./DB/new_lab_word.csv'
    csvFile = open(model_path, "r", encoding='UTF-8')
    reader= csv.reader(csvFile)
    labs = {}
    words = []

    for item in reader:
        if item:
            lab=item[lb].strip()
            wd=item[wod].strip()
            if lab not in labs:
                labs[lab]=[wd]
            else:
                labs[lab].append(wd)
    csvFile.close()
    return  labs
def load_vocab(model):
    csvFile = open(model, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs = {}
    words = []

    for item in reader:
        if item:
            lab = item[0].strip()
            wds = item[1:]
            wds=rm_null(wds)
            if lab not in labs:
                labs[lab] = wds
            else:
                labs[lab]+=wds
    csvFile.close()
    return labs
def define_en(astr):
    xw = wordnet.synsets(astr)  # 判断是否是英文
    if len(xw)>0:
        return astr
    else:
        return ''
def rm_duplicate(alist):
    out_data=[]
    for item in alist:
        if item.strip() not in out_data:
            out_data.append(item.strip())
    out_data=rm_null(out_data)
    return out_data
def stemed(astr):
    from nltk.corpus import stopwords
    import jieba
    alist=list(jieba.cut(astr))
    m=0
    alist = [get_en(w) for w in alist if w not in stopwords.words('english')]

    alist=[define_en(x) for x in alist]
    alist=rm_null(alist)

    alist=rm_duplicate(alist)
    alist=[ps.stem(w) for w in alist]
    alist = rm_null(alist)

    # outstr=' '.join(alist)
    return alist
def stemed_labKW(alist):

    import jieba
    outList=[]
    for val in alist:
        if ' ' in val:
            tval=list(val.split(' '))
            tmpList=[ps.stem(w) for w in tval]
            tmpStr=' '.join(tmpList)
            outList.append(tmpStr)
        else:
            outList.append(ps.stem(val))

    outList = rm_null(outList)

    # outstr=' '.join(alist)
    return outList
def stemed_str(val):
    tval=list(jieba.cut(val))
    tmpList = [x.strip() for x in tval]
    tmpList = [get_en(w) for w in tmpList if len(w) > 1]
    tmpList = rm_null(tmpList)
    tmpList = [ps.stem(w) for w in tmpList]
    tmpStr = ' '.join(tmpList)
    return tmpStr
def get_len(alab):
    alab=alab.strip()
    nlab=list(alab.split('.'))
    return len(nlab)
def check_lab_chain(alist,n=2):
    alist=sorted(alist,key=lambda x:len(x),reverse=True)
    n=int(min(get_len(alist[0])-1,n))
    if (get_len(alist[0])-get_len(alist[1]))==1:
        return True
    if (get_len(alist[0])-get_len(alist[1]))==2:
        return True
    if len(alist)>=(n+1):
        return True
    return False


def extract_lab(lab_list):#输入是相关的所有标签
    lab_list=rm_duplicate(lab_list)
    sortlist=sorted(lab_list,key=lambda x:len(x),reverse=True)
    wd_dic={}
    tmp_cell = []
    out_lab=[]
    for item in sortlist:
        if item not in tmp_cell:
            newlist=sortlist.copy()
            newlist.remove(item)
            for cell in newlist:
                if cell!=item:
                    if item.startswith(cell):
                        if item not in wd_dic:
                            wd_dic[item] = []
                        if cell not in tmp_cell:
                            tmp_cell.append(cell)
                        if cell not in wd_dic[item]:
                            wd_dic[item].append(cell)
    n=7
    for key in wd_dic:
        tmp=[key]+wd_dic[key]#一个链上的标签数组
        if check_lab_chain(tmp,n):
            if key not in out_lab:
                out_lab.append(key)
    out_=' '.join(out_lab)
    return out_
def refine_lab(alist):
    out=[]
    for val in alist:
        if alist.count(val)>1:
            out.append(val)
    return out
def predict_class(trwd,labs,words):
    temp_list=[]
    wd_dic={}
    t=0
    out_lab=[]
    train_word=list(trwd.split(' '))
    for i in range(len(words)):
        wd=words[i]
        lab=labs[i]
        if ' ' in wd:
            if wd in trwd:
                if lab not in out_lab:
                    out_lab.append(lab)
            tmp_wd=list(jieba.cut(wd))
            tmp_wd=[x for x in tmp_wd if x not in stopwords.words('english') and len(x)>1]
            tmp_wd=[x.strip() for x in tmp_wd]
            tmp_wd=rm_null(tmp_wd)
            for val in tmp_wd:
                if val in train_word and len(val)>1:
                    if lab not in out_lab:
                        out_lab.append(lab)
                    break
        else:
            if wd in train_word:
                if lab not in out_lab:
                    out_lab.append(lab)
    return out_lab
def predict_kw(kwlist,labs,words):
    temp_list = []
    wd_dic = {}
    t = 0
    out_lab = []
    train_word = ' '.join(kwlist)
    for i in range(len(words)):
        wd = words[i]
        lab = labs[i]
        if ' ' in wd:
            if wd in train_word:
                if lab not in out_lab:
                    out_lab.append(lab)
            tmp_wd = list(jieba.cut(wd))
            tmp_wd = [x for x in tmp_wd if x not in stopwords.words('english') and len(x) > 1]
            tmp_wd = [x.strip() for x in tmp_wd]
            tmp_wd = rm_null(tmp_wd)
            for val in tmp_wd:
                if val in train_word and len(val) > 1:
                    if lab not in out_lab:
                        out_lab.append(lab)
                    break
        else:
            if wd in kwlist:
                if lab not in out_lab:
                    out_lab.append(lab)
    return out_lab
def predict(train_word,labs,words,labKW):
    temp_list=[]
    wd_dic={}
    t=0
    train_word=stemed(train_word)
    labKW=stemed_labKW(labKW)
    wd_cnt={}
    tmp_wd={}
    WdLab={}
    for i in range(len(words)):
        wd=words[i]
        lab=labs[i]
        if wd not in WdLab:
            WdLab[wd]=[lab]
        else:
            if lab not in WdLab[wd]:
                WdLab[wd].append(lab)
        if wd not in tmp_wd:
            tmp_wd[wd]=[lab]
        else:
            if lab not in tmp_wd[wd]:
                tmp_wd[wd].append(lab)

        if wd in train_word:
            cnt=train_word.count(wd)
            wd_cnt[wd]=cnt
            if wd not in wd_dic:
                wd_dic[wd]=[lab]
            else:
                if lab not in wd_dic[wd]:
                    wd_dic[wd].append(lab)
            if lab not in temp_list:
                temp_list.append(lab)
    # out_lab=' '.join(temp_list)
    wd_list=sorted(wd_cnt.items(),key=lambda x:x[1],reverse=True)
    max_lth=wd_list[0][1]
    print('max fre:',wd_list[0])
    key_wd=[]#出现的高频词
    key_lab=[]#高频词相关的标签
    for val in wd_list:
        if val[1]>0.6*max_lth and val[1]>1:
            key_wd.append(val[0])
    # print('key:',key_wd)
    if len(key_wd)>0:
        for cell in key_wd:
            key_lab+=tmp_wd[cell]
    key_lab=[x for x in key_lab if len(x)<6]
    tmp_origLab=[]
    # print('lab:',len(key_lab))
    for val in labKW:#orign_label的词
        if val in WdLab:#词为键，相应标签为值
            tmp_origLab+=WdLab[val]#orign_label 相关的标签
    tmp_origLab=[x for x in tmp_origLab if len(x)<6]
    final_origLab=tmp_origLab
    # final_origLab=refine_lab(tmp_origLab)

    out_lab=extract_lab(temp_list)#从标签数组中提取有上级标签的标签
    out_lab_list=list(out_lab.split(' '))
    out_tmp=[]
    if len(key_lab)>0:
        for oll in out_lab_list:
            for tmpk in key_lab:
                if oll.startswith(tmpk):
                    out_tmp.append(oll)
                    break
    else:
        out_tmp=out_lab_list
    final_out=[]

    # print('orig:',final_origLab)
    if len(final_origLab)>0:
        for val in out_tmp:
            for cel in final_origLab:
                if val.startswith(cel):
                    final_out.append(val)
                    break
        out_lab=' '.join(final_out)
    else:
        out_lab = ' '.join(out_tmp)
    return out_lab
def get_en(astr):

    outstr = re.sub("[^a-zA-Z]", "", astr)
    outstr = outstr.strip().lower()
    return outstr
def clean_orin_data(astr):
    import string

    astr = astr.replace('\n', ' ')
    tr = re.sub("\[(.*)\]", "", astr)
    tr = re.sub("\((.*)\)", "", tr)
    for c in string.punctuation:
        tr = tr.replace(c, ' ')
    temp_list=list(jieba.cut(tr))
    temp_list=[get_en(x) for x in temp_list]

    temp_list=rm_duplicate(temp_list)
    temp_list = rm_null(temp_list)
    outstr=' '.join(temp_list)
    return outstr
def save_labs(labslist,newpath):
    csvFile1 = open(newpath, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer1 = csv.writer(csvFile1)
    for val in labslist:
        writer1.writerow([val])
    csvFile1.close()
def get_orin_data(dapth):#从参赛提供数据提取并初步清洗

    orign_mark=0
    desList=[]
    labsList=[]
    categ=[]
    with open(dapth, 'rb') as f:
        data = bson.decode_all(f.read())
        for item in data:
            pro_info = ''

            try:
                if item['description']:
                    temp_des=item['description']
                    temp_des=[temp_des[x] for x in temp_des if temp_des[x]]

                    for itd in temp_des:
                        itd=clean_orin_data(itd)
                        temp_itd=list(itd.split(' '))
                        temp_itd=rm_null(temp_itd)
                        des=' '.join(temp_itd)
                        des=clean_orin_data(des)
                else:
                    des=''
                    if item['short_description']:

                        temp_des=item['short_description']
                        temp_des = [temp_des[x] for x in temp_des if temp_des[x]]
                        st_des=' '.join(temp_des)
                        st_des=clean_orin_data(st_des)
                        des=st_des
            except:
                print('no description')
                des=''
            try:
                if item['origin_labels']:

                    temp_des=item['origin_labels']
                    temp_des=[clean_orin_data(x) for x in temp_des]
                    temp_des=rm_duplicate(temp_des)
                    temp_des=rm_null(temp_des)
                    orign_mark+=len(temp_des)#yang
                    temp_label=' # '.join(temp_des)
                    origin_label=temp_label

                else:
                    origin_label=''
            except:
                print('no origin label')
                origin_label = ''
            try:
                if item['products_services']:
                    pro_info=''
                    for xx in item['products_services']:
                        if len(xx['name'])>0:
                            pna=xx['name'].replace('\n',' ')
                            pro_info=pro_info+pna+' : '
                        if len(xx['description'])>0:
                            xdes=xx['description'].replace('\n',' ')
                            pro_info = pro_info +xdes+' / '
                    pro_info=clean_orin_data(pro_info)
            except:
                print('no product')
                pro_info = ''
            if len(des)>0 and len(pro_info)>0:
                temp=des+' '+pro_info
            else:
                temp=''
            # try:
            #     if item['categories']:
            #         label = ''
            #         for xx in item['categories']:
            #             if len(xx['category_no']) > 0:
            #                 label = label + ' ' + xx['category_no'] + ' '
            #         label_list = list(label.split(' '))
            #         label_list = rm_null(label_list)
            #         label_list = [x.strip() for x in label_list]
            #         out_label = ' '.join(label_list)
            #     else:
            #         out_label = ''
            # except:
            #     out_label=''
            # categ.append(out_label)
            desList.append(temp)
            labsList.append(origin_label)
    # savepath='./DB/origin_result.csv'
    # save_labs(categ,savepath)
    return desList,labsList
def list2list(alist):
    tmp=[]
    for val in alist:
        if val not in tmp:
            tmp.append(val)
            tval=list(val.split(' '))
            if len(tval)>1:
                for cel in tval:
                    if cel not in tmp:
                        tmp.append(cel)
    return tmp
def feature_define(vocabs,wdList):#根据模型内的词组，选择出文本中的相关词

    lth=len(vocabs)
    feature_wd=[]
    for val in vocabs:
        if val in wdList:
            if val not in feature_wd:
                feature_wd.append(val)
    return feature_wd
from classfity import countvec
def stem_list(alist):
    outlist=[]
    for val in alist:
        if ' ' in val:
            valist=list(val.split(' '))
            valist=[stemed_str(x) for x in valist]
            vstr=' '.join(valist)
            outlist.append(vstr)
        else:
            outlist.append(stemed_str(val))
    return outlist
def get_stem_data(inp,vocabs,lab=0,wd=1):

    csvFile = open(inp, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs=[]
    wds=[]
    keywds=[]
    for item in reader:
        if item:
            tmp_wd=item[wd:3]
            oglab=list(item[3].split('#'))
            oglab=[x.strip().lower() for x in oglab if len(x)>1]
            oglab=[stemed_str(x) for x in oglab]
            oglab=rm_null(oglab)
            tmp_wd=' '.join(tmp_wd)
            tmp_lab=item[lab].strip()
            tmp_wd=list(jieba.cut(tmp_wd))
            tmp_wd =[get_en(x) for x in tmp_wd]
            tmp_wd=[stemed_str(x) for x in tmp_wd]
            tmp_wd=[x.strip() for x in tmp_wd if len(x)>1]
            # feature_wd=feature_define(vocabs,tmp_wd)#用模型中的词选出文本中的
            input_wd=' '.join(tmp_wd)
            if len(input_wd)>0:
                feature_wd=countvec(input_wd)#output a list
            else:
                feature_wd=['']
            feature_wd=rm_null(feature_wd)
            key_wdlist=oglab#+feature_wd
            key_wd=' '.join(key_wdlist)
            wds.append(key_wd)
            labs.append(tmp_lab)
            keywds.append(key_wdlist)
    csvFile.close()
    return wds,labs,keywds
def count_nostem_vec(tmp_wd,vocabs):
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 4), stop_words='english')
    wds=[]
    cv_fit = cv.fit_transform([tmp_wd])
    gfn = cv.get_feature_names()  # 是词组合的数组，未词干化，词干化匹配然后返回未词干的词
    for val in gfn:
        tmp_val = stemed_str(val)
        if tmp_val in vocabs:
            if val not in wds:
                wds.append(val)
    return wds
def count_stem_vec(tmp_wd,vocabs):
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 5), stop_words='english')
    wds=[]
    cv_fit = cv.fit_transform([tmp_wd])
    gfn = cv.get_feature_names()  # 是词组合的数组，未词干化，词干化匹配然后返回未词干的词
    for val in gfn:
        if val in vocabs:
            if val not in wds and len(val)>1:
                wds.append(val)
    return wds
def cut_jieba(astr):
    tmp=list(jieba.cut(astr))
    tmp=[get_en(x) for x in tmp if len(x)>1]
    out=' '.join(tmp)
    return out.lower()
def get_stem_vocab_data(inp,vocabs,lab=0,wd=1):
    csvFile = open(inp, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs=[]
    wds=[]
    keywds=[]
    for item in reader:
        if item:
            tmp_orglab =[]
            tmp_wd=item[wd:3]
            tmp_wd=rm_null(tmp_wd)
            oglab=list(item[3].split('#'))
            oglab=[x.strip().lower() for x in oglab if len(x)>1]
            oglab=[cut_jieba(x) for x in oglab]
            oglab=[stemed_str(x) for x in oglab]
            oglab=rm_null(oglab)
            tmp_wd=' '.join(tmp_wd)
            tmp_lab=item[lab].strip()
            tmp_wd=list(jieba.cut(tmp_wd))
            tmp_wd =[get_en(x) for x in tmp_wd]
            tmp_wd=[stemed_str(x) for x in tmp_wd]
            tmp_wd=[x.strip().lower() for x in tmp_wd if len(x)>1]
            tmp_wd=' '.join(tmp_wd)
            #feature_wd=count_stem_vec(tmp_wd, vocabs)#用词的组合和词典匹配,返回的是数组
            # feature_wd=feature_define(vocabs,tmp_wd)#用模型中的词选出文本中的,不用高频词
            # feature_wd=rm_null(feature_wd)
            for val in oglab:
                if val not in tmp_orglab:
                    tmp_orglab.append(val)
                # tmp_val=list(jieba.cut(val))
                # tmp_val=[x for x in tmp_val if len(x)>1]
                # for cell in tmp_val:
                #     if cell not in tmp_orglab:
                #         tmp_orglab.append(cell)

            key_wdlist=tmp_orglab#+feature_wd
            key_wd=' '.join(key_wdlist)
            wds.append(key_wd)
            labs.append(tmp_lab)
            keywds.append(key_wdlist)
    csvFile.close()
    return wds,labs,keywds
def get_nostem_data(inp,vocabs,lab=0,wd=1):

    csvFile = open(inp, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs=[]
    wds=[]
    keywds=[]
    for item in reader:
        if item:
            tmp_wd=item[wd:3]
            oglab=list(item[3].split('#'))
            oglab=[x.strip().lower() for x in oglab if len(x)>1]
            # oglab=[stemed_str(x) for x in oglab]
            oglab=rm_null(oglab)
            tmp_wd=' '.join(tmp_wd)
            tmp_lab=item[lab].strip()
            tmp_wd=list(jieba.cut(tmp_wd))
            tmp_wd =[get_en(x) for x in tmp_wd]
            # tmp_wd=[stemed_str(x) for x in tmp_wd]
            tmp_wd=[x.strip() for x in tmp_wd if len(x)>1]
            # feature_wd=feature_define(vocabs,tmp_wd)#用模型中的词选出文本中的
            input_wd=' '.join(tmp_wd)
            if len(input_wd)>0:
                feature_wd=countvec(input_wd)#output a list
            else:
                feature_wd=['']
            feature_wd=rm_null(feature_wd)
            key_wdlist=oglab+feature_wd
            more_keyword=oglab
            key_wd=' '.join(more_keyword)
            wds.append(key_wd)
            labs.append(tmp_lab)
            keywds.append(key_wdlist)
    csvFile.close()
    return wds,labs,keywds
def out_num(astr):
    import re
    out=re.sub('[0-9]','',astr)
    out=out.strip().lower()
    return out
def get_nostem_vocab_data(inp,vocabs,lab=0,wd=1):
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 4), stop_words='english')
    union_vocab=r"./DB/jeff_testdata/union_vocab.csv"
    csvFile1 = open(union_vocab, "r", encoding='UTF-8')
    reader1 = csv.reader(csvFile1)
    vocab_list=[]
    vocab_dic={}
    for item in reader1:
        if item :
            vlab=item[0].strip()
            vwd=item[1:]
            vwd=rm_null(vwd)
            if vlab not in vocab_dic:
                vocab_dic[vlab]=vwd
            else:
                for xx in vwd:
                    if xx not in vocab_dic[vlab]:
                        vocab_dic[vlab].append(xx)
            for xx in vwd:
                if xx not in vocab_list:
                    vocab_list.append(xx)
    # print('jeff1:',vocab_list,vocab_dic)
    csvFile = open(inp, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs=[]
    wds=[]
    stem_wds=[]
    keywds=[]
    for item in reader:
        if item:
            wds = []
            stem_wds = []
            tmp_wd=item[wd:3]
            oglab=list(item[3].split('#'))
            oglab=[x.strip().lower() for x in oglab if len(x)>1]
            oglab=rm_null(oglab)
            tmp_wd=' '.join(tmp_wd)
            tmp_wd = list(jieba.cut(tmp_wd))
            tmp_wd=[x for x in tmp_wd if x not in stopwords.words('english') and len(x)>1]
            tmp_wd=[out_num(x) for x in tmp_wd]
            tmp_wd=rm_null(tmp_wd)
            # tmp_wd = [get_en(x) for x in tmp_wd]
            tmp_wd = ' '.join(tmp_wd)
            cv_fit = cv.fit_transform([tmp_wd])
            gfn = cv.get_feature_names()  # 是词组合的数组，未词干化，词干化匹配然后返回未词干的词
            # print('wds0:',wds)
            for val in gfn:
                tmp_val = stemed_str(val)
                if tmp_val in vocab_list and tmp_val not in stem_wds:
                    if val not in wds and len(val)>1:
                        # print('val:',val,type(tmp_val),len(tmp_val))
                        stem_wds.append(tmp_val)
                        wds.append(val)
            # print('jeff wds:',wds)
            keywds.append(oglab+wds)
    csvFile.close()
    return keywds,vocab_dic

def get_train_data(path):
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    tmp=[]
    tmp_lab=[]#orign_label
    for item in reader:
        if item:
            wods=item[:3]
            orig_=item[3].lower()
            orig_list=list(orig_.split('#'))
            # print('x:',orig_)
            orig_list=[x.strip() for x in orig_list]
            lab_keyword=list2list(orig_list)
            lab_keyword=[x for x in lab_keyword if x not in stopwords.words('english')]
            tmp_lab.append(lab_keyword)
            wd=' '.join(wods)
            tmp.append(wd.lower())
    csvFile.close()
    return tmp,tmp_lab
# from classfity import final_classify
def train_predict(path,outpath):
    model_path =  './DB/jeff_testdata/stemed_yang_Categories.csv'
    train = r'.\DB\jeff_testdata\stem_train.csv'#用于大类分类
    vocabpath =  r'.\DB\jeff_testdata\stem_train.csv'#用于大类分类
    labs, words=load_model(model_path)#获取模型数据用于细分类
    _,vocabs=load_model(vocabpath)
    # desList,labList=get_orin_data(path)
    desList,cpId,keywds=get_stem_data(path,vocabs)#获取测试数据的词干

    print('1:',len(desList),len(words))
    res_labs=[]
    csvFile3 = open(outpath, 'w', newline='', encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer3 = csv.writer(csvFile3)
    i=0
    lab_list=final_classify(train,desList)#根据大分类模型以及文章高频词先做大分类判断
    for i in range(len(desList)):
        self_lab=lab_list[i]
        # lab=predict(desList[i], labs, words,labKW[i])
        lab=predict_kw(keywds[i], labs, words)#根据文章高频词，匹配模型细分类
        # lab=predict_class(keywds[i], labs, words)#根据模型词汇，找到牵涉到的分类,是细分类
        # lab=predict_class(desList[i], labs, words)#根据模型词汇，找到牵涉到的分类,是细分类
        defined_lab=[]
        if len(self_lab)>0:
            for item in lab:
                for val in self_lab:
                    if item.startswith(val):
                        if item not in defined_lab:
                            defined_lab.append(item)
                            break
        if len(defined_lab)>0:
            labStr=extract_lab(defined_lab)
        else:
            labStr=''
        res_labs.append(labStr)


    print('check len:',len(cpId),len(res_labs))
    for xn in range(len(res_labs)):
        writer3.writerow([cpId[xn],lab_list[xn],res_labs[xn]])
        # writer3.writerow([lab_list[xn]])
    csvFile3.close()
def sep_sc(astr):
    ast=list(astr.split(':'))
    if len(ast)==2:
        return ast
    else:
        return []
        print('wrong')
def list2dic(alist):
    dic={}
    for item in alist:
        nit=sep_sc(item)
        if len(nit)>0:
            wd=nit[0]
            sc=nit[1]
            if wd not in dic:
                dic[wd]=sc
    return dic
def tf_score(astr,sc_path):
    csvFile = open(sc_path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    class_dic={}
    out_dic={}
    out_list=[]
    for item in reader:
        if item:
            clas=item[0]
            sc_list=item[1:]
            if clas not in class_dic:
                class_dic[clas]=[]
                for val in sc_list:
                    class_dic[clas].append(val)
    for key in class_dic:
        key_wd=class_dic[key]
        temp_dic=list2dic(key_wd)
        temp_sc=0.
        for xk in temp_dic:
            if xk in astr:
                temp_sc+=float(temp_dic[xk])
        out_dic[key]=temp_sc
    for od in out_dic:
        temp_out=str(od)+':'+str(out_dic[od])
        out_list.append(temp_out)
    csvFile.close()
    return out_list

def test(data_path,outpath,idlist):
    data_des=[]
    csvFile = open(data_path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    csvFile3 = open(outpath, 'w', newline='', encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer3 = csv.writer(csvFile3)
    for i, item in enumerate(reader):
        if i in idlist:
            print('i:',i)
            writer3.writerow(item)

    csvFile.close()
    csvFile3.close()
def temp(p1,outpath):
    csvFile1 = open(p1, "r", encoding='UTF-8')
    reader1 = csv.reader(csvFile1)
    csvFile3 = open(outpath, 'w', newline='', encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer3 = csv.writer(csvFile3)

    for item in reader1:
        if item:
            tmp=item[1]
            tmplist=list(jieba.cut(tmp))
            tmplist=[x.strip() for x in tmplist]
            tmplist=[stemed_str(x) for x in tmplist]
            tmplist=[x for x in tmplist if x not in stopwords.words('english')]
            tmplist=[x for x in tmplist if len(x)>2]
            tmpstr=' '.join(tmplist)

            writer3.writerow([get_head_lab(item[0].strip()),tmpstr])

    csvFile1.close()
    csvFile3.close()
def ger_vocab(reader):
    dic={}
    for item in reader:
        if item:
            lab=item[0]
            wd=item[1]
            if lab not in dic:
                dic[lab]=[wd]
            else:
                if lab not in dic[lab]:
                    dic[lab].append(wd)
    return dic
def ger_vocablist(path):
    csvFile1 = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile1)
    outlist=[]
    for item in reader:
        if item :
            wd=item[1].strip()
            if wd not in outlist:
                outlist.append(wd)
            wds=list(jieba.cut(wd))
            wds=[x.strip() for x in wds]
            wds=[get_en(x) for x in wds if len(x)>1]
            wds=rm_null(wds)
            for val in wds:
                if val not in outlist:
                    outlist.append(val)
    csvFile1.close()
    return outlist
def deal_raw(rawlist):
    data=' '.join(rawlist)
    data=list(jieba.cut(data))
    data=[get_en(x) for x in data]
    data=[stemed_str(x) for x in data]
    data=rm_null(data)
    data=' '.join(data)
    return data
def find_key_wds(vocabdic,datastr):
    dic={}

    for key in vocabdic:
        tmp=[]
        for val in vocabdic[key]:

            if val in datastr:
                if ' ' in val:
                    print('val:',val)
                temp=val+'-'+str(datastr.count(val))
                tmp.append(temp)
        dic[key]=tmp
    return dic
def most_wds(wdpth,inpth,outpth):
    csvFile1 = open(wdpth, "r", encoding='UTF-8')
    reader1 = csv.reader(csvFile1)
    csvFile = open(inpth, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    csvFile3 = open(outpth, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer3 = csv.writer(csvFile3)
    vocab_dic=ger_vocab(reader1)
    data=[]
    for item in reader:
        if item:
            lab=item[0].strip()
            wds=item[1:]
            wd_str=deal_raw(wds)
            keywd_dic=find_key_wds(vocab_dic,wd_str)
            writer3.writerow([lab,keywd_dic])


    csvFile.close()
    csvFile1.close()
    csvFile3.close()
# from similary_words import get_simi
def predict_wv(self_lab,kwlist,labs,words):#self_lab 一个样本对应分好的大类组，遍历这个组，每个大类作为键，值为相关细类

    temp_list = []
    wd_dic = {}
    t = 0
    refen_lab={}
    out_lab = []
    for val in self_lab:
        tmp_lab = []
        tmp_wd=[]
        if val not in refen_lab:
            refen_lab[val]=[]
            for i in range(len(words)):
                wd = words[i].strip().lower()
                lab = labs[i].strip()
                if lab.startswith(val) and lab!=val:
                    tmp_lab.append(lab)
                    tmp_wd.append(wd)
            for key in kwlist:
                for i in range(len(tmp_wd)):
                    tmp_sc=get_simi(key,tmp_wd[i])#获得两个词的相似度
                    if tmp_sc>0.6:
                        if tmp_lab[i] not in refen_lab[val]:
                            refen_lab[val].append(tmp_lab[i])
    for key in refen_lab:
        tmp_out=extract_lab(refen_lab[key])
        if len(tmp_out)>1:
            out_lab.append(tmp_out)

    union=' '.join(out_lab)

    return union
# from similary_words import get_smart_simi
def predict_wv_pkl(self_lab,kwlist,labs,words):#self_lab 一个样本对应分好的大类组，遍历这个组，每个大类作为键，值为相关细类

    temp_list = []
    wd_dic = {}
    t = 0
    refen_lab=[]
    refen_wd=[]
    out_lab = []
    for val in self_lab:
        tmp_lab = []
        tmp_wd=[]
        for i in range(len(labs)):
            if labs[i].startswith(val):
                refen_lab.append(labs[i])
                refen_wd.append(words[i])
    if len(refen_wd)>0:
        for key in kwlist:
            lab_id=get_smart_simi(key,refen_wd)
            for cel in lab_id:
                tmp_cel=refen_lab[cel]
                if tmp_cel not in out_lab:
                    out_lab.append(tmp_cel)

    union=' '.join(out_lab)

    return union


def check_wd(kwlist,vc):
    for item in kwlist:
        tmp=stemed_str(item)
        if tmp in vc:
            return True
    return False



def load_stem_wd(pth):
    csvFile = open(pth, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs = {}
    words = []
    for item in reader:
        if item:
            wd = item[1].strip()
            if wd not in words:
                words.append(wd)
    csvFile.close()
    return words
def get_wd_fr_data(path,vblist):
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs = []
    wds = []
    keywds = []
    for item in reader:
        if item:
            tmp_orglab = []
            tmp_wd = item[1:3]
            # print('11:', tmp_wd)
            tmp_wd = rm_null(tmp_wd)
            oglab = list(item[3].split('#'))
            oglab = [x.strip().lower() for x in oglab if len(x) > 1]
            oglab = [cut_jieba(x) for x in oglab]
            oglab = [stemed_str(x) for x in oglab if len(x)>1]
            oglab = rm_null(oglab)

            tmp_lab = item[0].strip()
            tmp_wd=' '.join(tmp_wd)
            tmp_wd = list(jieba.cut(tmp_wd))
            tmp_wd = [out_num(x) for x in tmp_wd if len(x)>1]
            tmp_wd = [stemed_str(x) for x in tmp_wd]
            tmp_wd = [x.strip().lower() for x in tmp_wd if len(x) > 1]
            tmp_wd = rm_null(tmp_wd)
            tmp_wd = ' '.join(tmp_wd)
            if len(tmp_wd)>1:
                feature_wd = count_stem_vec(tmp_wd,vblist)  # 用词的组合和词典匹配,返回的是数组
                feature_wd=rm_null(feature_wd)
            else:
                feature_wd=[]


            for val in oglab:
                if val not in tmp_orglab and val in vblist:
                    tmp_orglab.append(val)

            key_wdlist = tmp_orglab +feature_wd
            key_wd = ' '.join(key_wdlist)
            wds.append(key_wd)
            labs.append(tmp_lab)
            keywds.append(key_wdlist)

    csvFile.close()
    return wds, labs, keywds
def clean_dbstr(astr):
    oglab = list(astr.split('#yang#'))
    oglab = [x.strip().upper() for x in oglab if len(x) > 0]
    # oglab = [cut_jieba(x) for x in oglab]#数据已经分好词 无需再
    # oglab = [stemed_str(x) for x in oglab if len(x) > 1]
    # kptmp=[]
    # for val in oglab:
    #     tmp = []
    #     vls=list(val.split(' '))
    #     for cell in vls:
    #         if len(cell)>1:
    #             tmp.append(cell)
    #     kptmp.append(tmp)

    outlist = rm_null(oglab)
    return outlist
def check_list(al,vbl):
    out=[]
    tmp=list(al.split(' '))
    for key in tmp:
        if key in vbl and len (key)>0:
            out.append(key)
    outstr=' '.join(out)
    return outstr

def new_get_wd_fr_data(path,vblist):
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs = []
    wds = []
    keywds = []
    orglist=[]
    feature_wd=[]
    product=[]
    for item in reader:
        if item:
            tmp_orglab = []
            feature_wd = []
            tmp_wd = [item[1]]
            tmp_pro=item[2]
            # print('11:', tmp_wd)
            tmp_wd = rm_null(tmp_wd)
            oglab = list(item[3].split('#'))
            oglab = [x.strip().lower() for x in oglab if len(x) > 1]
            oglab = [cut_jieba(x) for x in oglab]
            oglab = [stemed_str(x) for x in oglab if len(x)>1]
            oglab = rm_null(oglab)

            tmp_lab = item[0].strip()
            tmp_wd=' '.join(tmp_wd)
            tmp_wd = list(jieba.cut(tmp_wd))
            tmp_wd = [out_num(x) for x in tmp_wd if len(x)>1]
            tmp_wd = [stemed_str(x) for x in tmp_wd]
            tmp_wd = [x.strip().lower() for x in tmp_wd if len(x) > 1]
            tmp_wd = rm_null(tmp_wd)


            tmp_pro=list(jieba.cut(tmp_pro))
            tmp_pro = [out_num(x) for x in tmp_pro if len(x) > 1]
            tmp_pro = [stemed_str(x) for x in tmp_pro]
            tmp_pro = [x.strip().lower() for x in tmp_pro if len(x) > 1]
            tmp_pro = rm_null(tmp_pro)
            # tmp_wd = ' '.join(tmp_wd)
            # if len(tmp_wd)>1:
            #     feature_wd = count_stem_vec(tmp_wd,vblist)  # 用词的组合和词典匹配,返回的是数组
            #     feature_wd=rm_null(feature_wd)
            # else:
            #     feature_wd=[]
            prolist=[]
            for key in tmp_wd:
                if key in vblist and len(key)>0 and key not in feature_wd:
                    feature_wd.append(key)
            for key in tmp_pro:
                if key in vblist and len(key)>0 and key not in prolist:
                    prolist.append(key)

            for val in oglab:
                if val not in tmp_orglab and val in vblist and len(val)>0:
                    tmp_orglab.append(val)

            key_wdlist = feature_wd
            orglist.append(tmp_orglab)#原始标签
            product.append(prolist)#产品描述
            key_wd = ' '.join(key_wdlist)
            wds.append(key_wd)
            labs.append(tmp_lab)
            keywds.append(key_wdlist)#公司描述

    csvFile.close()
    return wds, labs, keywds,orglist,product
def check_lth(alist):
    alist = rm_duplicate(alist)
    alist = rm_null(alist)
    alist = sorted(alist, key=lambda x: len(x), reverse=True)
    top_lab=alist[0]

    tmp_lth=get_lab_lth(top_lab)
    # print('cehcklth:', top_lab,tmp_lth,alist)
    if len(alist) == tmp_lth:
        return True
    uplay=get_head_lab(top_lab,tmp_lth-1)#找到上两层
    udlay=get_head_lab(top_lab,tmp_lth-2)
    toplay=get_head_lab(top_lab,1)
    seclay=get_head_lab(top_lab,2)
    # print('cj:',toplay,seclay)
    if uplay in alist and udlay in alist and toplay in alist and seclay in alist:
        return True
    # if tmp_lth<4:
    #     if len(alist)==tmp_lth:
    #         return True
    # else:
    #     top=get_head_lab(top_lab,1)
    #     sec=get_head_lab(top_lab,2)
    #     thd=get_head_lab(top_lab,3)
    #     if top in alist:
    #         if sec in alist or thd in alist:
    #             return True
    # alist=rm_duplicate(alist)
    # alist=rm_null(alist)
    # alist = sorted(alist, key=lambda x: len(x), reverse=True)
    # lth=len(list(alist[0].split('.')))
    # if lth==len(alist):
    #     return True
    return False
def check_lab_in(lab,alist):
    for val in alist:
        if val.startswith(lab) and len(val)>0:
            return True
    return False
def check_lab(lablist):#判断标签合集中，是否有包含最上三层
    lablist=[x.strip() for x in lablist]
    lablist=rm_null(lablist)
    lablist= sorted(lablist, key=lambda x: len(x), reverse=True)
    labdic={}
    tmp = lablist.copy()
    rout=[]

    for val in lablist:
        tmp.remove(val)
        if val not in labdic:
            labdic[val]=[]

        for cell in tmp:
            if val.startswith(cell) and len(cell)>0 and cell not in labdic[val]:
                labdic[val].append(cell)#每个标签一个集合，然后再去单独判断。
    for key in labdic:
        tmpl=[key]+labdic[key]
        if check_lth(tmpl):
            # print('checklab:',tmpl)
            if not check_lab_in(key,rout):

                rout.append(key)
                # print('chec00:', rout)

    # print('chec2:',rout )
    return rout
def check_others(labs,labset):
    outlist=[]
    for val in labs:
        # print('checkout:',outlist)
        tmp=val+'.0'
        if tmp in labset:
            if len(labs)==1 and (val=='13'):
                outlist.append(tmp)
            else:
                if val!='13':
                    outlist.append(tmp)
        else:
            outlist.append(val)
    # if '13' in outlist and len(outlist)!=1:
    #     outlist.remove('13')
    return outlist


def all_labs(path):
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs=[]
    for item in reader:
        if item:
            wd = item[0].strip()
            wds=list(wd.split('.'))
            wds=[str(x.strip()) for x in wds]
            wds=rm_null(wds)
            out='.'.join(wds)
            labs.append(out)
    csvFile.close()
    return labs


def task_out(outp,relab):

    csvFile2 = open(outp, 'w', newline='',
                    encoding='UTF-8')
    writer = csv.writer(csvFile2)
    for val in relab:
        tmp=list(val)
        if len(tmp[1])>0:
            writer.writerow(tmp)

    csvFile2.close()
def layer_one_classify(wdlist):
    from classfity import onehot_classify
    from classfity import use_model
    rootdir = r'.\DB\jeff_testdata\new_layer_model\first\1_layer_stemed.csv'
    labList = []
    finalist = []
    if len(wdlist) > 0:
        # tmpList = use_model(rootdir, wdlist)
        tmpList = onehot_classify(rootdir, wdlist)
        for val in tmpList:
            labList += val
        labList = rm_duplicate(labList)
        for cell in labList:
            if len(cell) > 0 and cell not in finalist:
                finalist.append(cell)

    return finalist
def newlayer_classify(prolist,idstr,first,wdlist,labset):
    from classfity import onehot_classify
    from classfity import use_model
    rootdir=r'.\DB\jeff_testdata\new_layer_model'
    lists = os.listdir(rootdir)
    labList=[]
    finalist=[]
    if len(first)>0:
        firstlab=layer_one_classify(first)
    else:
        if len(wdlist)>0:
            firstlab = layer_one_classify(wdlist)
        else:
            if len(prolist)>0:
                firstlab=layer_one_classify(prolist)


    wdlist=wdlist+first
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        if os.path.isfile(path):
            if len(wdlist)>0:
                tmpList=onehot_classify(path,wdlist)
                # tmpList=use_model(path,wdlist)
                for val in tmpList:
                    labList+=val
            if len(prolist)>0:
                proList=onehot_classify(path,prolist)
                # proList=use_model(path,prolist)
                for val in proList:
                    labList+=val
            labList=rm_duplicate(labList)
                # for cell in labList:
                #     if len(cell)>0 and cell not in finalist:
                #         finalist.append(cell)
    # print('final:',finalist)
    finalist=labList+firstlab
    outlist=check_lab(finalist)
    finallist=check_others(outlist,labset)
    # print('nextfinal:',outlist)
    outstr=' '.join(finallist)
    return (idstr,outstr)
def simple_load(pth):
    csvFile = open(pth, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    labs = {}
    words = []
    for item in reader:
        if item:
            wd = item[0].strip()

            val=list(wd.split(' '))
            for xx in val:
                if xx not in words and len(xx)>0:
                    words.append(xx)
    csvFile.close()
    return words

def coll_tilab(uplab,wds,tflabs,n):
    remark=[]
    for key in tflabs:
        if key.startswith(uplab) and 0<(len(key)-len(uplab))<(2*n+1):
            for cell in wds:
                if cell in tflabs[key] and key not in remark:
                    remark.append(key)
    return remark
def mini_tilab(wds,labs,tflabs):
    tmp=[]
    out=[]

    for val in labs:
        exlab = []
        if val.endswith('.0'):
            headlab = get_head_lab(val, -1)
        # else:
        #     headlab=val
            exlab=coll_tilab(headlab,wds,tflabs,2)
        # if len(exlab)==0:
        #     exlab=coll_tilab(headlab,wds,tflabs,2)
        if len(exlab) == 0:
            out.append(val)
        else:
            out+=exlab
    return out
def left_layer(exlist,n):
    out=[]
    for val in exlist:
        tmp=get_lab_lth(val)
        if tmp>4:
            if val.startswith('2.') or val.startswith('11.'):
                tmp_val = get_head_lab(val, 4)
            else:
                tmp_val=get_head_lab(val,n)
            if tmp_val not in out:
                out.append(tmp_val)
        else:
            out.append(val)
    out=[x.replace('.0','') for x in out]
    return out

def company_classify(orglist,orgstr,idstr,kwList,labset,tflabs):
    from classfity import use_model
    from classfity import onehot_classify
    rootdir = r'.\DB\jeff_testdata\classify for zh\new_layer_model'
    lists = os.listdir(rootdir)
    labList = []
    finalist = []
    tmplab=[]
    wdlist = rm_null(kwList)
    # print('11:',orgstr,orglist)
    tmplab+=layer_one_classify([orgstr])
    # print('12:', tmplab)
    tmplab+=layer_one_classify(orglist)
    # print('13:', tmplab)
    tmplab=rm_duplicate(tmplab)
    # if len(tmplab)==0 or ('13' in tmplab and len(tmplab)==1):
    #     tmplab += layer_one_classify(wdlist)

    # print('wlist:',wdlist,tmplab)
    # wdlist=wdlist+['energi power wind project develop']
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        if os.path.isfile(path):

            # print('patj0:',wdlist)
            tmpList = onehot_classify(path, wdlist)
            # tmpList = use_model(path, wdlist)
            # print('patj:',wdlist,tmpList)
            for val in tmpList:
                labList += val
            # if len(orgstr) > 0:
            #     tmpList = use_model(path,[orgstr])
            #     # print('org2:', orgstr,tmpList)
            #     for val in tmpList:
            #
            #         labList += val

            labList = rm_duplicate(labList)

    finalist = labList+tmplab
    finalist=rm_duplicate(finalist)
    # print('final0:',idstr,finalist)
    outlist = check_lab(finalist)
    # print('fianl1:',idstr,outlist)
    tmp_exlist = check_others(outlist, labset)
    # print('fianl11:',tmp_exlist)
    exlist=mini_tilab(wdlist,tmp_exlist,tflabs)#如果有.0的分类则看看有没有下级的
    # print('nextfinal:',idstr,exlist)
    exlist=left_layer(exlist,3)
    outstr = ' '.join(exlist)
    return (idstr, outstr)




def tfidf_labs(tfidf_path):
    csvFile = open(tfidf_path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    tf_labs = {}
    for item in reader:
        if item:
            lab = item[0].strip()
            wds = item[1:]
            wds = [x.strip() for x in wds]
            wds = rm_null(wds)
            if lab not in tf_labs:
                tf_labs[lab]=wds
            else:
                tf_labs[lab]+=wds
                tf_labs[lab]=rm_duplicate(tf_labs[lab])
    csvFile.close()
    return tf_labs


def sepr_company_data(path, vblist, all_labList, tf_labs):
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)

    keywds = []
    outid = []
    orglab = []
    feature_wd = []
    orglablist = []
    result_lab = []
    for item in reader:
        if item:
            out_lab = []
            feature_wd = []
            idstr = item[0].strip()  # 公司id
            tmp = item[1:4]  # 公司特征
            for val in tmp:
                if len(val) > 0:
                    feature_wd += (clean_dbstr(val))  # 每个公司特征作为一个字符串组成一个数组
            # print('fea0:', feature_wd)
            oglab = item[4].strip()  # 原始标签项
            oglist = clean_dbstr(oglab)  # 原始标签项，a list
            prolist = []
            allinfo = oglist + feature_wd  # 所有特征的数组，其中原始标签是分开每个成一元素，描述则是一个描述成一字符串元素
            allinfo = rm_null(allinfo)
            # print('info0:', allinfo)

            orglabStr = ' '.join(oglist)  # 原始标签合并项
            # print('org1:', orglabStr, oglist)

            for tkey in allinfo:
                tmpkl = check_list(tkey, vblist)
                if len(tmpkl) > 0:
                    prolist.append(tmpkl)  # 是过滤单词后的allinfo
            # print('info1:', prolist)

            if len(prolist) > 0:

                out_lab = company_classify( oglist, orglabStr,idstr, prolist, all_labList, tf_labs)

                # print('out_lab:', out_lab)
                if len(out_lab[1]) > 0:
                    result_lab.append(out_lab)

    csvFile.close()
    return result_lab
if __name__ == '__main__':
    maxInt = sys.maxsize
    decrement = True

    while decrement:
        # decrease the maxInt value by factor 10
        # as long as the OverflowError occurs.

        decrement = False
        try:
            csv.field_size_limit(maxInt)
        except OverflowError:
            maxInt = int(maxInt / 10)
            decrement = True
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--test", type=str, default='./DB/company.bson', help="input data to classify")
    parser.add_argument("-r", "--result", type=str, default='./DB/result.csv', help="output data of classification")

    args = parser.parse_args()
    # path='./DB/manul_origin_dataset.csv'
    path=args.test
    outpath=args.result
    sc_path=r'C:\Users\XUEJW\PycharmProjects\untitled1\DB\7_layers\zhou class\model\first\tfidf\tfIdf_first_union_stemed.csv'
    data_path = r"./DB/test dataset/test final/test_dataset_bymyself.csv"
    outpath= r"./DB/test dataset/test final/temp_test.csv"

    model_path=r'C:\Users\XUEJW\PycharmProjects\untitled1\DB\zhou_class\yang_Categories02.csv'
    new_path=r"./DB/test dataset/test final/new_dataset_classify.csv"
    p1=r"./DB/test dataset/test final/final_test_lab.csv"
    p2=r"./DB/test dataset/test final/temp_test.csv"
    p1=r"./DB/yang_class/manul_data/yang_class_vocab.csv"
    outpth=r"./DB/yang_class/manul_data/stem_yang_class_vocab.csv"
    # temp(p1,outpth)
    wdpth=r"./DB/yang_class/manul_data/stem_yang_class_vocab.csv"
    inpth= r"./DB/jeff_testdata/new_test_dataset_bymyself.csv"#
    outpth=r"./DB/yang_class/manul_data/test_data_keywd.csv"
    # most_wds(wdpth, inpth, outpth)
    train = r'C:\Users\XUEJW\PycharmProjects\untitled1\DB\7_layers\zhou class\model\first\first_Categories.csv'
    outpath = r"./DB/yang_class/manul_data/stem_first_Categories.csv"
    # temp(train,outpath)
    testpath= r"./DB/jeff_testdata/all_cp_test_dataset.csv"#146条
    outpath= r"./DB/jeff_testdata/new_result.csv"#146条
    wv_inpth=r"./DB/jeff_testdata/wordvec/new_test_dataset_bymyself.csv"#item=[labs,contents,products,orign_lab,outlab]
    # train_predict(inpth, outpath)#use tfidf classify words is stemmed
    wv_inpth = r"./DB/jeff_testdata/random_db_data.csv"
    # w2v_predict(wv_inpth, outpath)#use word2vec similary words is not stemmed
    inpath=r"./DB/jeff_testdata/wordvec/new_test_dataset_bymyself.csv"
    test=r"./DB/jeff_testdata/test.csv"
    # final_predict(inpath,outpath)

    # final_predict(inpath, outpath)
    other_check = r"./DB/jeff_testdata/zhou_class.csv"
    model_path = r'.\DB\jeff_testdata\classify for zh\20180805_zh_Categories_vocab.csv'
    # inpath=r'.\DB\company_db_data.csv'
    # new_predict(test, outpath, all_labList)
    # new_predict(test, outpath)
    tfidf_path=r"./DB/jeff_testdata/classify for zh/tfidf_union.csv"
    inpath = r"./DB/jeff_testdata/classify for zh/2018-08-06_company_zh.csv"
    inpath = r"./DB/jeff_testdata/classify for zh/test.csv"

    vocabList = simple_load(model_path)
    # print('vb:',len(vocabList),vocabList[:10])
    #1014 ['燃料', '供应', '煤', '原煤', '勘探', '开采', '加工', '煤层', '煤层气', '瓦斯']
    all_labList = all_labs(other_check)
    tf_labs=tfidf_labs(tfidf_path)

    relab = sepr_company_data(inpath, vocabList, all_labList, tf_labs)
    # inpath = r"./DB/company_db_data.csv"
    outpath= r"./DB/jeff_testdata/classify for zh/test_out.csv"
    # outpath= r"./DB/jeff_testdata/company_dataset_result.csv"

    task_out(outpath, relab)

    print('end job:', ctime())

