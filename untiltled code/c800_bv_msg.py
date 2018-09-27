#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import sqlite3#将中英文导入本地数据库，为了输
import xlrd
import neo4j_py2neo as npy
import time
conn = sqlite3.connect(r'E:\c800_bv_msg.db',check_same_thread=False)
cursor = conn.cursor()
def url_exists(url,xname):
    # conn = sqlite3.connect(r'E:\c800_bv_msg.db')
    # cursor = conn.cursor()
    sql_cmd = 'select * from C800_BV where inmsg=? '
    cursor.execute(sql_cmd,(url,))
    res = cursor.fetchall()
    suc = True
    if len(res) > 0 :
        #print '%s exists' % url

        pass
    else:
        sql_cmd_2 = 'insert into C800_BV VALUES(?,?,?,?,?) '
        cursor.execute(sql_cmd_2,(url,xname,'','',''))
        # print '%s added' % url
        # suc = False

def init_db(bg,ed):
    filexls = r'E:\name.xlsx'
    book = xlrd.open_workbook(filexls)  # .strip('\'')
    table = book.sheets()[1]  # 从0开始
    nrows = table.nrows
    # 'bv_conveyor_extr_move_not_permitted_rem'
    # conn=sqlite3.connect(r'E:\c800_bv_msg.db')
    sql_init1 = 'drop table if EXISTS C800_BV'
    sql_init2 = '''create table C800_BV(inmsg text,enmsg text,redm text,otherm text,param text)'''
    ctem = ''
    # cursor=conn.cursor()
    cursor.execute(sql_init1)  # 这是重头重建

    cursor.execute(sql_init2)
    # conn.commit()
    for i in range(bg, ed):
        cname = table.cell_value(i, 2).strip('\'')

        # ename = table.cell_value(i, 1).strip('\'')
        xname = table.cell_value(i, 0).strip('\'')
        if cname != '' and cname != None:
            url_exists(cname,xname)

def cname_exist(cname):
    sql_cmd = 'select redm,otherm,param from C800_BV where inmsg=?'
    cursor.execute(sql_cmd, (cname,))
    tempx = cursor.fetchall()

    ta = tempx[0][0]

    tb = tempx[0][1]

    tc = tempx[0][2]
    return ta,tb,tc
# def export_data(bg,ed):
#     lis=[]
#
#     msgdic=npy.dfind(xname)#dict
#     #print('4:',msgdic)
#     ta,tb,tc=cname_exist(cname)
#     lis.append(ta)
#     lis.append(tb)
#     lis.append(tc)
#     index=0
#     #print('0:',lis)
#     for tkey in msgdic:
#         ctem = lis[index]
#         index+=1
#         #print('1:',ctem)
#         # print('1:',tkey)
#         for cel in msgdic[tkey]:
#             if cel not in ctem:
#                 # print('0:',cel)
#                 ctem += (cel + '*')
#         # print('2:', ctem)
#         sql = 'update C800_BV set ' + tkey + '=? where inmsg=? '  # 使用变量方式特别+tkey+
#
#         cursor.execute(sql, (ctem, cname))

        # conn.commit()
    #sql='''create table C800_BV(cn text,en text,xn text)'''#删除是drop table C800_BV
    #cur.execute("PRAGMA table_info(table)")获取
def find_msg():
    conn = sqlite3.connect(r'E:\c800_bv_excel.db',check_same_thread=False)
    cursor = conn.cursor()
    sql='select xname from C800_BV '
    cursor.execute(sql)
    msg_x = cursor.fetchall()

    for mx in msg_x:
        msgdic={}
        oldtime = time.clock()
        xname=mx[0]
        msgdic = npy.npy(xname)  # dict
        #print(xname,msgdic)

        index=0
        #print('0:',lis)
        for tkey in msgdic:
            ctem=''
            index+=1
            #print('1:',ctem)
            # print('1:',tkey)
            for cel in msgdic[tkey]:
                if cel not in ctem:
                    # print('0:',cel)
                    ctem += (cel + '*')
            # print('2:', ctem)
            sql = 'update C800_BV set ' + tkey + '=? where xname=? '  # 使用变量方式特别+tkey+

            cursor.execute(sql, (ctem, xname))
            conn.commit()
        print(time.clock()-oldtime)
#init_db(0,2819)#新建表的第一步
#export_data(2488,2514)
find_msg()

cursor.close()
conn.commit()
conn.close()