#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import csv
import jieba
import sqlite3
import re
import os
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)
    return lis
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
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
def out_num(instr):
    outstr = re.sub('[0-9]+$', '', instr)
    outstr = re.sub('^[0-9]+', '', outstr)

    return outstr
def rm_space(astr):
    out_=re.sub(' ','',astr)
    return out_
def out_en(astr):
    outstr = re.sub("[a-zA-Z]", "", astr)
    outstr=outstr.strip()
    return outstr
def jieba_cut(astr,conn):#最终用于处理输入，常用词标点去除,返回空格连接的字符串
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
    astr = astr.strip()
    ostr = rm_puc(astr)
    olist = list(jieba.cut(ostr))
    olist=rm_same(olist)
    olist = rm_null(olist)
    stopwords = stopwordslist('./stopword_zh_en.txt')
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


    return data
def eng_cut(astr):
    item=astr.strip()
    xlist = list(item.split("_"))
    xlist=rm_null(xlist)
    return xlist
def delwith_srcb(root,name):#处理翻译参照表
    db_path='./Db_classify.db'
    conn = sqlite3.connect(db_path)
    file_path=os.path.join(root, name)
    write_path=os.path.join(root, 'new_'+name)
    write_path1 = os.path.join(root, 'new_conf' + name)
    csvFile = open(file_path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    csvFile1 = open(write_path1, 'w', newline='',
                    encoding='UTF-8')  # 写入匹配不成功的
    writer1 = csv.writer(csvFile1)
    csvFile2 = open(write_path, 'w', newline='',
                    encoding='UTF-8')  # 写入匹配成功的

    writer2 = csv.writer(csvFile2)
    data = []
    rows_en=[]
    rows_zh=[]
    for row in reader:
        if row:
            rows_zh.append(row[0])
            rows_en.append(row[1])
        else:
            print('err:',row)

    lth = len(rows_zh)
    print('src:',rows_zh[:2],rows_en[:2])
    for i in range(lth):

        x1 = jieba_cut(rows_zh[i],conn)
        x2 = eng_cut(rows_en[i])
        data1 = []
        data2 = []
        data3 = []
        if len(x1) == len(x2):
            for n in range(len(x1)):
                data1.append([x1[n],x2[n]])
        else:
            # print('1:', x1)
            writer1.writerow([rows_zh[i],rows_en[i]])
    for xx in data1:
        writer2.writerow(xx)

    csvFile.close()
    csvFile1.close()
    csvFile2.close()
# delwith_srcb(r'E:\兴业银行\中文翻译英文最终数据集\对照表','srcb_Attribute.csv')