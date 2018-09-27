#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
from multiprocessing import Process
import time
#import c800_bv_msg as msg_db
import sqlite3
import xlrd
import neo4j_py2neo as npy
def callback_db(ptr, count):

    time.sleep(0.1) #如果获取不到锁，等待0.5秒
    #printf("database is locak now,can not write/read.\n");  //每次执行一次回调函数打印一次该信息
    return 1    #//回调函数返回值为1，则将不断尝试操作数据库。
#conn = sqlite3.connect(r'E:\c800_bv_msg.db', isolation_level="IMMEDIATE", timeout=60,check_same_thread=False)
# filexls = r'E:\name.xlsx'
# book = xlrd.open_workbook(filexls)  # .strip('\'')
# table = book.sheets()[1]  # 从0开始


# def work(xbg,xed):
#     #conn = sqlite3.connect(r'E:\c800_bv_msg.db', isolation_level="IMMEDIATE", timeout=60,check_same_thread=False)
#     #cursor = conn.cursor()
#     #msg_db.export_data(xbg,xed)
#
#
#     # filexls=r'E:\name.xlsx'
#     # book=xlrd.open_workbook(filexls)#.strip('\'')
#     # table=book.sheets()[1]#从0开始
#     nrows=table.nrows
#     lis=[]
#     for i in range(xbg,xed):
#         cursor = conn.cursor()
#         lis = []
#         cname = table.cell_value(i, 2).strip('\'')
#
#         # ename = table.cell_value(i, 1).strip('\'')
#         xname = table.cell_value(i, 0).strip('\'')
#
#
#             # sql = 'insert into C800_BV VALUES(?,?,?,?) '
#             # cursor.execute(sql, (cname,'','',''))
#        # print('3:',cname,xname)
#         msgdic=npy.dfind(xname)#dict
#         #print('4:',msgdic)
#
#         sql_cmd = 'select redm,otherm,param from C800_BV where inmsg=?'
#         cursor.execute(sql_cmd, (cname,))
#         tempx = cursor.fetchall()
#         try:
#             ta = tempx[0][0]
#             lis.append(ta)
#         except IndexError as e:
#             print(tempx)
#         try:
#             tb = tempx[0][1]
#             lis.append(tb)
#         except:
#             print(tempx)
#         try:
#             tc = tempx[0][2]
#             lis.append(tc)
#         except:
#             print(tempx)
#
#
#
#
#         index=0
#         #print('0:',lis)
#         for tkey in msgdic:
#             ctem = lis[index]
#             index+=1
#             #print('1:',ctem)
#             # print('1:',tkey)
#             for cel in msgdic[tkey]:
#                 if cel not in ctem:
#                 # print('0:',cel)
#                     ctem += (cel + '*')
#             # print('2:', ctem)
#             sql = 'update C800_BV set ' + tkey + '=? where inmsg=? '  # 使用变量方式特别+tkey+
#
#             cursor.execute(sql, (ctem, cname))
#         cursor.close()
#         conn.commit()
def find_msg(bg,ed):
    conn = sqlite3.connect(r'E:\c800_bv_excel.db',isolation_level="IMMEDIATE", timeout=10,check_same_thread=False)
    cursor = conn.cursor()
    for xn in range(bg,ed):
        sql='select xname,redmsg,othermsg,param from C800_BV where rowid=?'
        cursor.execute(sql,(xn,))
        msg_x = cursor.fetchall()

        if len(msg_x) > 0:
            #print('m:', msg_x[0][1])
            if msg_x[0][1]==None and msg_x[0][2]==None and msg_x[0][3]==None and len(msg_x[0])>0:

                msgdic={}

                xxme=msg_x[0][0]
                #print('ok:',xxme)
                msgdic = npy.npy(xxme)  # dict


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

                    sql = 'update C800_BV set ' + tkey + '=? where rowid=? '  # 使用变量方式特别+tkey+
                    if ctem != '':
                        cursor.execute(sql, (ctem, xn))
                        conn.commit()

if __name__ == '__main__':
    # Process(target=work,kwargs={'name':'egon'})
    oldtime=time.clock()
    lt=[]
    for x in range(14):
        lt.append(str(x))
    for item in lt:
        item=Process(target=find_msg,args=(int(item)*100,(int(item)+1)*100))
        item.start()
    # p1=Process(target=work,args=(20,40))
    # p2=Process(target=work,args=(40,60))
    # p1.start()
    # p2.start()
    print('tme:',time.clock()-oldtime)
