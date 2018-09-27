#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import sqlite3#将中英文导入本地数据库，为了输入的时候查询
import xlrd
filexls=r'E:\name.xlsx'
book=xlrd.open_workbook(filexls)#.strip('\'')
table=book.sheets()[0]#从0开始
nrows=table.nrows

conn=sqlite3.connect(r'D:\c800_bv_data.db')
sql_init1='drop table if EXISTS C800_BV'
sql_init2='''create table C800_BV(cn text,en text,xn text)'''
cursor=conn.cursor()
cursor.execute(sql_init1)

cursor.execute(sql_init2)
conn.commit()
for i in range(nrows):
    cname = table.cell_value(i, 2).strip('\'')
    ename = table.cell_value(i, 1).strip('\'')
    xname = table.cell_value(i, 0).strip('\'')
    sql = 'insert into C800_BV VALUES(?,?,?) '

    cursor.execute(sql,(cname,ename,xname))
    conn.commit()
#sql='''create table C800_BV(cn text,en text,xn text)'''#删除是drop table C800_BV
#cur.execute("PRAGMA table_info(table)")获取

cursor.close()
conn.commit()
conn.close()