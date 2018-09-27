#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun

import sqlite3
import re
import jieba
import warnings
import time
import numpy as np
import jieba
from sklearn.externals import joblib
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
oldtime = time.clock()
# from gensim.models import Word2Vec
from gensim.models import KeyedVectors
sql_add='./xy_zh_en.db'
print('Use 122g embeddings')
w2v_model='./news_12g_baidubaike_20g_novel_90g_embedding_64.bin'
try:
    model= KeyedVectors.load_word2vec_format(w2v_model,binary=True)
except Exception as e:
    print('err1:', e)
# filepath=r'C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\stopword.txt'
filepath='./stopword.txt'
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)
def out_num(instr):
    outstr = re.sub("[^\D]", "", instr)#去除数字
    return outstr


def normalize(name):
    return name.capitalize()

def strip_cap(alist):
    olist=[]
    for item in alist:
        try:
            cel = item.strip().capitalize()

        except:
            cel = item
        olist.append(cel)
    return olist
def standar(astr):
    if len(astr) > 0:
        if '_' in astr:
            cel = list(astr.split('_'))

            # print('00:',cel)
            rm_null(cel)
            en_out = strip_cap(cel)
            # print('11:',en_out)
            en_input = '_'.join(en_out)

        elif ' ' in astr:
            cel2 = list(astr.split(' '))
            rm_null(cel2)
            en_out2 = strip_cap(cel2)
            en_input = '_'.join(en_out2)
        else:
            en_input = astr.strip()
    else:
        en_input = astr
        print('22:', en_input)
    return en_input
def find_from_0(instr,cursor):
    sql = 'select en  from zh_en_0 where (zh like ?) '
    input_data=out_num(instr).strip()
    res = cursor.execute(sql, (input_data,))
    # res = cursor.execute(sql, (wx,))
    tempx = res.fetchall()
    if len(tempx)>0:
        # print('0:',tempx,tempx[0][0],type(tempx[0][0]))
        return tempx[0][0]#is a str
    else:

        return False
def find_from_dict(instr,cursor):
    sql = 'select en  from zh_en_prior2 where (zh like ?) '
    input_data = out_num(instr).strip()
    res = cursor.execute(sql, (input_data,))
    tempx = res.fetchall()
    if len(tempx) > 0:
        # print('0:',tempx,tempx[0][0],type(tempx[0][0]))
        return tempx[0][0]#is a str
    else:
        return False

def find_from_1(instr,cursor):
    sql = 'select en  from zh_en_prior1 where (zh like ?) '
    input_data = out_num(instr).strip().upper()
    res = cursor.execute(sql, (input_data,))
    tempx = res.fetchall()
    if len(tempx) > 0:
        # print('0:',tempx,tempx[0][0],type(tempx[0][0]))
        return tempx[0][0]#is a str
    else:
        return False
def normalize(name):
    return name.capitalize()
def concat(lis):
    en_out = list(map(normalize, lis))
    en_result = '_'.join(en_out)
    return en_result
def dele_stop_word(alist):
    stopwords = stopwordslist(filepath)
    # print('st:',stopwords)
    tstr = []
    for word in alist:
        sw=word.strip().lower()
        if sw not in stopwords:
            if word != '\t':
                tstr.append(word.strip())
    rm_null(tstr)
    # print('y:',tstr)
    return tstr
def deal_data(instr,cursor):#分词
    command = 'select * from fenci'
    sql = command
    res = cursor.execute(sql)
    tempx = res.fetchall()
    fenci = []
    if tempx:
        for x in tempx:
            if x not in fenci:
                fenci.append(x[0])
    fenci_set = set(fenci)
    jieba.load_userdict(fenci_set)

    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    data = []
    line = re.sub(r, '', instr)#去除符号
    outstr = re.sub("[^\D]", "", line)
    item=list(jieba.cut(outstr.strip()))
    rm_null(item)
    # data=dele_stop_word(item)

    return item

def find_word(instr,cursor):#no jieba because already done
     #判断是否是全字母：instr
    temp_instr=instr
    temp_instr1=instr
    result = re.sub(r'[A-Za-z]', '',temp_instr )
    result1 = re.sub(r'[0-9]', '', temp_instr1)
    if len(result)==0 or len(result1)==0:
        return instr
    if find_from_0(instr,cursor):#第一个表没有，找字典表，再没有找最后一个表
        return find_from_0(instr,cursor)
    else:
        if find_from_dict(instr,cursor):
            return find_from_dict(instr,cursor)
        else:
            if find_from_1(instr,cursor):
                return find_from_1(instr,cursor)
            else:
                # return find_from_w2v(instr)
                return ''

def deep_data(instr):
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    data = []
    line = re.sub(r, '', instr)  # 去除符号
    outstr = re.sub("[^\D]", "", line)
    item = list(jieba.cut(outstr.strip(),cut_all=True))

    rm_null(item)
    if instr in item:
        item.remove(instr)
        if len(item)==0:
            item.append(instr)

    # data=dele_stop_word(item)

    return item
def rm_duplicate(alist):
    out_data=[]
    for item in alist:
        if item.strip() not in out_data:
            out_data.append(item.strip())
        # print('3:',out_data)
    rm_null(out_data)
    return out_data
def find_from_w2v(instr,model):
    index = model.wv.index2word
    out_data=[]
    if instr in index:
        rela_word = model.most_similar(instr,topn=3)#is a list
        # print('te6:',rela_word)
        for xw in rela_word:
            out_data.append(xw[0])
        return out_data
def single_find(instr,model,clist,cursor):
    out_str=[]
    c_str=[]
    m_str=[]
    for char in instr:
        c_str.append(char)
        for xx in clist:
            if char in xx:
                m_str.append(char)
    for item in c_str:
        if item in m_str:
            c_str.remove(item)
    for char in c_str:
        if find_word(char,cursor) and find_word(char,cursor) not in out_str:
            out_str.append(find_word(char,cursor).capitalize())
            # print('te5:',out_str)
        else:
            rela_char=find_from_w2v(char,model)
            # print('te6:', rela_char)
            if rela_char:
                if len(rela_char) > 0:
                    data_out = ''
                    for xx in rela_char:
                        if find_word(xx,cursor) and find_word(xx,cursor) not in data_out:
                            data_out = find_word(xx,cursor)
                            return data_out
                    if data_out == '':
                        for xx in rela_char:
                            data_out = single_find(xx, model,clist,cursor)
                            if len(data_out) > 0:
                                return data_out
            return ''
    return ('_'.join(out_str))
def from_w2c_next(inlist,model,clist,cursor):
    if inlist:
        if len(inlist)>0:
            data_out=''
            for xx in inlist:
                xfw=find_word(xx,cursor)
                if xfw and xfw not in data_out:
                    data_out=find_word(xx,cursor)
                    return data_out
        # else:
        #     return ''

            if data_out=='':
                for xx in inlist:
                    data_out=single_find(xx,model,clist,cursor)
                    if len(data_out)>0:
                        return data_out

    return ''
def move_char(alist,i):
    for n in range(i):
        lth=99
        xlh=''
        for x in alist:
            if len(x)<lth:
                lth=len(x)
                xlh=x
        alist.remove(xlh)
    return alist
def create_shor(alist):#缩短单词
    relist=[]
    for xx in alist:
        ind=alist.index(xx)
        if len(xx) > 4:
            alist[ind] = alist[ind][0:3]
    #     if len(xx) < 3:
    #         relist.append(xx)
    # for it in relist:
    #
    #     alist.remove(it)
    return alist
def get_shorter(astr):#去重复单词
    i=0
    nlist=list(astr.split('_'))
    alist=[]
    for xa in nlist:
        if xa not in alist:
            alist.append(xa)
    tpstr = '_'.join(alist)
    # print('quchong0:', tpstr)
    alist=create_shor(alist)
    nwstr = '_'.join(alist)

    # print('quchong:',nwstr)
    while len(nwstr)>30:
        i+=1
        alist = list(tpstr.split('_'))
        alist=move_char(alist,i)
        # print('mc:',alist,i)
        alist = create_shor(alist)
        # print('cs:', alist)
        nwstr = '_'.join(alist)
        # print('yang:',nwstr,i)
        if len(nwstr)<30:
            break
            # return nwstr

    return nwstr
def dsc(astr,cursor):#make sentence shorter
    alist=list(astr.split('_'))
    alist=dele_stop_word(alist)
    sql = 'select jc  from get_shorter where (zh like ?) '
    for i in range(len(alist)):
        alist[i]=alist[i].capitalize()
        res = cursor.execute(sql, (alist[i],))
    # res = cursor.execute(sql, (wx,))
        tempx = res.fetchall()
        if len(tempx) > 0:
            alist[i]=tempx[0][0]
        # print('0:',tempx,tempx[0][0],type(tempx[0][0]))
    alist=rm_duplicate(alist)
    nstrn='_'.join(alist)
    # print('nrt:',nstrn)
    if len(nstrn)<30:
        return nstrn
    else:
        nstrx=get_shorter(nstrn)
        nst = list(nstrx.split('_'))
        nlst=rm_duplicate(nst)
        str_out='_'.join(nlst)
        # print('yangn:',nstrx)
        return str_out
def put_in_Db(alist,tb_name,cursor):#当有新内容时更新数据库,alist 中包含list
    # init(tb_name)
    i=2
    h=0
    for row in alist:#row is a list,row[0] is a str,rows1 is a list
        if row:
            cell=row[0].strip().upper()
            cel=out_num(cell)
            cel=out_num(cell)
            en=row[1].strip()
            sql = 'insert into '+tb_name+' VALUES(?,?) '
            try:
                cursor.execute(sql,(cel,en))

            except Exception as e :
                # print('err:',e)
                h+=1
    print('unique is {}'.format(h))

def check_dp_list(alist,clist):
    temp=[]
    addt=[]
    for xx in alist:
        for cel in clist:
            if xx in cel and xx not in temp:
                temp.append(xx)
            if cel in xx:
                xt=re.sub(cel,'',xx)
                if xt not in addt and xt not in clist:
                    addt.append(xt)
                if xx not in temp:
                    temp.append(xx)
                # print('in2:',temp)

    for ite in temp:
        alist.remove(ite)
    for xy in addt:
        alist.append(xy)
    return alist

def do_trans(instr,conn,model=None):
    '''do the translation job'''
    # instr=out_num(instr.strip())
    cursor = conn.cursor()
    instr=instr.upper()
    finded=[]
    if 'B2B' in instr:
        instr=instr.strip()
    else:
        instr=out_num(instr)
    result=[]
    if len(instr)>0:
        if find_from_0(instr,cursor):
            return find_from_0(instr,cursor)#先去表1找
        else:#找不到了，分词
            str_list=deal_data(instr,cursor)#is a list
            # print('te0:',str_list)
            for item in str_list:
                if find_word(item,cursor)!='' and find_word(item,cursor) not in result:
                    finded.append(item)
                    result.append(find_word(item,cursor))
                    # print('te1:',result,finded)
                else:
                    dp_list=deep_data(item)
                    dp_list.sort(key=lambda x: len(x),reverse=True)
                    if len(finded)>0:

                        dpt_li=check_dp_list(dp_list,finded)
                    else:
                        dpt_li=dp_list
                    # print('te2:', dpt_li,dp_list)
                    for dpic in dpt_li:
                        if find_word(dpic,cursor) != '' and find_word(dpic,cursor) not in result:
                            finded.append(dpic)
                            result.append(find_word(dpic,cursor))
                    # print('te3:', result,finded)
                    if len(finded)>0:
                        dpt_li = check_dp_list(dpt_li, finded)
                    # print('te31:', dpt_li, finded)
                    for pic in dpt_li:
                        xsingle=single_find(pic,model,finded,cursor)
                        if xsingle!='' and xsingle not in result:
                            finded.append(pic)
                            # print('xsing:',xsingle)
                            result.append(xsingle)
                            # print('te4:', result,finded)
                        else:
                            rela_char = find_from_w2v(pic, model)
                            xw2c=from_w2c_next(rela_char,model,finded,cursor)
                            if xw2c!='' and xw2c not in result:
                                # print('xw2c:',xw2c)
                                finded.append(pic)
                                result.append(xw2c)
                            # print('te5:', result,finded)



        # print('6:',result)
        if len(result)>0:
            if type(result) == list:
                result=dele_stop_word(result)
                result=rm_duplicate(result)
                result = '_'.join(result)
            if type(result) == str:
                result=list(result.split('_'))
                result = dele_stop_word(result)
                result = rm_duplicate(result)
                result = '_'.join(result)
            if len(result)>29:
                result=dsc(result,cursor)
            return result

        else:
            return ''
        # print('_'.join(result))
    else:
        return instr

def out_stander(astr):
    if isinstance(astr,str):
        olis=list(astr.split('_'))
        rm_null(olis)
        ostr=standar(olis)
        return ostr
    if isinstance(astr,list):
        astr=astr[0]
        olis = list(astr.split('_'))
        rm_null(olis)
        ostr = '_'.join(olis)
        return ostr

def persis_input(input_str,model):#中英文翻译执行接口
    '''input a chinese str and output an english str'''
    conn = sqlite3.connect(sql_add)
    astr=input_str
    ostr=do_trans(astr,conn,model)
    conn.commit()
    out_en=standar(ostr)
    conn.close()
    return out_en

# 下面是分类部分
def init(tb_name,conn):
    sql_init1='drop table if EXISTS '+tb_name
    sql_init2='''create table '''+tb_name+''' (zh text PRIMARY KEY,en INT )'''
    cursor=conn.cursor()
    cursor.execute(sql_init1)
    cursor.execute(sql_init2)
    conn.commit()
def init_sp_tb(conn):
    sql_init1 = 'drop table if EXISTS sampl_tb'
    sql_init2 = '''create table sampl_tb (src text,src_tb text,src_col text,tgt_tb text )'''
    cursor = conn.cursor()
    cursor.execute(sql_init1)
    cursor.execute(sql_init2)
    conn.commit()

def out_en(astr):
    outstr = re.sub("[a-zA-Z]", "", astr)
    outstr=outstr.strip()
    return outstr
def get_en(astr):
    outstr = re.sub("[^a-zA-Z]", "", astr)
    outstr = outstr.strip().upper()
    return outstr
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)
def clean_input(instr):#only for new input
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    line = re.sub(r, '', instr)
    outstr = re.sub("[^\D]", "", line)
    outstr=out_en(outstr)
    return outstr
def put_in(filepath,tb_name,conn):#file csv put into Db
    import csv
    cursor=conn.cursor()
    # init(tb_name)
    csvFile = open(filepath, "r",encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    rows1=[]
    rows2=[]
    rows3=[]
    i=2
    h=0
    for row in reader:#row is a list,row[0] is a str,rows1 is a list
        if row:
            cell=row[0].strip().upper()
            # cel=out_num(cell)
            cel=cell
            en=row[1].strip()
            sql = 'insert into '+tb_name+' VALUES(?,?) '
            try:
                cursor.execute(sql,(cel,en))

            except Exception as e :
                # print('err:',e)
                h+=1
    print('unique is {}'.format(h))
    csvFile.close()
    conn.commit()
    cursor.close()

def add_tb(tb_name,astr,conn):
    cursor = conn.cursor()
    sql = 'insert into ' + tb_name + ' VALUES(?,?) '
    try:
        cursor.execute(sql, (astr, 1))
    except Exception as e:
        print('err:', e)

    conn.commit()
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)
    return lis
def out_num(instr):
    outstr = re.sub("[^\D]", "", instr)
    return outstr
def del_stop(alist):
    # filepath = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\stopword.txt'
    filepath='./stopword.txt'
    def stopwordslist(filepath):
        stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
        return stopwords
    stopwords = stopwordslist(filepath)
    # print('st:',stopwords)
    tstr = []
    for word in alist:
        sw = word.strip().lower()
        if sw not in stopwords:
            if word != '\t':
                wword=word.strip().upper()
                # wnstr=out_num(wword)
                wnstr=wword
                tstr.append(wnstr)
    rm_null(tstr)
    return tstr#is a list
def like_fill(astr,cursor):#fenci create list只分词及一般处理
    import numpy as np
    import re
    command = 'select * from fenci'
    sql = command
    res = cursor.execute(sql)
    tempx = res.fetchall()
    fenci = []
    if tempx:
        for x in tempx:
            if x not in fenci:
                fenci.append(x[0])
    fenci_set = set(fenci)
    jieba.load_userdict(fenci_set)
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    src_tb_word = re.sub(r, '', astr)
    cutlist = list(jieba.cut(src_tb_word))
    # cutlist = del_stop(cutlist)

    return cutlist
def read_fr_db(tb_name,astr,cursor):#输入查询的表名和名称,返回一个np的矩阵，用了tolist最后是数组
    command='select cell from '+tb_name
    sql = command
    res=cursor.execute(sql)
    tempx = res.fetchall()
    astr=astr.strip().upper()
    if tempx:
        lth=len(tempx)
        out_list=np.zeros(lth)
        cell_list = [x[0].strip().upper() for x in tempx]
        if astr=='':
            return out_list.tolist()
        if tb_name=='Db_src':
            astr=get_en(astr)
            if astr in cell_list:
                i = cell_list.index(astr)
                out_list[i] = 1.
        else:
            stlist=like_fill(astr,cursor)#input a str output a jieba list
            for st in stlist:
                if st in cell_list:
                    i = cell_list.index(st)
                    out_list[i] = 1.
    else:
        print('no such column')

    fi_list=out_list.tolist()
    return fi_list
def deal_new_samp(astr,cursor):#处理一个新的名称，产生一个分词后的数组，且字数大于2
    command = 'select * from fenci'
    sql = command
    res = cursor.execute(sql)
    tempx = res.fetchall()
    fenci = []
    if tempx:
        for tx in tempx:  # is a tuple
            fc=tx[0].strip()
            if fc not in fenci:
                fenci.append(fc)
        fenci_set=set(fenci)
    out_list=[]
    alist=like_fill(astr,cursor)
    for al in alist:
        if len(al)>1 or al in fenci:
            out_list.append(al)
    return out_list
def add_samptb(conn,tb,alist):
    cursor=conn.cursor()
    sql = 'insert into ' + tb + ' VALUES(?,?,?,?) '
    try:
        cursor.execute(sql, (alist[0],alist[1],alist[2],alist[3]))
    except Exception as e:
        print('err:', e)

    conn.commit()
def add_new_samptb(conn,source=None):#source should be a list[src,src_tb,src_col,tgt]用于新增的分类
    cursor=conn.execute()
    if source:
        if len(source)>4:
            for x in range(4):
                if x==0:
                    data=get_en(source[x])
                    add_tb('Db_src',data,conn)
                if x==1:
                    data_list=deal_new_samp(source[x],cursor)
                    for dl in data_list:
                        add_tb('Db_tb',dl,conn)
                if x==2:
                    data_list = deal_new_samp(source[x],cursor)
                    for dl in data_list:
                        add_tb('Db_col', dl,conn)
            add_samptb(conn,'samp_tb',source)

    conn.commit()
def data_input(alist,cursor):#由输入的数组，根据已有的模型预测分类结果
    import numpy as np
    if len(alist)<3:
        print('You may input 3 strings as Source name,Source table name,Source table column')
        r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    try:
        src_word = get_en(alist[0])
        src_word = src_word.strip().upper()
        src_0=read_fr_db('Db_src',src_word,cursor)#is src list[0,0,..] 76x1
    except:
        src_0 = read_fr_db('Db_src', '',cursor)
        print('You may need Source Name')
    try:
        src_word = alist[1].strip()
        src_1 = read_fr_db('Db_tb',src_word,cursor)#is src_tb list[0,0,..] 566x1
    except:
        src_1= read_fr_db('Db_tb','',cursor)
        print('You may need Source Table Name')
    try:
        src_word = alist[2].strip()
        src_2 = read_fr_db('Db_col',src_word,cursor)
    except:
        src_2 =  read_fr_db('Db_col','',cursor)
        print('You may need Source Column Name')
    union = src_0+ src_1 + src_2
    return union
def like_data_input(alist,cursor):#由样本表建模
    import numpy as np
    if len(alist)==4:
        r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
        try:
            src_word = get_en(alist[0])
            src_word = src_word.strip().upper()
            src_0=read_fr_db('Db_src',src_word,cursor)#is src list[0,0,..] 76x1
        except:
            src_0 = read_fr_db('Db_src', '',cursor)
        try:
            src_word = alist[1].strip()
            src_1 = read_fr_db('Db_tb',src_word,cursor)#is src_tb list[0,0,..] 566x1
        except:
            src_1= read_fr_db('Db_tb','',cursor)

        try:
            src_word = alist[2].strip()
            src_2 = read_fr_db('Db_col',src_word,cursor)# 2124
        except:
            src_2 =  read_fr_db('Db_col','',cursor)
        tgt_word = alist[3].strip().upper()

        if 'T00' in tgt_word  :
            tgt = [0]
        if 'T01' in tgt_word  :
            tgt = [1]
        if 'T02' in tgt_word  :
            tgt = [2]
        if 'T03' in tgt_word  :
            tgt = [3]
        if 'T04' in tgt_word  :
            tgt = [4]
        if 'T05' in tgt_word  :
            tgt = [5]
        if 'T06' in tgt_word  :
            tgt = [6]
        if 'T07' in tgt_word  :
            tgt = [7]
        if 'T08' in tgt_word  :
            tgt = [8]
        if 'T09' in tgt_word  :
            tgt = [9]
        if 'T10' in tgt_word  :
            tgt = [10]
        if 'T99' in tgt_word  :
            tgt = [11]
        if 'REF' in tgt_word  :
            tgt = [12]
        union = src_0+ src_1 + src_2+tgt
    return union

def jieba_cut(astr,cursor):
    command = 'select * from fenci'
    sql = command
    res = cursor.execute(sql)
    tempx = res.fetchall()
    fenci = []
    if tempx:
        for x in tempx:
            if x not in fenci:
                fenci.append(x[0])
    fenci_set=set(fenci)
    jieba.load_userdict(fenci_set)
    # jieba.load_userdict(r"E:\兴业银行\中文翻译英文最终数据集\切词时用\分词库.txt")
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    astr=astr.strip()
    ostr=re.sub(r, '', astr)
    olist=list(jieba.cut(ostr))
    olist=rm_null(olist)
    zh_out = ' '.join(olist)
    return zh_out
def samp_tb(cursor):
    command = 'select * from samp_tb'
    sql = command
    res = cursor.execute(sql)
    tempx = res.fetchall()
    train_data=[]
    if tempx:
        for tx in tempx:#is a tuple

            train_data.append(like_data_input(list(tx),cursor))
    # print('0:',type(train_data),train_data[0])#是个列表中列表
    return train_data#列表中列表
def create_model(model_path,cursor):

    train_data=samp_tb(cursor)
    from sklearn.ensemble import RandomForestClassifier as Rfc
    from sklearn.preprocessing import OneHotEncoder
    import pandas as pd
    from sklearn.utils import shuffle
    shuf_data = shuffle(train_data)
    tr_x=[x[:-1] for x in shuf_data]

    train_y_ = [[y[-1]] for y in shuf_data]
    # print('2:',train_y_[0],type(train_y_[0]))
    ohe = OneHotEncoder()
    ohe.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
    label_name = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T99', 'REF']
    tr_y = ohe.transform(train_y_).toarray()#这个输入必须是ohe.fit里格式
    clf = Rfc(random_state=0)  # oob_score
    # model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\classify model\yang_Rf_model.pkl'
    clf.fit(tr_x, tr_y)
    # print('train score is {0}'.format(clf.score(tr_x, tr_y)))
    joblib.dump(clf, model_path)
def get_rown(conn):#检测样本和特征有没有增加，如果增加修改记录表
    tb_name=['Db_src','Db_tb','Db_col','samp_tb']
    rowli = []

    cursor = conn.cursor()
    for x in tb_name:
        command = 'select count(*) from ' + x
        sql = command
        res = cursor.execute(sql)
        tempx = res.fetchall()

        if tempx:
            rown=tempx[0][0]
            rowli.append(rown)
    # print('tt:',rowli)
    get_sql='select * from mark'
    getres = cursor.execute(get_sql)
    existed = getres.fetchall()
    if existed:
        ex_temp=list(existed[0])
    ex_temp=list(map(int,ex_temp))
    # print(ex_temp)
    if rowli!=ex_temp:#数据有变化，从新训练
        for x in range(4):
            sqls = 'update mark set '+tb_name[x]+'='+str(rowli[x])
            res=cursor.execute(sqls)
            conn.commit()
        model_path = './classify_model.pkl'
        create_model(model_path,cursor)

def do_class(alist,model_path,cursor):
    union=[data_input(alist,cursor)]
    label_name = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T99', 'REF']
    clf = joblib.load(model_path)
    pre_out=clf.predict(union)
    prob_out=clf.predict_proba(union)
    # print(pre_out)
    for item in pre_out:
        ind = np.where(item == 1)
    id=ind[0].tolist()
    if len(id)>0:
        return label_name[id[0]]
        # print('pro:',prob_out[id[0]][0][1],)
    else:
        return 'Null'
def classify_port(input_list):#先执行samp_tb()从样本表制作输入数据，create_model后生成模型,再执行do_class 可以进行输入的分类
    sql_classify = './Db_classify.db'
    conn = sqlite3.connect(sql_classify)
    cursor=conn.cursor()
    model_path = './classify_model.pkl'
    do_class(input_list,model_path,cursor)
    conn.close()
def train_model_port(mulist):

    sql_classify = './Db_classify.db'
    conn = sqlite3.connect(sql_classify)
    for alist in mulist:
        if alist:
            add_new_samptb(conn,alist)
    get_rown(conn)
    conn.close()

persis_input('你好',model)