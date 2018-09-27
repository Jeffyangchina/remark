#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import pybloom as pb
import csv
import random
import numpy as np
import hashlib
import timeit
import time
import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.debug('yang ni hao')
# logger.info('should print')
# logger.info('should print')
prng = np.random.RandomState(1)
#
# import xmlrpc.client
# with xmlrpc.client.ServerProxy("http://localhost:8080/") as proxy:
#     # get_out=proxy.pp()
#     get_out=proxy.find_from_w2v('男')
#     # get_out=xmlrpc.client.Unmarshaller(get_out.data)
#     print(get_out)
#
#     # print('0:',s.model.most_similar('客户', topn=3))
#     # print(s.model)

px=prng.rand(1,1000000)
try:
    plx=px[0].tolist()
except Exception as err:

    logger.exception(err)
# print('u:')


# prng = np.random.RandomState(1)
# pt=prng.rand(1,1000000)
# plt=pt[0].tolist()
# bpx=hashlib.sha512(px)
# # bpx_=bpx.digest_size()
# bpx2=bpx.digest()
# bpt=hashlib.sha1(pt)
# print('0:',len(bpx2))
# if bpt==bpx:
#     print('ok')
# print('0:',px)
# px[0][2]=1
# print('1:',px)
# px=prng.rand(1,1000000)
#
#
# plx[2] = 1
# plx[10] = 1
#
# prng = np.random.RandomState(1)
# pt=prng.rand(1,1000000)
#
def check(list,blf):
    count=0
    print('xx:',type(list),len(list))
    i=0
    for x in list:
        if i<2:
            print('t:',blf.add(x)[0])
            i+=1
        if  blf.add(x)[0]==False:
            count+=1
    print('w:',count)
    return count
f = pb.BloomFilter(capacity=1500000, error_rate=0.01)
pl1=[]
# # f1 = pb.BloomFilter(capacity=1050, error_rate=0.001)
oldtime=time.time()
for x in plx:
    _, bi0 = f.add(x)
newtime=time.time()
print('0:',(newtime-oldtime))
newtime=time.time()
oldtime=time.time()
_, bi1= f.add(1)
newtime=time.time()
# print('0:',oldtime)
# print('1:',newtime)
print('1:',(newtime-oldtime))
# for x in plx:
#     writer1.writerow([x])
#     # _, bi0=f.add(x)
# newtime=time.time()
# csvFile1.close()
# print('0:',(newtime-oldtime))
# oldtime=time.time()
#
# xxx=check(plt,f)
# newtime=time.time()
# print('2:',xxx,(newtime-oldtime))
# for y in pt[0]:
#     _, bi1=f1.add(y)
# newtime=time.time()
# print('1:',(newtime-oldtime))
# oldtime=time.time()
# if bi1==bi0:
#     print('ok',type(bi1),bi1[:5])
# else:
#     bi=bi1^bi0
#     xp=np.array(bi)
#     print('2:',np.sum(xp == 1),len(bi))
#     newtime = time.time()
#     print('3:', (newtime - oldtime))
