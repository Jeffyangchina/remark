import os
import xlwt
import xlrd
import time
import re
import sqlite3
from xlutils.copy import copy
#import xlutils as xul
conn = sqlite3.connect(r'E:\c800_bv_excel.db',check_same_thread=False)
cursor = conn.cursor()
def init_db():
    filexls = r'E:\name.xlsx'
    book = xlrd.open_workbook(filexls)  # .strip('\'')
    table = book.sheets()[1]  # 从0开始
    nrows = table.nrows


    sql_init1 = 'drop table if EXISTS C800_BV'
    sql_init2 = '''create table C800_BV(xname text,cname text,modu text)'''
    ctem = ''
    # cursor=conn.cursor()
    cursor.execute(sql_init1)  # 这是重头重建

    cursor.execute(sql_init2)
    for i in range(nrows):
        xname = table.cell_value(i, 0).strip('\'')
        cname = table.cell_value(i, 2).strip('\'')
        sql_cmd_2 = 'insert into C800_BV VALUES(?,?,?) '
        cursor.execute(sql_cmd_2, (xname,cname,''))
    conn.commit()

def xlfind(st,xt):
    sql_cmd = 'select modu from C800_BV where xname=?'
    cursor.execute(sql_cmd, (st,))
    tempx = cursor.fetchall()
    #print('0:',tempx,st,xt)
    if len(tempx)>0:
        if xt not in tempx[0][0]:
            tempmd = tempx[0][0]+xt+'*'
            sql_add = 'update C800_BV set modu=? where xname=? '  # 使用变量方式特别+tkey+

            cursor.execute(sql_add, (tempmd,st))
            conn.commit()

def make_name(num=2):

    add = r'E:\gdl'
    # filexls = r'E:\name.xlsx'
    # book = xlrd.open_workbook(filexls)  # .strip('\'')
    # table = book.sheets()[1]  # 从0开始

    # nrows = table.nrows

    for (root, dirs, files) in os.walk(add):
        for item in files:
            oldtime = time.clock()
            with open(add + '\\' + item, 'r+', encoding='ISO-8859-1') as f1:
                xd=''
                fx = f1.readlines()
                for s in fx:
                    s = s.strip()
                    s = s.strip(';')
                    if 'module ' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):

                        slist = s.split()

                        for xx in slist:

                            if '_' in xx:
                                xt=xx.split('_')
                                for n in range(num):
                                    xd+=xt[n]+'_'
                                xd=xd[:-1]
                                break
                    stl=s.split()
                    for ih in stl:
                        if '_' in ih and len(ih)>10:
                            ih = re.sub(r'\[.*\]', '', ih)
                            ih = re.sub(r'\{.*\}', '', ih)
                            ih = ih.strip(';')
                            ih = ih.strip('}')
                            ih = ih.strip('{')
                            ih = ih.strip(']')
                            ih = ih.strip(')')
                            ih = ih.strip('[')
                            ih = ih.strip(',')
                            if '+' in ih:
                                ite = ih.split('+')
                                for itm in ite:
                                    if '_' in itm:
                                        ih = itm
                            if '=' in ih:
                                ite = ih.split('=')
                                for itm in ite:
                                    if '_' in itm:
                                        ih = itm
                            if '*' in ih:
                                ite = ih.split('*')
                                for itm in ite:
                                    if '_' in itm:
                                        ih = itm
                            if ',' in ih:
                                ite = ih.split(',')
                                for itm in ite:
                                    if '_' in itm:
                                        ih = itm
                            if '}' in ih:
                                ite = ih.split('}')
                                for itm in ite:
                                    if '_' in itm:
                                        ih = itm
                            xlfind(ih,xd)
        print(time.clock()-oldtime)

#make_name()

# inser_sql='ALTER table C800_BV ADD COLUMN redmsg text'
# cursor.execute(inser_sql)
# inser_sql='ALTER table C800_BV ADD COLUMN othermsg text'
# cursor.execute(inser_sql)
# inser_sql='ALTER table C800_BV ADD COLUMN param text'
# cursor.execute(inser_sql)
# conn.commit()
#init_db()
def init_add():

    filexls = r'E:\name.xlsx'
    book = xlrd.open_workbook(filexls)  # .strip('\'')
    table = book.sheets()[1]  # 从0开始
    nrows = table.nrows
    for i in range(nrows):
        xname = table.cell_value(i, 0).strip('\'')
        cname = table.cell_value(i, 2).strip('\'')
        sql_init_add = 'update C800_BV set cname=? where xname=? '
        cursor.execute(sql_init_add, (cname,xname))
    conn.commit()

