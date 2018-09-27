#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun

import os
import xlrd
import time
import re
from py2neo import Graph,Node,Relationship
tf=Graph("http://localhost:7474", username="neo4j", password="yang")
#tf.delete_all()
filexls=r'E:\name.xlsx'
book=xlrd.open_workbook(filexls)#.strip('\'')
table=book.sheets()[1]#从0开始
nrows=table.nrows

add=r'E:\gdl'
markadd=r'E:\\mark.txt'
f=open(markadd,'a+')
mark=0
wm=0
def get_name(st):
    for i in range (nrows):
        #print('0:',i)

        if st==table.cell_value(i, 0).strip('\''):
            if table.cell_value(i, 2).strip('\'')=='':
                return table.cell_value(i, 1).strip('\''),table.cell_value(i, 1).strip('\'')
            else:
                return table.cell_value(i, 2).strip('\''),table.cell_value(i, 1).strip('\'')
        else:
            continue
def push_in(graph,label,dname,ename=None,cname=None):
    node=Node(label,ename=ename,cname=cname,xname=dname)
    #print('node:',node)
    graph.merge(node)
def push_rel(k1,k2,graph):

    node1=graph.find_one('C800_BV_msg',property_key='xname',property_value=k1)
    node2 = graph.find_one('C800_BV_msg', property_key='xname',property_value=k2)
    rel=Relationship(node1,'to_msg',node2)
    #print('rel:',rel)
    graph.merge(rel)
def writein2(list1,list2):
    for icel in list1:
        #print('1:',get_name(al[i]))

        if (get_name(icel)):
            #ad[mark] = al[i]
            #print('x:')
            cname, ename = get_name(icel)
            #print('0:',icel)
            #file.write(str(mark))
            #file.write('，'+al[i]+'，'+cname+'，'+ename+'\n')
            push_in(tf,'C800_BV_msg',icel,ename,cname)
            #mark+=1

        else:
            #file.write(str(mark)+'，'+al[i]+ '\n')
            #print('nofind',icel)
            push_in(tf, 'C800_BV_msg', icel)
            #mark += 1

    for icel2 in list2:
        #print('1:', get_name(bl[x]))

        if (get_name(icel2)):
            #bd[mark] = bl[x]
            #print('g:')
            cname, ename = get_name(icel2)
            #file.write(str(mark))
            #print('01:',icel2)
            #file.write('，'+bl[x]+'，'+cname+'，'+ename+'，'+'\n')
            push_in(tf, 'C800_BV_msg' , icel2,ename, cname)
            #mark += 1
        else:
            #file.write(str(mark)+'，'+bl[x] + '\n')
            #print('02:', icel2)
            push_in(tf, 'C800_BV_msg',icel2)
            #mark += 1
    for keys in list1:
        #print('0:',keys)
        for keys2 in list2:
            if keys !=keys2:
                #file.write(keys + '，' + ' to_msg, ' + keys2 + '\n')
                # file.write(ad[keys]+ '，to,' +bd[keys2] + '\n')
                #print('2:',keys,keys2)
                push_rel(keys, keys2, tf)
def writein(al,bl,file):
    global mark
    alen=len(al)
    blen=len(bl)
    ad={}
    bd={}
    for i in range(alen):
        #print('1:',get_name(al[i]))

        if (get_name(al[i])):
            ad[mark] = al[i]
            #print('x:')
            cname, ename = get_name(al[i])
            #file.write(str(mark))
            #file.write('，'+al[i]+'，'+cname+'，'+ename+'\n')
            push_in(tf,'C800_BV_msg',al[i],ename,cname)
            mark+=1

        else:
            #file.write(str(mark)+'，'+al[i]+ '\n')
            push_in(tf, 'C800_BV_msg', al[i])
            mark += 1

    for x in range(blen):
        #print('1:', get_name(bl[x]))

        if (get_name(bl[x])):
            bd[mark] = bl[x]
            #print('g:')
            cname, ename = get_name(bl[x])
            #file.write(str(mark))
            #file.write('，'+bl[x]+'，'+cname+'，'+ename+'，'+'\n')
            push_in(tf, 'C800_BV_msg' , bl[x],ename, cname)
            mark += 1
        else:
            #file.write(str(mark)+'，'+bl[x] + '\n')
            push_in(tf, 'C800_BV_msg', bl[x])
            mark += 1
    # print('a:',ad)
    # print('b:',bd)
    # for keys in ad:
    #     #print('0:',keys)
    #     for keys2 in bd:
    #         if ad[keys] not in bd[keys2]:
    #             file.write(ad[keys]+ '，' +' to_msg, '+ bd[keys2] + '\n')
    #             #file.write(ad[keys]+ '，to,' +bd[keys2] + '\n')
    #             push_rel(ad[keys],bd[keys2],tf)
    #print('0:',al)
    #print('1:',bl)
    for keys in al:
        #print('0:',keys)
        for keys2 in bl:
            if keys !=keys2:
                #file.write(keys + '，' + ' to_msg, ' + keys2 + '\n')
                # file.write(ad[keys]+ '，to,' +bd[keys2] + '\n')
                #print('0:',keys2)
                push_rel(keys, keys2, tf)
for (root,dirs,files) in os.walk(add):
    for item in files:
        oldtime=time.clock()
        at=0
        t1=0
        kt=0
        if_m=0
        # if_list=[]
        # then_list=[]
        slist=''
        if_dic={}
        then_dic={}
        acti=[]
        disp=[]
        with open(add+'\\'+item,'r+',encoding='ISO-8859-1') as f1:
			# print(f.readline())
            if_dic = {}
            then_dic = {}
            f.write(item+'\n')
            fx=f1.readlines()
            #print('0::',len(fx))
            for s in fx:

                s=s.strip()
                # s = s.strip(';')
                # s = s.strip('}')
                # s = s.strip('{')
                #print('0:',s)
                #if s.startswith('if '):
                if 'activators' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):
                    at=1
                # if '{' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):
                #     kt=1
                # if '}' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):
                #     kt=0
                # if 'end' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):
                #     at=0
                if 'if ' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):
                    t1+=1
                if 'endif' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):
                    t1-=1
                if at>0 and t1==0:
                    #print('0:',s)
                    if 'end;' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):
                        at = 0
                    slist=s.split()
                    #print('at:',at)
                    for ih in slist:
                        #print('ih0:',ih)
                        if '{' in ih:
                            kt=1
                            if 'step of powerup' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):

                                if  'step of powerup' not in acti:
                                    acti.append('step of powerup')
                        #print('kt:',kt)
                        # if 'then' in ih and not s.startswith('|') and not s.startswith('*') and not s.startswith('#') :
                        #     if_m-=1
                        if len(ih)>10 and ('_' in ih):
                            #ih = re.sub(r'\[\d+\]', '', ih)#\是转义用 ，连续
                            ih1 = re.sub(r'\[.*\]', '', ih)
                            ih1 = re.sub(r'\{.*\}', '', ih1)
                            ih1 = ih1.strip(';')
                            ih1 = ih1.strip('}')
                            ih1 = ih1.strip('{')
                            ih1 = ih1.strip(']')
                            ih1 = ih1.strip(')')
                            ih1 = ih1.strip('[')
                            ih1 = ih1.strip(',')
                            #print('ih:',ih1)
                            if '+' in ih1:
                                ite=ih1.split('+')
                                for itm in ite:
                                    if '_' in itm:
                                        ih1=itm
                            if '=' in ih1:
                                ite=ih1.split('=')
                                for itm in ite:
                                    if '_' in itm:
                                        ih1=itm
                            if '*' in ih1:
                                ite=ih1.split('*')
                                for itm in ite:
                                    if '_' in itm:
                                        ih1=itm
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
                            if(kt==1):
                                # if not if_dic.get(t1):
                                #     if_dic[t1]=[]
                                # if ih not in if_dic[t1]:
                                #     if_dic[t1].append(ih)
                                if ih1 not in acti:
                                    acti.append(ih1)

                                   #if_list.append(ih)
                            #print('kt2:',ih)
                            if(kt==0):
                                if ih1 not in disp:
                                    disp.append(ih1)

                        if '}' in ih:
                            #print('dd')
                            kt = 0

                    if at==0:
                        #print('aa:',acti,disp)
                        if len(acti)>0 and len(disp)>0:
                            #print('1:',acti,disp)
                            writein2(acti,disp)
                        acti=[]
                        disp=[]
                # if 'endif;' in s:
                #     #print('2:',t1)
                #
                #     t1-=1
                # if t1==0:
                #     writein(if_list,then_list,f)
                #     if_list=[]
                #     then_list=[]
        print(item + ':' + str(time.clock() - oldtime))
f.close()