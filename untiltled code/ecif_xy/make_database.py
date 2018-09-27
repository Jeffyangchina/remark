#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import sqlite3
import csv
import re
conn=sqlite3.connect(r'C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\xy_zh_en.db')
def init():
    sql_init1='drop table if EXISTS zh_en'
    sql_init2='''create table zh_en(zh text PRIMARY KEY,en text,jc text)'''
    cursor=conn.cursor()
    cursor.execute(sql_init1)
    cursor.execute(sql_init2)
    conn.commit()
#
def clean_input(instr):
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    line = re.sub(r, '', instr)
    outstr = re.sub("[^\D]", "", line)
    return outstr
# init()
def normalize(name):
    return name.capitalize()
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)

def standar(str):
    if '_' in str or ' ' in str:
        if '_' in str:
            cel=list(str.split('_'))
            rm_null(cel)
            # print('00:',cel)
            en_out=list(map(normalize,cel))
            # print('11:',en_out)
            en_input='_'.join(en_out)

        if ' ' in str:
            cel2 = list(str.split(' '))
            rm_null(cel2)
            en_out2 = list(map(normalize, cel2))
            en_input = '_'.join(en_out2)
    else:
        en_input=str.capitalize()
    # print('22:', en_input)
    return en_input
def put_in():
    cursor=conn.cursor()
    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior0\extract_of_中英文.csv", "r",encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    rows1=[]
    rows2=[]
    rows3=[]
    i=2
    h=0
    def normalize(name):
        return name.capitalize()
    def standar(str):
        str=clean_input(str)
        if '_' in str or ' ' in str:
            if '_' in str:
                cel=list(str.split('_'))
                rm_null(cel)
                # print('00:',cel)
                en_out=list(map(normalize,cel))
                # print('11:',en_out)
                en_input='_'.join(en_out)

            if ' ' in str:
                cel2 = list(str.split(' '))
                rm_null(cel2)
                en_out2 = list(map(normalize, cel2))
                en_input = '_'.join(en_out2)
        else:
            en_input=str.capitalize()
        # print('22:', en_input)
        return en_input
    for row in reader:#row is a list,row[0] is a str,rows1 is a list
        rows1.append(row[0])
        if len(row)>1:
            rows2.append(row[1])
        else:
            rows2.append('')
        if len(row)>2:
            rows3.append(row[2])
        else:
            rows3.append('')
        # if i==2:
        #     print('2:',rows3)
        #     i=3
    lth=len(rows1)

    for i in range (lth):
        zh=rows1[i].strip()#is a str
        en=rows2[i].strip()
        jc=rows3[i].strip()
        # jc_1=rows3[i]
        en_1=standar(en)
        jc_1=standar(jc)

        # print('0:',zh,en_1,jc_1)
        sql = 'insert into zh_en VALUES(?,?,?) '
        try:
            cursor.execute(sql,(zh,en_1,jc_1))
        except Exception as e :
            print('err:',e)
            h+=1

    print('all is %s,unique is %s',(lth,h))
    csvFile.close()
    conn.commit()
    #sql='''create table C800_BV(cn text,en text,xn text)'''#删除是drop table C800_BV
    #cur.execute("PRAGMA table_info(table)")获取

    cursor.close()
    conn.commit()
    conn.close()
# put_in()
def check_same():
    cursor = conn.cursor()
    import os
    rootdir = r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\未处理\en"

    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    sql = 'select zh from zh_en '#zh---same china  en---same english
    res = cursor.execute(sql)  # 必须元组,所以只有一个值时要多加个,

    tempx = res.fetchall()#is a double list
    data=[]
    # print('0:',data)
    # print('1:',tempx[0])
    # print('2:',len(tempx))
    for i in range(len(tempx)):
        data.append(tempx[i][0].lower())
    # print('3:',len(data))
    # sql = 'select jc from zh_en '这部分是英文提取
    # res = cursofor i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        new_path = os.path.join(rootdir, 'new_'+list[i])
        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile2 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer = csv.writer(csvFile2)
            input_data=[]
            for item in reader:#a list
                for i in range (len(item)):
                    if item[i].lower() in data:
                        item[i]='----'
                if item[0]!='----':

                    writer.writerow(item)
            csvFile.close()
            csvFile2.close()  # 必须元组,所以只有一个值时要多加个,
    # tempx = res.fetchall()  # is a double list
    # for i in range(len(tempx)):
    #     data.append(tempx[i][0].lower())
    # print('4:', len(data))

    #
# init()
def put_in_1():#prior2
    sql_init1 = 'drop table if EXISTS zh_en_prior1'
    sql_init2 = '''create table zh_en_prior1(zh text PRIMARY KEY,en text,jc text)'''
    cursor = conn.cursor()
    cursor.execute(sql_init1)
    cursor.execute(sql_init2)
    conn.commit()
    cursor = conn.cursor()
    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior2\prior2.csv", "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    rows1 = []
    rows2 = []
    h=0

    for item in reader:  # a list
        rows1.append(item[0])
        zh=item[0].strip()
        en=item[1].strip()
        en_1 = standar(en)
        zh=clean_input(zh)
        jc_1=''

        sql = 'insert into zh_en_prior1 VALUES(?,?,?) '

        try:
            cursor.execute(sql, (zh, en_1, jc_1))
        except Exception as e:
            print('err:', e)
            h += 1
    lth=len(rows1)
    print('1all is %s,unique is %s', (lth, h))
    csvFile.close()
    conn.commit()
    # sql='''create table C800_BV(cn text,en text,xn text)'''#删除是drop table C800_BV
    # cur.execute("PRAGMA table_info(table)")获取

    cursor.close()
    conn.commit()
    conn.close()
# put_in_1()
def put_in_2():#prior2 英汉字典，所以英文字段要处理同put_in
    import os
    sql_init1 = 'drop table if EXISTS zh_en_prior2'
    sql_init2 = '''create table zh_en_prior2(zh text PRIMARY KEY,en text,jc text)'''
    cursor = conn.cursor()
    cursor.execute(sql_init1)
    cursor.execute(sql_init2)
    conn.commit()
    cursor = conn.cursor()

    i = 2
    h = 0

    rootdir= r'C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior3'
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        rows1 = []
        rows2 = []
        rows3 = []
        path = os.path.join(rootdir, list[i])

        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            print('0:',path)
            input_data = []
            for row in reader:  # row is a list,row[0] is a str,rows1 is a list
                rows1.append(row[0])
                if len(row) > 1:
                    rows2.append(row[1])
                else:
                    rows2.append('')
                if len(row) > 2:
                    rows3.append(row[2])
                else:
                    rows3.append('')
                    # if i==2:
                    #     print('2:',rows3)
                    #     i=3
            lth = len(rows1)

            for i in range(lth):
                zh = rows1[i].strip()  # is a str
                en = rows2[i].strip()
                jc = rows3[i].strip()
                # jc_1=rows3[i]
                zh=clean_input(zh)
                en_1 = standar(en)
                if jc!='':
                    jc_1 = standar(jc)
                else:
                    jc_1=jc

                # print('0:',zh,en_1,jc_1)
                sql = 'insert into zh_en_prior2 VALUES(?,?,?) '
                try:
                    cursor.execute(sql, (zh, en_1, jc_1))
                except Exception as e:
                    # print('err:', e)
                    h += 1

            print('all is %s,unique is %s', (lth, h))
            conn.commit()
            # sql='''create table C800_BV(cn text,en text,xn text)'''#删除是drop table C800_BV
            # cur.execute("PRAGMA table_info(table)")获取
        csvFile.close()

    cursor.close()
    conn.commit()
    conn.close()
# put_in_2()