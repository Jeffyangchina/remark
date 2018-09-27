#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import sqlite3
import jieba
from sklearn.metrics import pairwise as pw
import time
oldtime=time.clock()
# from sklearn.feature_extraction.text import CountVectorizer as CV
# from sklearn.feature_extraction.text import TfidfTransformer as TF

#sql='select cn ,xn from C800_BV where (cn like ?)'
#if cname != '' and ('_rem_' in xname or '_rsm_' in xname or '_ysm_' in xname or '_msm_' in xname)
# cv=CV()
# tf=TF()


def find_str(st):
    conn = sqlite3.connect(r'E:\c800_bv_data.db')
    cursor = conn.cursor()
    outlist = []
    scores = {}
    sql = 'select cn from C800_BV where (cn like ?) and (xn like ? or xn like ? or xn like ? or xn like ?)'
    for word in st:
        if len(word)>1:
            wx='%'+word+'%'
            res=cursor.execute(sql,(wx,'%_rem%','%_rsm','%_ysm%','%_msm%'))
            #res = cursor.execute(sql, (wx,))
            for i in res.fetchall():
                if i not in outlist:
                    # print('0:',i[0])
                    # print('1:',st)
                    #tdif_dic[i]=tf.fit_transform(cv.fit_transform(i))
                    scores[i[0]]=1
                    for k in st:
                        if k in i[0]:
                            scores[i[0]]+=1
                    outlist.append(i[0])
    return scores

def dofind(keywords):
    outdic=find_str(keywords)
    oy=sorted(outdic.items(),key =lambda x:x[1],reverse=True)
    finaloy=oy[:3]
    i=1
    di={}
    for key in finaloy:
        di[i]=key[0]
        print(str(i)+':'+key[0])
        i+=1

    print('time:',(time.clock()-oldtime))
#print(outlist[0][0][0])输出第一个字[0][0]则是输出第一条
def find_msg(st):#输出需要是个字典
    conn = sqlite3.connect(r'E:\c800_bv_msg.db')
    cursor = conn.cursor()

    msgdic = {}
    sql = 'select redm,otherm,param from C800_BV where inmsg=?'
    res = cursor.execute(sql,(st,))#必须元组,所以只有一个值时要多加个,


    tempx=res.fetchall()
    print('00:',tempx)
    temppm=tempx[0][2].split('*')#.remove('')

    temprm = tempx[0][0].split('*')  # .remove('')

    tempnr = tempx[0][1].split('*')  # .remove('')
    try:
        tempnr.remove('')
        temppm.remove('')
        temprm.remove('')
    except:
        pass

    msgdic['相关红色信息'] = temprm
    msgdic['相关提示信息'] = tempnr
    msgdic['相关参数'] = temppm
    print('0:',msgdic)
    # msgdic['redmsg'] = tempx[0].split('*')
    # for i in res.fetchall():
    #     templ=i.split('*')
    #     msgdic['redmsg']=templ
    #         # print('0:',i[0])
    #         # print('1:',st)
    #         #tdif_dic[i]=tf.fit_transform(cv.fit_transform(i))
    #         scores[i[0]]=1
    #         for k in st:
    #             if k in i[0]:
    #                 scores[i[0]]+=1
    #         outlist.append(i[0])00
    return 1
st='抽出器的运动未得到允许'
find_msg(st)
print('time:',(time.clock()-oldtime))