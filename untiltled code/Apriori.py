#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import itertools as its

def pop(inlist,poplist):
    if len(poplist)==0:return inlist
    for popcell in poplist:
        for cell in inlist:
            if set(popcell) < set(cell):#子集包含比较用set(tuple)

                inlist.remove(cell)
                continue#在for遍历里不要删除列表内容，或者倒序，或者复制列表list[：]就是一种复制
    return inlist


def loadData(inData):
    tempData=[]

    tupleData=[]
    strData=[]
    for cell0 in inData:
        cell=sorted(cell0)#要排序避免重复
        #print('ce:',cell)
        strlist=sorted(list(map(str,cell)))#不管是不是数字全部整成字符串

        strData.append(tuple(strlist))
        for item in cell:

            if not str(item) in tempData:
                tempData.append(str(item))
                tupleData.append(tuple(str(item)))
    tempData.sort()
    tupleData.sort()#要排序避免重复
    outData=''.join(tempData)
    #print('ou:',outData,'\n',tupleData)
    return outData,tupleData,strData




def scanD(inData,per):
    ld=len(inData)
    #Data=makestr(inData)
    #print(Data)
    newdic={}
    poplist=[]
    apop=[]
    newlist=[]
    num=0
    tempData,Data0,strData=loadData(inData)

    for j in range(1,ld+1):
        if j==1:
            templist=Data0
        else:

            orinlist=list(its.combinations(tempData,j))#返回的是元组值


            templist=pop(orinlist,poplist)#删掉不合格数据后,去查是否包含该子集
        if not templist:
            return newdic#newlist
        tl=len(templist)


        for lnl in templist:

            num=0
            for dnl in strData:

                if set(lnl) <= set(dnl):
                    num+=1
            if num>=per*ld:
                newlist.append([lnl,float(num/ld)])
                newdic[lnl]=float(num/ld)
            else:
                apop.append(lnl)
        poplist=apop
    print('1:',newdic)
    return newdic#newlist


def calcConf(ali,minConf=0.7):
    donelist=[]
    for keys in ali:
        lk = len(keys)
        if lk > 1 and (keys not in donelist):
            for n in range(1,lk):
                iters = its.combinations(keys, n)
                Hkey = set(next(iters))
                #print('h:',Hkey,keys)
                while True:
                    try:
                        alist=list(set(keys) - Hkey)
                        alist.sort()
                        ckey = tuple(alist)#元组和列表内元素排列顺序不同则不同，而集合则不会
                        #print('ck:', ckey,keys)
                        per = ali[keys] / (ali[ckey])
                        if per >= minConf:
                            print(list(ckey),'--->',list(Hkey),':',per)
                        Hkey = set(next(iters))
                    except StopIteration:
                        break
            donelist.append(keys)
            #print('d:',donelist,keys)

if __name__=='__main__':
    indata=[[1,3,4],[2,3,5],[5,2,3,1],[2,5]]
    aliinput=scanD(indata,0.5)
    print(aliinput)
    calcConf(aliinput,0.7)






