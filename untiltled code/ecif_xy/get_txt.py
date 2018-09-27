#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun

import os

import time
import re
import copy

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
pick_zh= re.compile(u'[^\u4e00-\u9fa5]+')#排除非中文

def contain_zh(lis):
    '''
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    '''
    i=2
    for word in lis:
        # word = word.decode()
        if i==2:
            # print('y:',type(lis))
            i=3
        global zh_pattern
        match = zh_pattern.search(word)
        if match:
            return match
    return False

def from_book():
    add=r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\词典'
    write_zh=r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\词典\_zh.txt'
    f1 = open(write_zh, 'w')

    write_en=r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\词典\_en.txt'
    f2 = open(write_en, 'w')
    mark=0
    wm=0
    i=1
    for (root,dirs,files) in os.walk(add):
        for item in files:
            t1=0
            if_m=0
            slist=''
            if_dic={}
            then_dic={}
            with open(add+'\\'+item,'r+',encoding='utf-8') as f:
                if_dic = {}
                then_dic = {}
                fx=f.readlines()
                t1 = 0
                if_m = 0
                #print('0::',len(fx))
                for s in fx:# s is str
                    if contain_zh(s):
                        try:
                            f1.write(s)
                        except Exception as e:
                            print('err:', e)

                    else:
                        # if i< 3:
                        #     print('y:',s,len(s))
                        #     i += 1
                        if len(s)>1:#换行符也占一位
                            try:
                                f2.write(s)
                            except Exception as e:
                                print('err:',e)

    f1.close()
    f2.close()
def pick_one(lis):#多个翻译取最短那个
    r1 = '\(.*\) '#转义要
    r2 = ' \(.*\)'
    lth=float("inf")
    for cel in lis:
        cel = re.sub(r1, '', cel)
        cel = re.sub(r2, '', cel)
        cel=cel.strip()
        comp=cel.split(' ')
        if len(comp)<lth:
            lth=len(comp)
            out_str=cel
            celth=len(cel)
        if len(comp)==lth:
            if len(cel)<celth:
                celth=len(cel)
                out_str=cel
    return out_str
def pick_zh_out(stri):
    out_str=re.sub(pick_zh,'',stri)
    return out_str.strip()

def from_dict():
    add = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\词典'
    write_zh = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\zh_to_en.txt'
    f1 = open(write_zh, 'w')
    #
    # write_en = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\词典\_en.txt'
    # f2 = open(write_en, 'w')

    for (root,dirs,files) in os.walk(add):
        for item in files:
            row1=[]

            row2=[]
            with open(add+'\\'+item,'r+',encoding='utf-8') as f:
                fx = f.readlines()
                for x in fx:
                    zh=''
                    lis=list(x.strip().split(','))
                    # print('1:',lis)
                    if len(lis)>1:
                        if contain_zh(lis[0]):
                            pu=pick_one(lis[1:])
                            zh=lis[0]+','+pu+'\n'
                            # print('2:',pu,zh)
                            f1.write(zh)
def from_dict_en():
    add = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\未处理词典'
    write_zh = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\zh_to_en.txt'
    f1 = open(write_zh, 'w')
    #
    # write_en = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\词典\_en.txt'
    # f2 = open(write_en, 'w')

    for (root,dirs,files) in os.walk(add):
        for item in files:
            row1=[]

            row2=[]
            with open(add+'\\'+item,'r+',encoding='utf-8') as f:
                fx = f.readlines()
                for x in fx:
                    zh=''
                    lis=list(x.strip().split(','))
                    print('1:',lis)
                    if len(lis)>1:

                        for zcel in lis[1:]:
                            zh_in=pick_zh_out(zcel)
                            if len(zh_in)>0:

                                zh = zh_in+ ',' +lis[0]  + '\n'
                                print('2:',zh)
                                f1.write(zh)

