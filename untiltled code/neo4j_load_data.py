#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import os
import xlrd
import time
import re
import copy
from py2neo import Graph,Node,Relationship
tf=Graph("http://localhost:7474", username="neo4j", password="yang")
#tf.delete_all()
filexls=r'E:\name.xlsx'
book=xlrd.open_workbook(filexls)#.strip('\'')
table=book.sheets()[0]#从0开始
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
    graph.merge(node)
def push_rel(k1,k2,graph):

    node1=graph.find_one('C800_BV_msg',property_key='xname',property_value=k1)
    node2 = graph.find_one('C800_BV_msg', property_key='xname',property_value=k2)
    rel=Relationship(node1,'to_msg',node2)

    graph.merge(rel)
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
    # for kx in al:
    #     for kw in bl:
    #         if kw==kx:
    #             bl.remove(kw)
    for keys in al:
        #print('0:',keys)
        for keys2 in bl:

            if keys !=keys2:

                push_rel(keys, keys2, tf)
for (root,dirs,files) in os.walk(add):
    for item in files:
        oldtime=time.clock()

        t1=0
        if_m=0
        # if_list=[]
        # then_list=[]
        slist=''
        if_dic={}
        then_dic={}
        with open(add+'\\'+item,'r+',encoding='ISO-8859-1') as f1:
			# print(f.readline())
            if_dic = {}
            then_dic = {}
            f.write(item+'\n')
            fx=f1.readlines()
            t1 = 0
            if_m = 0
            #print('0::',len(fx))
            for s in fx:

                s=s.strip()
                s = s.strip(';')
                s = s.strip('}')
                s = s.strip('{')
                #print('0:',s)
                #if s.startswith('if '):
                if 'if ' in s and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):
                    t1+=1
                    if_m += 1
                if t1>0:
                    slist=s.split()

                    for ih in slist:

                        if 'then' in ih and not s.startswith('|') and not s.startswith('*') and not s.startswith('#') :
                            if_m-=1
                        # if ih=='if' and not s.startswith('|') and not s.startswith('*') and not s.startswith('#') :
                        #     if_m +=1
                        #     t1+=1
                        if len(ih)>12 and ('_' in ih):
                            #ih = re.sub(r'\[\d+\]', '', ih)#\是转义用 ，连续
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
                                ite=ih.split('+')
                                for itm in ite:
                                    if '_' in itm:
                                        ih=itm
                            if '=' in ih:
                                ite=ih.split('=')
                                for itm in ite:
                                    if '_' in itm:
                                        ih=itm
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
                            if(if_m>0):
                                if not if_dic.get(t1):
                                    if_dic[t1]=[]
                                if ih not in if_dic[t1]:
                                    if_dic[t1].append(ih)

                                   #if_list.append(ih)
                            else:
                                if not then_dic.get(t1):
                                    then_dic[t1]=[]
                                if ih not in then_dic[t1]:
                                    #then_list.append(ih)
                                    then_dic[t1].append(ih)
                        #print('if_dic:', if_dic)
                        #print('th_dic:', then_dic)
                        if 'endif' in ih and not s.startswith('|') and not s.startswith('*') and not s.startswith('#'):


                            if t1>0:

                                iflis=[]
                                thenlis=[]
                                if not then_dic.get(t1):
                                    then_dic[t1] = []
                                if then_dic[t1]!=None:
                                    thenlis=copy.deepcopy(then_dic[t1])
                                    #then_dic[t1]=[]
                                tx=t1
                                # while(tx>0):
                                #     if not if_dic.get(tx):
                                #         if_dic[tx] = []
                                #     iflis.extend(if_dic[tx])
                                #     tx-=1
                                while(tx>0):
                                    if not if_dic.get(tx):
                                        if_dic[tx]=[]
                                    iflis=if_dic[tx]
                                    thenlis =copy.deepcopy(then_dic[t1])
                                    #print('0:',t1,iflis,thenlis)
                                    if iflis != [] and thenlis != []:
                                        for l1 in iflis:
                                            for l2 in thenlis:
                                                if l1==l2:
                                                    thenlis.remove(l2)
                                    if iflis != [] and thenlis != []:
                                        writein(iflis, thenlis, f)
                                    tx-=1
                                #
                                # if iflis!=[] and thenlis!=[]:
                                #     writein(iflis,thenlis,f)
                            if_dic[t1]=[]
                            then_dic[t1]=[]
                            t1 -= 1
                        if t1==0:
                            if_m =0
                            if_dic = {}
                            then_dic = {}
                            break
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