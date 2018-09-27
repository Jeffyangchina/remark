#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import py2neo
from py2neo import Graph,Node,Relationship
import time
import xlrd
import sqlite3
conn = sqlite3.connect(r'E:\c800_bv_excel.db',check_same_thread=False)
cursor = conn.cursor()
tf=Graph("http://localhost:7474", username="neo4j", password="yang")
end_nodes_list=[]
red_msg_nodes=[]
other_msg_nodes=[]
dp_nodes=[]
x_red_msg_nodes=[]
x_other_msg_nodes=[]
x_dp_nodes=[]
nlist=[]
tlist=[]
clist=[]
relt_a=[]
relt_b=[]
relt_c=[]
mark=0
filexls=r'E:\name.xlsx'
book=xlrd.open_workbook(filexls)#.strip('\'')
table=book.sheets()[1]#从0开始
nrows=table.nrows
def get_name(st):
    for i in range (nrows):
        #print('0:',i)

        if st==table.cell_value(i, 0).strip('\''):

            return table.cell_value(i, 2).strip('\'')
        else:
            continue
def get_sqlite_name(st):
    sql_get = 'select cname from C800_BV where xname=?'
    cursor.execute(sql_get, (st,))
    tempx = cursor.fetchall()
    if len(tempx)>0:
        #print('get:',tempx[0][0])
        return tempx[0][0]

def find_end_nodes(graph,node,nlist,calist):
    #global nlist
    global mark
    global tlist
    global clist
    node_list=graph.match_one(rel_type='to_msg',end_node=node,bidirectional=False)
    #print('0:',node_list)
    #print('00:', node_list.start_node()['cname'])

    if node_list==None:
        #print('1:',nlist)
        if node['xname'] not in nlist:

            nlist.append(node['xname'])
            calist.append(node['xname'])
        if node['cname']!=None:
            #print('12:')'%_rem%','%_rsm','%_ysm%','%_msm%'

            if node['cname'] not in end_nodes_list:
                end_nodes_list.append(node['cname'])
                if '_rem' in node['xname'] or '_rsm' in node['xname']:
                    if node['cname'] not in red_msg_nodes:
                        red_msg_nodes.append(node['cname'])
                    if node['xname'] not in x_red_msg_nodes:
                        x_red_msg_nodes.append(node['xname'])
                elif '_csm' in node['xname'] or '_ysm' in node['xname'] or '_msm' in node['xname']:
                    if node['cname'] not in other_msg_nodes:
                        other_msg_nodes.append(node['cname'])
                    if node['xname'] not in x_other_msg_nodes:
                        x_other_msg_nodes.append(node['xname'])
                else:
                    if node['cname'] not in dp_nodes:
                        dp_nodes.append(node['cname'])
                    if node['xname'] not in x_dp_nodes:
                        x_dp_nodes.append(node['xname'])


    else:
        tlist=[]
        lists = graph.match(rel_type='to_msg', end_node=node, bidirectional=False)

        for nd in lists:
            if nd.start_node()['xname'] not in nlist:
                tlist.append(nd)
                nlist.append(nd.start_node()['xname'])
                calist.append(nd.start_node()['xname'])
        #
            #print('none')
        if tlist !=[]:
            for kl in tlist:
                #print('00:',kl.start_node()['xname'])

                gxname=kl.start_node()['xname']
                gcname=get_name(gxname)
                nlist.append(gxname)
                if gcname!=None:
                    if '_rem' in gxname or '_rsm' in gxname and '__EO' not in gxname:
                        # if gcname not in red_msg_nodes:
                        #     red_msg_nodes.append(gcname)
                        if gxname not in x_red_msg_nodes:
                            x_red_msg_nodes.append(gxname)
                    elif '_csm' in gxname or '_ysm' in gxname or '_msm' in gxname:
                        # if gcname not in other_msg_nodes:
                        #     other_msg_nodes.append(gcname)
                        if gxname not in x_other_msg_nodes:
                            x_other_msg_nodes.append(gxname)
                    elif '_ipr' in gxname or '_dpr' in gxname :
                    #else:
                        # if gcname not in dp_nodes:
                        #     dp_nodes.append(gcname)
                        if gxname not in dp_nodes:
                            x_dp_nodes.append(gxname)

                find_end_nodes(graph, kl.start_node(),nlist,calist)
    #print('cc:',x_dp_nodes)
    return  x_red_msg_nodes, x_other_msg_nodes, x_dp_nodes
    # return red_msg_nodes, other_msg_nodes, dp_nodes
def dfind(xname,nlist,calist):
    x_red_msg_nodes = []
    x_other_msg_nodes = []
    x_dp_nodes = []
    #oldtime=time.clock()
    root_node=tf.find_one('C800_BV_msg',property_key='xname',property_value=xname)
    if root_node ==None:
        x=[]
        y=[]
        z=[]
        return x,y,z
    else:
        tt=root_node['cname']
        tt2='条盒包装机'
        tt3='透明纸包装机'
        ttx = root_node['xname']
        x_red_msg_nodes, x_other_msg_nodes, x_dp_nodes=find_end_nodes(tf,root_node,nlist,calist)
        # if tt in red_msg_nodes:
        #     red_msg_nodes.remove(tt)
        # if tt2 in dp_nodes:
        #     dp_nodes.remove(tt2)
        # if tt3 in dp_nodes:
        #     dp_nodes.remove(tt3)


        if ttx in x_red_msg_nodes:
            x_red_msg_nodes.remove(ttx)
        if ttx in x_dp_nodes:
            x_dp_nodes.remove(ttx)
        if ttx in x_dp_nodes:
            x_dp_nodes.remove(ttx)
    #print('cd:',x_dp_nodes)
    return x_red_msg_nodes, x_other_msg_nodes, x_dp_nodes

def init_find(xt):
    nlist = []
    calist=[]
    rn, on, pn = dfind(xt,nlist,calist)
    #print('22:',calist)
    return rn,on,pn

def filter_pr(lt):

    sql_cmd = 'select modu from C800_BV where xname=?'
    cursor.execute(sql_cmd, (lt,))
    tempx = cursor.fetchall()
    if len(tempx) > 0:
        #print('xx:',tempx[0][0])
        tempmd=tempx[0][0].split('*')

        try:
            tempmd.remove('')
        except:
            pass
        #print('xx2:', tempmd)
        return tempmd
    else:
        tempmd=[]
        #print('xx1:', tempmd)
        return tempmd
def filter_list(lst,cplst):
    reout=[]
    for xx in lst:
        xmd=filter_pr(xx)
        comlist=list(set(xmd).intersection(set(cplst)))
        #print('d:',comlist)
        if len(comlist)>0:
            reout.append(xx)
    #print('dd:',reout)
    return reout
oldtime=time.clock()
# xt = 'bv_entry_bad_pack_formation_check_rsm'
def npy(xt):
    relt_a = []
    relt_b = []
    relt_c = []
    rnx=[]
    onx=[]
    pnx=[]
    end_nodes_list = []
    red_msg_nodes = []
    other_msg_nodes = []
    dp_nodes = []
    x_red_msg_nodes = []
    x_other_msg_nodes = []
    x_dp_nodes = []
    nlist = []
    tlist = []
    clist = []
    outdi = {}
    xt_md=filter_pr(xt)
    #print('ss:',xt_md)
    rnx, onx, pnx = init_find(xt)
    #print('0:',pnx)
    if len(xt_md)>0:
        if len(rnx)>0:
            rnx=filter_list(rnx,xt_md)
        if len(onx)>0:
            onx=filter_list(onx,xt_md)
        if len(pnx)>0:
            pnx=filter_list(pnx,xt_md)

    for xn in rnx:
        if get_sqlite_name(xn) not in relt_a:
            relt_a.append(get_sqlite_name(xn))
    for xn in onx:
        if get_sqlite_name(xn) not in relt_b:
            relt_b.append(get_sqlite_name(xn))
    for xn in pnx:
        if get_sqlite_name(xn) not in relt_c:
            relt_c.append(get_sqlite_name(xn))
        if 'ch_gp_film_chains_cross_step_ipr' in relt_c:
            relt_c.append('透明纸移位寄存中断工步')
            relt_c.remove('ch_gp_film_chains_cross_step_ipr')
    outdi['redmsg'] = relt_a
    outdi['othermsg'] = relt_b
    outdi['param'] = relt_c
    return outdi
# print(npy('ch_wl_wheel_heater_2F_diag_type1_xii_rsm'))
