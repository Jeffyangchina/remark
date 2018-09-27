#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import csv
import jieba
import re
import os
import jieba.analyse as jas
# 读取csv文件方式1
def rm_puc(line):
    from zhon.hanzi import punctuation as zh_puc
    from string import punctuation as en_puc
    line=re.sub("[%s]+" % en_puc, "", line)
    line=re.sub("[%s]+" % zh_puc, "", line)

    from zhon.hanzi import punctuation as zh_puc
    from string import punctuation as en_puc
    line=re.sub("[%s]+" % en_puc, "", line)
    line=re.sub("[%s]+" % zh_puc, "", line)
    return line
def rm_same(alist):
    outlis=[]
    for item in alist:
        if item not in outlis:
            outlis.append(item)
    return outlis
def rm_space(astr):
    out_=re.sub(' ','',astr)
    return out_
def rm_null(lis):
    for cel in lis:
        if len(cel)==0:
            lis.remove(cel)
    return lis
def jieba_cut(astr):
    jieba.load_userdict(r"E:\兴业银行\中文翻译英文最终数据集\切词时用\fenci.txt")

    astr=astr.strip()
    ostr=rm_puc(astr)

    olist=list(jieba.cut(ostr))
    olist=rm_null(olist)

    return olist
def eng_cut(astr):
    item=astr.strip()
    xlist = list(item.split("_"))
    xlist=rm_null(xlist)
    return xlist
def deal_data():#分词
    jieba.load_userdict(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\补充.txt")
    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior0.csv", "r",encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    r = '[’!"#$%&\－()（*+,-./:：、＋（）;<=>?@[\\]^_`{|}~]+'

    data = []
    for item in reader:
        # print('00:',item,item[0])
        if len(item)>0:
            xen=''
            xzh=''

            line= item[1].strip()
            line = re.sub(r, '',line)

            xen=' '.join(list(item[1].split("_")))
            rm_null(xen)
            line2=item[0].strip()
            # xt=list(reversed(jas.extract_tags(item[0])))
            xzh = ' '.join(list(jieba.cut(line2)))


            data.append([xzh]+[xen])
        # print('11:',data)

    # 从列表写入csv文件
    csvFile2 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior0_new.csv", 'w', newline='',encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile2)
    m = len(data)
    for i in range(m):
        writer.writerow(data[i])
    csvFile2.close()

    csvFile.close()
def shuff():
    import numpy as np
    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\中英文.csv", "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    dataset=[]
    csvFile2 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\tr_xdata.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile2)
    csvFile3 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\tr_ydata.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer3 = csv.writer(csvFile3)

    csvFile4 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\dev_xdata.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer4 = csv.writer(csvFile4)
    csvFile5 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\dev_ydata.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer5 = csv.writer(csvFile5)
    csvFile6 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\te_xdata.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer6 = csv.writer(csvFile6)
    csvFile7 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\te_ydata.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer7 = csv.writer(csvFile7)
    for x in reader:
        dataset.append(x)

    np.random.shuffle(dataset)
    # print('ss:',dataset[44])
    lt=len(dataset)
    # print('0:',lt)
    tr_data=dataset[:int(0.8*lt)]
    dev_data = dataset[int(0.8 * lt):int(0.9 * lt)]
    te_data = dataset[int(0.9 * lt):]
    for xx in tr_data:

        writer2.writerow([xx[0]])#方法中的参数是list类型，必须是writer.writerow(['abcd'])才可以，不然就会被逗号分开
        writer3.writerow([xx[1]])
    for xx1 in dev_data:

        writer4.writerow([xx1[0]])
        writer5.writerow([xx1[1]])
    for xx2 in te_data:
        writer6.writerow([xx2[0]])
        writer7.writerow([xx2[1]])
    csvFile2.close()
    csvFile3.close()
    csvFile4.close()
    csvFile5.close()
    csvFile6.close()
    csvFile7.close()
    csvFile.close()


def get_vocal(filepath):#统计次数，用字典

    import os
    # rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'
    rootdir=filepath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = []
    data_dic={}
    # # print('0:',list)
    for i in range(0, len(lists)):

        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'vocab_'+lists[i] )
        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型


            for item in reader:
                # print('0:',item)
                for x in item:
                    # print('1:',x)
                    if len(x)>1:
                        xx=x.split(' ')
                        for cell in xx:
                            if cell in data_dic:
                                data_dic[cell]+=1
                            else:
                                data_dic[cell]=1
                    else:
                        if x in data_dic and x !='':
                            data_dic[x] += 1
                        else:
                            data_dic[x] = 1
                    # print('2:',data_dic)
            csvFile.close()


    for key in data_dic:
        data.append(key + ',' + str(data_dic[key]))

    csvFile2 = open(r"C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\test_new.csv", 'w', newline='',
                                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile2)

    for i in data:
        writer.writerow([i])#必须是list
    csvFile2.close()

       # 你想对文件的操作
def modify_all():#遍历
    import os
    rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'

    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = []
    # # print('0:',list)
    for i in range(0, len(lists)):

        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, lists[i]+'_new')
        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile2 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer = csv.writer(csvFile2)


            for item in reader:
                data = ""
                input_data = []
                for xx in item:
                    data+=xx+' '
                input_data.append((data+'.'))
                writer.writerow(input_data)
            csvFile.close()
            csvFile2.close()
def check_name(lis):
    if type(lis)== str:
        if 'T0' in lis or 'T99' in lis:
            return False
        else:
            return True
    else:

        for x in lis:
            if 'T0' in x or 'T99' in x:
                return False
            else:
                return True


def make_map():#要排除有表代码的如T00这种开头，因为是以单词字数来匹配.

    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\模型数据集\dev\dev_xdata_new.csv", "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    csvFile2 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\模型数据集\dev\dev_ydata_new.csv", "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)  # 返回的是迭代类型
    dataset = []
    csvFile3 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\模型数据集\dev\concat.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile3)
    csvFile4 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\模型数据集\dev\dev_xdata_rest.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer1 = csv.writer(csvFile4)
    csvFile5 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\模型数据集\dev\dev_ydata_rest.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile5)
    rows1 = [row for row in reader]
    rows2 = [row for row in reader2]
    lth=len(rows1)

    for i in range (lth):
        x1=rows1[i]
        x2=rows2[i]
        data1 = []
        data2 = []
        data3 = []
        if len(x1)==len(x2) :
            if check_name(x2):
                for n in range(len(x1)):
                    data1.append([x1[n],x2[n]])
        # else:
        #     # data2.append(x1)
        #     # data3.append(x2)
        else:
            # print('1:', x1)
            writer1.writerow(x1)

            # print('2:', x2)
            writer2.writerow(x2)
        if len(data1)>0:
            for x in data1:
                # print('0:',x)
                writer.writerow(x)

    csvFile.close()
    csvFile2.close()
    csvFile3.close()
    csvFile4.close()
    csvFile5.close()


def make_concat():#去头尾空格,大小写统一
    import os
    rootdir = r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\模型数据集\concat"

    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = []
    data1=[]
    data2=[]
    data_dic = {}
    csvFile1 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\模型数据集\concat\sumall.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer1 = csv.writer(csvFile1)
    csvFile2 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\训练集\模型数据集\concat\conflic.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile2)
    # # print('0:',list)
    for i in range(0, len(lists)):

        path = os.path.join(rootdir, lists[i])

        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型

            for item in reader:#is a list
                # print('0:',item)
                x1=item[0].strip()
                x2=item[1].strip().lower()
                if x1 in data_dic:
                    if x2 in data_dic[x1]:
                        continue
                    else:
                        data_dic[x1].append(x2)
                else:
                    data_dic[x1]=[x2]


            csvFile.close()
    # print('0:',data_dic)
    for key in data_dic:
        # print('2:',data_dic[key],key)
        if len(data_dic[key])>1:
            data_dic[key].insert(0, key)
            writer2.writerow(data_dic[key])
        elif len(data_dic[key])==1:
            # print('1:',data_dic[key].insert(0, key))
            data_dic[key].insert(0, key)
            writer1.writerow(data_dic[key])

    csvFile2.close()
    csvFile1.close()

def make_map_db():

    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior0_new.csv", "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    rows1=[]
    rows2=[]

    dataset = []
    csvFile3 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior0_cout1.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile3)
    csvFile4 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior0_cout_zh.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer1 = csv.writer(csvFile4)
    csvFile5 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\prior0_cout_en.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile5)
    for row in reader:
        rows1.append(row[0])
        rows2.append(row[1])

    lth=len(rows1)

    for i in range (lth):
        x1=list(rows1[i].split(' '))
        x2=list(rows2[i].split(' '))
        if i==2:
            print('1:',x1,len(x1))
        data1 = []
        data2 = []
        data3 = []
        if len(x1)==len(x2):
            for n in range(len(x1)):
                data1.append([x1[n],x2[n]])
        # else:
        #     # data2.append(x1)
        #     # data3.append(x2)
        else:
            # print('1:', x1)如果发现写入是一个个字符则是因为没有输入列表格式
            writer1.writerow(x1)

            # print('2:', x2)
            writer2.writerow(x2)
        if len(data1)>0:
            for x in data1:
                # print('0:',x)
                writer.writerow(x)

    csvFile.close()

    csvFile3.close()
    csvFile4.close()
    csvFile5.close()
def extract_csv():#提取需要人工标注的单词
    import os
    rootdir = r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\未处理\to deal with"
    write_zh = r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\未处理\extract_zh.csv"
    f1 = open(write_zh, 'w', newline='')
    writer = csv.writer(f1)
    #
    # write_en = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\中英文语料库\词典\_en.txt'
    # f2 = open(write_en, 'w')

    lists = os.listdir(rootdir)
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])

        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型

            input_data=[]
            for item in reader:#a list
                for i in range (len(item)):
                    if item[i]!='----' and item[i] not in input_data:
                        input_data.append(item[i])
                        writer.writerow([item[i]])




            csvFile.close()
    f1.close()
def find_num(instr):
    outstr = re.sub("[^\D]", "", instr)
    outstr1=re.sub('[a-z]','',outstr.lower())
    return outstr1
def out_num(instr):
    # outstr = re.sub("[^\D]", "", instr)#
    outstr=re.sub('[0-9]+$','',instr)#只匹配末尾的数字
    return outstr

def dropout_num():#去除数字
    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\未处理\extract_zh.csv", "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    dataset = []
    csvFile2 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\未处理\extract_zh_outnum.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile2)
    for item in reader:
        if len(item)>0:
            if len(find_num(item[0]))>0:
                writer2.writerow([item[0]])#如果写入csv时，把字符串拆开了，是因为写入是需要list格式


def normalize(name):
    return name.capitalize()


def standar(str):
    if '_' in str or ' ' in str:
        if '_' in str:
            cel = list(str.split('_'))
            # print('00:',cel)
            rm_null(cel)
            en_out = list(map(normalize, cel))
            # print('11:',en_out)
            en_input = '_'.join(en_out)

        if ' ' in str:
            cel2 = list(str.split(' '))
            rm_null(cel2)
            en_out2 = list(map(normalize, cel2))
            en_input = '_'.join(en_out2)
    else:
        en_input = str.capitalize()
    # print('22:', en_input)
    return en_input
def define_table(name):
    if 'T0' in name or 'T9' in name:
        return True
    else:
        return False
def rm(instr):#取出开头'_'
    indata=list(instr.strip().split('_'))
    rm_null(indata)
    en_out = list(map(normalize, indata))
    en_input = '_'.join(en_out)
    return en_input
def clean_sum_table():#去除数字\英文字段做下 常规处理 去重 单独提出表名
    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\中英文.csv", "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    dataset = []
    csvFile2 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\extract_of_中英文.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile2)
    csvFile3 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\table_name中英文.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer3 = csv.writer(csvFile3)
    csvFile4 = open(r"C:\Users\XUEJW\Desktop\兴业数据\xy_dataset\中对英\db\maybe_pingyin中英文.csv", 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer4 = csv.writer(csvFile4)
    dict_all={}
    w3=[]
    w4=[]
    for item in reader:
        inrow=[]
        if len(item)>1:
            # row1=out_num(item[0])
            row1=item[0].strip()
            row2=item[1].strip()
            row2 = rm(row2)
            inrow.append(row1)
            inrow.append(row2)
            # row2=standar(out_num(item[1]))
            if define_table(row2):
                if row1 not in w3:
                    w3.append(row1)
                    writer3.writerow(inrow)
            else:

                # print('0:', row2)

                if '_' not in row2:
                    if row1 not in w4:
                        w4.append(row1)
                        writer4.writerow(inrow)

                # print('1:',row2)
                elif row1 not in dict_all:#同样的中文如果有不同的英文，取频率最大的那个翻译
                    dict_all[row1]=[[row2,1]]
                else:
                    wn=1
                    for icel in dict_all[row1]:
                        if icel[0]==row2:
                            icel[1]+=1
                            wn=2
                            break
                    if wn==1:
                        dict_all[row1].append([row2, 1])


    for dicel in dict_all:
        lnum=0
        lstr=''
        in_data=[]
        for  ddcel in dict_all[dicel]:#ddcel is a 2 dim list
            # print('3:',ddcel)
            if ddcel[1]>lnum:
                lnum=ddcel[1]
                lstr=ddcel[0]
        in_data.append(dicel)
        in_data.append(lstr)

        # print('2:',in_data)

        writer2.writerow(in_data)#如果写入csv时，把字符串拆开了，是因为写
    csvFile.close()
    csvFile2.close()
    csvFile3.close()
    csvFile4.close()
# clean_sum_table()
def rm_duplicate(alist):
    out_data=[]
    for item in alist:
        if item.strip() not in out_data:
            out_data.append(item.strip())
        # print('3:',out_data)
    rm_null(out_data)
    return out_data
def write_in(astr,alist,writer):
    for xx in alist:
        if len(xx)>0:
            writer.writerow([astr,xx])
def extract_ftable(filename):#提取有用数据
    add=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\\'
    path=add+filename+'.csv'
    newpath = add + filename + '_type.csv'
    # print('0:',path)
    try:
        csvFile = open(path, "r", encoding='UTF-8')
        csvFile2 = open(newpath, 'w', newline='',
                        encoding='UTF-8')  # 设置
    except:
        csvFile = open(path, "r", encoding='GB2313')
        csvFile2 = open(newpath, 'w', newline='',encoding='GB2313')

    reader = csv.reader(csvFile)  # 返回的是迭代类型
    dataset = []
    rows0 =[]
    rows1 =[]
    rows2 =[]
    rows3 =[]


    writer2 = csv.writer(csvFile2)
    for row in reader:
        rows0.append(row[0].strip())
        rows1.append(row[1].strip())
        rows2.append(row[2].strip())
        rows3.append(row[3].strip())

    # print('1:',rows1)
    row0_=rm_duplicate(rows0)
    row1_ =rm_duplicate(rows1)
    row2_ =rm_duplicate(rows2)
    row3_ =rm_duplicate(rows3)
    write_in('src_col',row0_,writer2)
    write_in('src',row1_,writer2)
    write_in('tgt_tb',row2_,writer2)
    write_in('src_tb',row3_,writer2)
    # print('2:',rows1)
    csvFile.close()
    csvFile2.close()
# filename='T01_feature'
# extract_ftable(filename)
def uni_type(filepath):#去重 去数字 统一大写
    import os
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    rootdir = filepath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):

        path = os.path.join(rootdir, lists[i])

        uni_path = os.path.join(rootdir, 'uniq_' + lists[i])
        if os.path.isfile(path):
            temp = []
            try:
                csvFile = open(path, "r", encoding='UTF-8')
            except:
                print('encode error')
            reader = csv.reader(csvFile)  # 返回的是迭代类型

            csvFile3 = open(uni_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer1 = csv.writer(csvFile3)
            for item in reader:
                # print('0:',item)
                if item:
                    istr = re.sub(r, '', item[0])
                    istr=out_num(istr)
                    wor=istr.strip().upper()
                    if wor not in temp:
                        temp.append(wor)
            temp=del_stop(temp)
            for xx in temp:

                writer1.writerow([xx])
            csvFile.close()

            csvFile3.close()

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
def del_stop(alist):
    filepath = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\stopword.txt'

    stopwords = stopwordslist(filepath)
    # print('st:',stopwords)
    tstr = []
    for word in alist:
        sw = word.strip().lower()
        if sw not in stopwords:
            if word != '\t':
                wword=word.strip().upper()
                wnstr=out_num(wword)
                tstr.append(wnstr)
    rm_null(tstr)

    return tstr#is a list
def vocab_num(filepath):  # 统计次数，用字典,

    import os
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'
    jfc_add=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    rootdir = filepath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = []
    data_dic = {}
    # # print('0:',lists)
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'vocab_' + lists[i])
        if os.path.isfile(path):
            temp_dic={}
            try:
                csvFile = open(path, "r", encoding='UTF-8')
            except:
                csvFile = open(path, "r", encoding='GB2313')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile2 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer = csv.writer(csvFile2)

            for item in reader:
                # print('0:',item)
                if item:
                    istr = re.sub(r, '', item[0])

                    cutlist=list(jieba.cut(istr))
                    cutlist=del_stop(cutlist)
                    cutlist= list(map(normalize, cutlist))
                    # cutlist=list(jas.extract_tags(istr))
                    for xc in cutlist:
                        if xc not in data_dic:
                            data_dic[xc]=1
                        else:
                            data_dic[xc]+=1
                        if xc not in temp_dic:
                            temp_dic[xc] = 1
                        else:
                            temp_dic[xc] += 1
            for xd in temp_dic:
                if len(xd)>0:
                    writer.writerow([xd,temp_dic[xd]])

            csvFile.close()
            csvFile2.close()


    sum_path=filepath+'\\sum_vocab' + '.csv'
    print('3:',sum_path)
    csvFile4 = open(sum_path, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile4)
    for key in data_dic:
        writer2.writerow([key,data_dic[key]])
    csvFile4.close()
def find_same_word(filepath):
    import os
    rootdir = filepath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = []
    data_dic = {}
    # # print('0:',lists)
    for i in range(0, len(lists)):

        path = os.path.join(rootdir, lists[i])

        if os.path.isfile(path):
            temp_dic = {}
            try:
                csvFile = open(path, "r", encoding='UTF-8')
            except:
                csvFile = open(path, "r", encoding='GB2313')
            reader = csv.reader(csvFile)  # 返回的是迭代类型

            for item in reader:
                # print('0:',item)
                if item:

                    cpwd=item[0].strip().upper()
                    cpwd=out_num(cpwd)
                    if cpwd not in data:
                        data.append(cpwd)

            csvFile.close()

    sum_path = filepath + '\\sum_vocab' + '.csv'
    print('3:', sum_path)
    csvFile4 = open(sum_path, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile4)
    for key in data_dic:
        writer2.writerow([key, data_dic[key]])
    csvFile4.close()
def out_en(astr):
    outstr = re.sub("[a-zA-Z]", "", astr)
    outstr=outstr.strip()
    outstr=rm_space(outstr)
    return outstr
def vocab_sum(filepath):  # 统计所有次数，用字典,

    import os
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'
    jfc_add=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    rootdir = filepath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = []
    data_dic = {}
    # # print('0:',lists)
    for i in range(0, len(lists)):

        path = os.path.join(rootdir, lists[i])

        if os.path.isfile(path):
            temp_dic={}
            try:
                csvFile = open(path, "r", encoding='UTF-8')
            except:
                csvFile = open(path, "r", encoding='GB2313')
            reader = csv.reader(csvFile)  # 返回的是迭代类型

            for item in reader:
                # print('0:',item)
                if item:
                    istr = re.sub(r, '', item[0])
                    cutlist=list(jieba.cut(istr))
                    cutlist=del_stop(cutlist)
                    cutlist= list(map(normalize, cutlist))
                    # cutlist=list(jas.extract_tags(istr))
                    for xc in cutlist:
                        if xc not in data_dic:
                            data_dic[xc]=1
                        else:
                            data_dic[xc]+=1


            csvFile.close()



    sum_path=filepath+'\\sum_vocab' + '.csv'
    print('3:',sum_path)
    csvFile4 = open(sum_path, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile4)
    for key in data_dic:
        writer2.writerow([key,data_dic[key]])
    csvFile4.close()
def make_one_word(filepath):  # 制作输入数据，去掉单个中文字,

    import os
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'

    rootdir = filepath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = []
    data_dic = {}
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'one_word_' + lists[i])
        if os.path.isfile(path):
            temp_dic={}
            try:
                csvFile = open(path, "r", encoding='UTF-8')
            except:
                csvFile = open(path, "r", encoding='GB2313')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile2 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer = csv.writer(csvFile2)

            for item in reader:
                # print('0:',item)
                if item:
                    istr = item[0].strip().upper()
                    istr=out_en(istr)
                    # cutlist=del_stop(cutlist)可以
                    if len(istr)>1:
                        writer.writerow([istr])

            csvFile.close()
            csvFile2.close()
def make_dnn_model(fpath):#作模型，搜集所有的词输入,改用从数据库读取
    import os

    model_path=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\model_input.csv'
    csvFile2 = open(model_path, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile2)
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    src_data=[]

    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        if os.path.isfile(path):
            print('0:',path)
            src_data=[]
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            for item in reader:
                if item:
                    src_data.append(item[0].strip().upper())
            print('1:',len(src_data))
            writer.writerow(src_data)
            csvFile.close()
    csvFile2.close()
def fill_matrix(alist,astr):#fenci fill the matrix
    import numpy as np
    import re
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # astr=out_num(astr)
    astr=astr.strip()
    src_tb_word = re.sub(r, '', astr)
    cutlist = list(jieba.cut(src_tb_word))
    cutlist = del_stop(cutlist)
    zero_matrix = np.zeros(len(alist))
    for tcell in cutlist:
        if tcell in alist:
            h = alist.index(tcell)
            zero_matrix[h] = 1.
    return zero_matrix
def fill_one_label(alist,astr):#用序号

    tgt_tb=astr.strip()
    if  tgt_tb in alist:
        h = alist.index(tgt_tb)
        tgt_label = h
    else:
        print(tgt_tb)
    return tgt_label
def fill_one_hot_label(alist,aint):#用one hot
    from sklearn.preprocessing import OneHotEncoder
    new_list=[]
    for i in range(len(alist)):
        new_list.append([i])
    ohe = OneHotEncoder()
    ohe.fit(new_list)
    tr_y = ohe.transform([[aint]]).toarray()
    tr_out=tr_y[0].tolist()
    return tr_out

def deep_typer_input(fpath):#细分类时制作训练数据，onehot,标签是573
    import numpy as np
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'
    jfc_add = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\model_input.csv'
    csvFile2 = open(model_path, "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)
    suml=[]
    src=[]
    src_tb=[]
    src_col=[]

    for xx in reader2:

        if xx:
            suml.append(xx)
    src=suml[0]
    src_tb=suml[1]
    src_col=suml[2]
    tgt=suml[3]
    csvFile2.close()
    print('lth:',len(src),len(src_tb),len(src_col),len(tgt))#78 565+2120 =2763
    src_0 = np.zeros(len(src))
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件

    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path=os.path.join(rootdir, 'onehot_input_' + lists[i])
        if os.path.isfile(path):
            data_in = []
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            for item in reader:
                if item:
                    src_0 = np.zeros(len(src))
                    src_word=item[0].strip().upper()
                    if src_word in src:
                        i = src.index(src_word)
                        src_0[i] = 1.
                    temp_word=item[1].strip()
                    src_1=fill_matrix(src_tb,temp_word)
                    col_word=item[2].strip()
                    src_2=fill_matrix(src_col,col_word)
                    tgt_word=item[3].strip()
                    src_3 = fill_matrix(tgt,tgt_word)
                templist=src_0.tolist()+src_1.tolist()+src_2.tolist()

                if len(templist)>0:
                    if templist not in data_in:
                        data_in.append(templist)
                        union=templist+src_3.tolist()
                        writer3.writerow(union)
            csvFile3.close()
            csvFile.close()
def one_label_input(fpath):#细分类时制作训练数据，标签(表名)是不分词，每个为一类，总类反而更多
    import numpy as np
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'
    jfc_add = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\one_label\model_input.csv'
    csvFile2 = open(model_path, "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)
    # model_path3 = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\one_label\model_label_one_word.csv'
    model_path3=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\训练集开始集\确定类后再预测细分类\T00\label model\T00 tgt_tb.csv'#单独对每细类做label one hot
    csvFile4 = open(model_path3, "r", encoding='UTF-8')
    reader4 = csv.reader(csvFile4)
    suml=[]
    src=[]
    src_tb=[]
    tgt=[]
    i=1
    for xx in reader2:

        if xx:
            suml.append(xx)
    src=suml[0]
    src_tb=suml[1]
    src_col=suml[2]
    for xt in reader4:
        if i<3:
            print('xt:',xt,xt[0])
            i+=1
        if len(xt[0])>0:
            tgt.append(xt[0].strip())

    csvFile2.close()
    print('lth:',len(src),len(src_tb),len(src_col),len(tgt))#lth: 76 566 2124 785
    src_0 = np.zeros(len(src))
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path=os.path.join(rootdir, 'one_hot_label_' + lists[i])
        if os.path.isfile(path):
            data_in = []
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            for item in reader:
                if item:
                    src_0 = np.zeros(len(src))
                    src_word=item[0].strip().upper()
                    if src_word in src:
                        i = src.index(src_word)
                        src_0[i] = 1.
                    temp_word=item[1].strip()
                    src_1=fill_matrix(src_tb,temp_word)
                    col_word=item[2].strip()
                    src_2=fill_matrix(src_col,col_word)
                    tgt_word=item[3].strip()
                    src_3 = fill_one_label(tgt,tgt_word)
                    src_3_one_hot=fill_one_hot_label(tgt,src_3)
                templist=src_0.tolist()+src_1.tolist()+src_2.tolist()

                if len(templist)>0:
                    if templist not in data_in:
                        data_in.append(templist)
                        # union=templist+[src_3]
                        union=templist+src_3_one_hot
                        writer3.writerow(union)
            csvFile3.close()
            csvFile.close()
def label_one_dim(fpath):#提取所有目标表名,不把表名拆开
    import numpy as np

    model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\model_label_one_word.csv'
    csvFile2 = open(fpath, "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)
    csvFile3 = open(model_path, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer3 = csv.writer(csvFile3)
    suml=[]
    tgt_tb=[]
    i = 1
    for xx in reader2:

        if xx:

            tgt_t=xx[3]
            if i<3:
                print(tgt_t)
                i+=1
            if len(tgt_t)>0 and tgt_t not in tgt_tb:
                tgt_tb.append(tgt_t)
                writer3.writerow([tgt_t])

    csvFile2.close()
    csvFile3.close()
def deal_zh(astr):
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # temp=out_num(astr.strip())不能去数字 有B2B表
    temp_word = re.sub(r, '', astr)
    return temp_word.strip()


def temp_tiny_class_deal(fpath):#处理文字，去重去空格,去除尾部数字

    suml=[]
    i=1
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        if '.csv' not in lists[i]:

            name=lists[i]
            print('ss:',name)
        new_path=os.path.join(rootdir, 'cleaned_' + lists[i])
        if os.path.isfile(path):
            data_in = {}
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            i=1
            vocab_li=[]
            for item in reader:
                if item:
                    src0=item[0].strip().upper()
                    src1=item[1].strip()
                    src2=item[2].strip()
                    src2=out_num(src2)
                    src3=item[3].strip()

                    if len(src0)!=0 or len(src1)!=0 or len(src2)!=0:
                        if 'ETL加载作业名' not in src2 and 'ETL业务日期' not in src2 and 'ETL加载作业名' not in src2 and 'ETL处理时间戳' not in src2 and ')(' not in src0 and 'ETL首次插入日期' not in src2:
                            src_sum=[src0,src1,src2,src3]
                            if src_sum not in vocab_li:
                                vocab_li.append(src_sum)
            for xx in vocab_li:
                writer3.writerow(xx)
            csvFile3.close()
            csvFile.close()
                   #  src=item[1].strip()
                   #  src=out_num(src)
                   #  src=rm_space(src)
                   #  src_=out_en(src)
                   #  src_f=rm_space(src_)
                   # # 只是处理文字不提取汉字
                   #  tgt=item[0].strip()
                   #  tgt=out_num(tgt)
                   #  tgt_=out_en(tgt)
                   #  tgt_f=rm_space(tgt)


def tiny_class_deal(fpath):#处理文字，去重去空格,去除尾部数字

    suml=[]
    i=1
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        if '.csv' not in lists[i]:

            name=lists[i]
            print('ss:',name)
        new_path=os.path.join(rootdir, 'cleaned_' + lists[i])
        if os.path.isfile(path):
            data_in = {}
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            i=1
            vocab_li=[]
            for item in reader:

                if item:

                    # src=item[1].strip()
                    # src=out_num(src)
                    # src=rm_space(src)
                    # src_=out_en(src)
                    # src_f=rm_space(src_)
                    # 只是处理文字不提取汉字
                    # tgt=item[0].strip()
                    # tgt=out_num(tgt)
                    # tgt_=out_en(tgt)
                    # tgt_f=rm_space(tgt)

                    tgt=item[0].strip()
                    tgt=rm_puc(tgt)
                    tgt = out_num(tgt)
                    tgt_cut=jieba_cut(tgt)
                    for xx in tgt_cut:
                        if xx not in vocab_li:
                            vocab_li.append(xx)

                    # if len(src_f)>0 and len(tgt_f)>0 and src!=tgt:
                    #     if tgt not in data_in:
                    #         data_in[tgt]=[src]
                    #     elif src not in data_in[tgt]:
                    #         data_in[tgt].append(src)
            print('0:',len(vocab_li))
            for x in vocab_li:
                if len(x)>0:
                    writer3.writerow([x])
            csvFile3.close()
            csvFile.close()
def cut_src_tb(astr):#fenci fill the matrix
    import numpy as np
    import re
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # astr=out_num(astr.strip())
    src_tb_word = re.sub(r, '', astr)
    cutlist = list(jieba.cut(src_tb_word))
    cutlist = del_stop(cutlist)#去中英文数字
    return cutlist

def tiny_class_cut_src_tb(fpath):
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'double_cut_' + lists[i])
        if os.path.isfile(path):
            data_in = []
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            inlist = []
            for item in reader:
                if item:
                    src = item[0].strip().upper()
                    # src_tb_temp = item[1].strip()
                    # src_col = item[2].strip()
                    src_tb=item[1].strip()
                    src_col_temp=item[2].strip()
                    tgt_tb = item[3].strip()
                    # if len(src_tb_temp)>0:
                    #     src_tb_list=cut_src_tb(src_tb_temp)
                    #     for xx in src_tb_list:
                    #         if len(xx)>1:
                    #             templist = [src, xx, src_col, tgt_tb]
                    #             writer3.writerow(templist)
                    # else:
                    #     writer3.writerow([src, src_tb_temp, src_col, tgt_tb])
                    if len(src_col_temp)>0:
                        src_col_list=cut_src_tb(src_col_temp)
                        for xx in src_col_list:
                            if len(xx)>1:
                                templist=[src,src_tb,xx,tgt_tb]
                                writer3.writerow(templist)
                    else:
                        writer3.writerow([src,src_tb,src_col_temp,tgt_tb])
            csvFile3.close()
            csvFile.close()
def cut_srctb_onelabel(fpath):#细分类时制作训练数据，标签(表名)是不分词，每个为一类，总类反而更多
    import numpy as np
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'
    jfc_add = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\one_label\model_input.csv'
    csvFile2 = open(model_path, "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)
    model_path3 = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\one_label\model_label_one_word.csv'
    csvFile4 = open(model_path3, "r", encoding='UTF-8')
    reader4 = csv.reader(csvFile4)
    suml=[]
    src=[]
    src_tb=[]
    tgt=[]
    i=1
    for xx in reader2:

        if xx:
            suml.append(xx)
    src=suml[0]
    src_tb=suml[1]
    src_col=suml[2]
    for xt in reader4:
        if i<3:
            print('xt:',xt,xt[0])
            i+=1
        tgt.append(xt[0].strip())

    csvFile2.close()
    csvFile4.close()
    print('lth:',len(src),len(src_tb),len(src_col),len(tgt))#lth: 76 566 2124 784
    src_0 = np.zeros(len(src))
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path=os.path.join(rootdir, 'one_label_' + lists[i])
        if os.path.isfile(path):
            data_in = []
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            for item in reader:
                if item:
                    src_0 = np.zeros(len(src))
                    src_word=item[0].strip().upper()
                    if src_word in src:
                        i = src.index(src_word)
                        src_0[i] = 1.
                    temp_word=item[1].strip()
                    src_1=fill_matrix(src_tb,temp_word)
                    col_word=item[2].strip()
                    src_2=fill_matrix(src_col,col_word)
                    tgt_word=item[3].strip()
                    src_3 = fill_one_label(tgt,tgt_word)
                templist=src_0.tolist()+src_1.tolist()+src_2.tolist()

                if len(templist)>0:
                    if templist not in data_in:
                        data_in.append(templist)
                        union=templist+[src_3]
                        writer3.writerow(union)
            csvFile3.close()
            csvFile.close()

def trans_concate(slis,blis):
    import itertools
    nlis=[]
    out_lis=[]
    #itertools.combinations产生所有子集，无序
    sth=len(slis)
    bth=len(blis)
    if sth>bth:
        ndis=sth-bth
        for n in range(bth):
            nlis.append(n)
        sub_set=list(itertools.combinations(nlis,ndis))
        if len(sub_set)>0:
            templist = []
            for item in sub_set:
                templist=[]
                for x in range(ndis):
                    templist.append(item[x])
                scel=0
                for cell in range(bth):
                    if cell in templist:
                        out_lis.append([blis[cell],'_'.join(slis[scel:scel+2])])
                        scel=scel+2
                    else:
                        out_lis.append([blis[cell],slis[scel]])
                        scel+=1
        else:
            if len(blis)>0:
                out_lis.append([blis[0],'_'.join(slis)])
    else:
        ndis = bth -sth
        for n in range(sth):
            nlis.append(n)
        sub_set = list(itertools.combinations(nlis, ndis))
        if len(sub_set) > 0:
            for item in sub_set:
                templist = []
                for x in range(ndis):
                    templist.append(x)
                scel = 0
                for cell in range(sth):
                    if cell in templist:
                        out_lis.append([''.join(blis[scel:scel + 2]), slis[cell]])
                        scel = scel + 2
                    else:
                        out_lis.append([blis[scel], slis[cell]])
                        scel += 1
        else:
            out_lis.append([blis + slis])
    out_lis=rm_same(out_lis)
    return out_lis


def comblist(doublist):#组合相同中文不同英文
    comdic={}
    out_lis=[]
    conf_lis=[]
    for xx in doublist:
        if type(xx[0])==str:
            if xx[0] not in comdic:#dict 不支持key为list类型
                comdic[xx[0]]=[xx[1]]
            else:
                if xx[1]!=comdic[xx[0]]:
                    comdic[xx[0]].append(xx[1])
        else:
            pass

    for key in comdic:
        if len(comdic[key])>1:
            conf_lis.append([key,comdic[key]])
        else:
            out_lis.append([key,comdic[key][0]])
    return out_lis,conf_lis
def col_trans(tr_set):
    rootdir = tr_set
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    r = '[’!"#$%&\－()（*+,-./:：/”“。（）‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    for i in range(0, len(lists)):
        data = []
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'new_' + lists[i])
        new_path1 = os.path.join(rootdir, 'conf_' + lists[i])
        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型

            csvFile1 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer1 = csv.writer(csvFile1)
            csvFile2 = open(new_path1, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer2 = csv.writer(csvFile2)
            conlis=[]
            doubtlis=[]
            for item in reader:
                if item:
                    if len(item)>1:
                        line = item[1].strip()
                        xen =list(line.split("_"))
                        en_out = list(map(normalize, xen))
                        xen=rm_null(en_out)
                        xlen=len(xen)
                        line2 = item[0].strip()
                        line = re.sub(r, '', line2)

                        # xt=list(reversed(jas.extract_tags(item[0])))
                        xzh = list(jieba.cut(line))
                        rm_null(xzh)
                        zlen=len(xzh)
                        if xlen==zlen:
                            for x in range(xlen):
                                conlis.append([xzh[x], xen[x]])
                        else:
                            tlis=trans_concate(xen,xzh)
                            if tlis:
                                doubtlis+=tlis
            conlis=rm_same(conlis)
            pri0_lis,conf_lis=comblist(conlis)
            doubtlis=rm_same(doubtlis)
            newdol=[]
            # print('y1:',conlis)
            for xx in pri0_lis:
                writer1.writerow(xx)
            for yy in doubtlis:
                if yy not in pri0_lis:
                    newdol.append(yy)
            # print('y3:',newdol)

            conf_lis2,conf_lis3=comblist(newdol)
            new_conf=conf_lis+conf_lis2+conf_lis3
            for xy in new_conf:
                writer2.writerow(xy)
            csvFile.close()
            csvFile2.close()
            csvFile1.close()


def make_sum_dataset(tr_set):  # 制作总的训练集，测试集,
    from pandas import DataFrame
    from sklearn.utils import shuffle
    rootdir = tr_set
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件

    for i in range(0, len(lists)):
        data = []
        path = os.path.join(rootdir, lists[i])
        new_path1 = os.path.join(rootdir, 'tr_' + lists[i])
        new_path2 = os.path.join(rootdir, 'te_' + lists[i])
        if os.path.isfile(path):
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型

            csvFile3 = open(new_path1, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            csvFile4 = open(new_path2, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer4 = csv.writer(csvFile4)
            for item in reader:
                if item:
                    if len(item[0])!=0 or len(item[1])!=0 or len(item[2])!=0:
                        data.append(item)

            csvFile.close()
            sdata = DataFrame(data)
            print('lx1:',len(sdata))
            shuf_data = shuffle(sdata)
            lt_x = len(sdata) * 0.1
            put_lt = int(lt_x)
            if put_lt == 0:
                put_lt = 1
            # print('3:',len(data),type(data),len(sdata),type(sdata))

            tr_= shuf_data[:-put_lt].values

            te_= shuf_data[-put_lt:].values

            for xx in tr_:
                writer3.writerow(xx)
            for yy in te_:
                writer4.writerow(yy)
            csvFile3.close()
            csvFile4.close()
def get_model(path):
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    suml=[]
    for xx in reader:
        if len(xx)>0:
            for x in xx:
                if x.strip() not in suml:
                    suml.append(x.strip())

    csvFile.close()
    return suml


def new_one_hot_label(file_path):
    import numpy as np
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    # rootdir = r'C:\Users\XUEJW\Desktop\兴业数据\一万句zh_en\test\1\2'
    # tr_path = os.path.join(file_path, 'tr')
    # te_path = os.path.join(file_path, 'te')
    fpath=os.path.join(file_path, 'dataset')
    tgt_tb_ = os.path.join(file_path, 'label model\\tgt_tb.csv')
    src_tb_ = os.path.join(file_path, 'label model\\src_tb.csv')
    src_col_ = os.path.join(file_path, 'label model\\src_col.csv')
    jfc_add = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    src_tb = get_model(src_tb_)
    src_col = get_model(src_col_)
    tgt=get_model(tgt_tb_)
    print('lth:',  len(src_tb), len(src_col), len(tgt))  # lth: 每个类都不一样
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'one_hot_label_' + lists[i])
        if os.path.isfile(path):
            data_in = []
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            for item in reader:
                if item:

                    temp_word = item[1].strip()
                    src_1 = fill_matrix(src_tb, temp_word)
                    col_word = item[2].strip()
                    src_2 = fill_matrix(src_col, col_word)
                    tgt_word = item[3].strip()
                    src_3 = fill_one_label(tgt, tgt_word)#返回序号，整数然后才能作onehot
                    src_3_one_hot = fill_one_hot_label(tgt, src_3)
                templist =  src_1.tolist() + src_2.tolist()

                if len(templist) > 0:
                    if templist not in data_in:
                        data_in.append(templist)
                        # union=templist+[src_3]
                        union = templist + src_3_one_hot
                        writer3.writerow(union)
            csvFile3.close()
            csvFile.close()

def ten_class_one_hot_ipnut(file_path):  # 10大类时制作训练数据，
    import numpy as np
    r = '[’!"#$%&\－()（*+,-./:：”“。‘、，【】＋（）;<=>?@[\\]^_`{|}~]+'
    fpath=os.path.join(file_path, 'all data')
    tr_path = os.path.join(file_path, 'tr data')
    te_path = os.path.join(file_path, 'te data')
    model_path = os.path.join(file_path, 'label model\\model_input.csv')

    jfc_add = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    csvFile2 = open(model_path, "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)
    suml = []
    src = []
    src_tb = []
    tgt = []
    i = 1
    for xx in reader2:

        if xx:
            suml.append(xx)
    src = suml[0]
    src_tb = suml[1]
    src_col = suml[2]
    bclass=suml[4]

    csvFile2.close()

    print('lth:', len(src), len(src_tb), len(src_col), len(bclass))  # lth: 76 566 2124 784
    src_0 = np.zeros(len(src))
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path = os.path.join(rootdir, 'one_hot_' + lists[i])
        if os.path.isfile(path):
            data_in = []
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            for item in reader:
                if item:
                    src_0 = np.zeros(len(src))
                    src_word = item[0].strip().upper()
                    if src_word in src:
                        i = src.index(src_word)
                        src_0[i] = 1.
                    temp_word = item[1].strip()
                    src_1 = fill_matrix(src_tb, temp_word)
                    col_word = item[2].strip()
                    src_2 = fill_matrix(src_col, col_word)
                    tgt_word = item[3].strip()
                    src_3 = fill_one_label(bclass, tgt_word)
                    src_3_one_hot = fill_one_hot_label(bclass, src_3)

                templist = src_0.tolist() + src_1.tolist() + src_2.tolist()

                if len(templist) > 0:
                    if templist not in data_in:
                        data_in.append(templist)
                        union = templist + src_3_one_hot
                        writer3.writerow(union)
            csvFile3.close()
            csvFile.close()
def delet_right_one():
    csvFile = open(r'E:\兴业银行\中文翻译英文最终数据集\trans\final_sum_col_trans.csv', "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    csvFile1 = open(r'E:\兴业银行\中文翻译英文最终数据集\tb_name\new_new2_tb_trans.csv', "r", encoding='UTF-8')
    reader1 = csv.reader(csvFile1)  # 返回的是迭代类型
    dataset = []
    csvFile2 = open(r'E:\兴业银行\中文翻译英文最终数据集\trans\new_new_new2_tb_trans.csv', 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile2)
    for item in reader:
        if item:
            if len(item)>0:
                dataset.append(item[0])
    csvFile.close()
    for item in reader1:
        if item:
            if len(item)>0:
                if item[0] not in dataset:
                    writer2.writerow(item)  # 如果写
    csvFile2.close()
    csvFile1.close()
# delet_right_one()
def delwith_tb():

    csvFile = open(r'E:\兴业银行\中文翻译英文最终数据集\切词时用\cut_word_sum.csv', "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    csvFile2 = open(r'E:\兴业银行\中文翻译英文最终数据集\切词时用\new_cut_word_sum.csv', 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile2)
    data=[]
    for item in reader:
        if item:
            try:
                line=item[0]
                if len(line)>1:
                    if line not in data:
                        data.append(line)
                        writer2.writerow([line])
            except:
                print(item)
    csvFile.close()
    csvFile2.close()
def delwith_srcb(root,name):#处理翻译参照表
    file_path=os.path.join(root, name)
    write_path=os.path.join(root, 'new_'+name)
    write_path1 = os.path.join(root, 'new_conf' + name)
    csvFile = open(file_path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    csvFile1 = open(write_path1, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer1 = csv.writer(csvFile1)
    csvFile2 = open(write_path, 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile2)
    data = []
    rows_en=[]
    rows_zh=[]
    for row in reader:
        if row:
            rows_zh.append(row[0])
            rows_en.append(row[1])
        else:
            print('err:',row)

    lth = len(rows_zh)
    print('src:',rows_zh[:2],rows_en[:2])
    for i in range(lth):

        x1 = jieba_cut(rows_zh[i])
        x2 = eng_cut(rows_en[i])
        data1 = []
        data2 = []
        data3 = []
        if len(x1) == len(x2):
            for n in range(len(x1)):
                data1.append([x1[n],x2[n]])
        else:
            # print('1:', x1)
            writer1.writerow([rows_zh[i],rows_en[i]])
    for xx in data1:
        writer2.writerow(xx)

    csvFile.close()
    csvFile1.close()
    csvFile2.close()
# delwith_srcb(r'E:\兴业银行\中文翻译英文最终数据集\对照表','srcb_Attribute.csv')
def make_tensor_input(fpath):
    import numpy as np

    jfc_add = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\分词库\fenci.txt'
    if os.path.isfile(jfc_add):
        jieba.load_userdict(jfc_add)
    model_path = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\model_input.csv'
    csvFile2 = open(model_path, "r", encoding='UTF-8')
    reader2 = csv.reader(csvFile2)
    suml=[]
    src=[]
    src_tb=[]
    src_col=[]

    for xx in reader2:

        if xx:
            suml.append(xx)
    src=suml[0]
    src_tb=suml[1]
    src_col=suml[2]
    # tgt=suml[3]
    csvFile2.close()
    print('lth:',len(src),len(src_tb),len(src_col))#78 565+2120 =2763
    src_0 = np.zeros(len(src))
    rootdir = fpath
    lists = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件

    for i in range(0, len(lists)):
        path = os.path.join(rootdir, lists[i])
        new_path=os.path.join(rootdir, 'tensor_input_' + lists[i])
        if os.path.isfile(path):
            src_data = []
            csvFile = open(path, "r", encoding='UTF-8')
            reader = csv.reader(csvFile)  # 返回的是迭代类型
            csvFile3 = open(new_path, 'w', newline='',
                            encoding='UTF-8')  # 设置newline，否则两行之间会空一行
            writer3 = csv.writer(csvFile3)
            for item in reader:
                if item:
                    src_0 = np.zeros(len(src))
                    src_word=item[0].strip().upper()
                    if src_word in src:
                        i = src.index(src_word)
                        src_0[i] = 1.
                    temp_word=item[1].strip()
                    src_1=fill_matrix(src_tb,temp_word)
                    col_word=item[2].strip()
                    src_2=fill_matrix(src_col,col_word)
                    tgt_word=item[3].strip().upper()
                    if tgt_word=='T00':
                        tgt=[0]
                    if tgt_word == 'T01':
                        tgt = [1]
                    if tgt_word == 'T02':
                        tgt = [2]
                    if tgt_word == 'T03':
                        tgt = [3]
                    if tgt_word == 'T04':
                        tgt = [4]
                    if tgt_word == 'T05':
                        tgt = [5]
                    if tgt_word == 'T06':
                        tgt = [6]
                    if tgt_word == 'T07':
                        tgt = [7]
                    if tgt_word == 'T08':
                        tgt = [8]
                    if tgt_word == 'T09':
                        tgt = [9]
                    if tgt_word == 'T10':
                        tgt = [10]
                    if tgt_word == 'T99':
                        tgt = [11]
                    if tgt_word == 'REF':
                        tgt = [12]



                union=src_0.tolist()+src_1.tolist()+src_2.tolist()+tgt
                writer3.writerow(union)
            csvFile3.close()
            csvFile.close()
def temp():
    csvFile = open(r'E:\yang_xy_test\ten class\train_sample_fr_tgt.csv', "r", encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    csvFile2 = open(r'E:\yang_xy_test\ten class\cleaned_train_sample_fr_tgt.csv', 'w', newline='',
                    encoding='UTF-8')  # 设置newline，否则两行之间会空一行
    writer2 = csv.writer(csvFile2)
    data=[]
    stopwords=stopwordslist(r'E:\yang_xy_test\ten class\stopword_zh_en.txt')
    for item in reader:
        if item:
            try:
                line=out_num(item[0]).upper()
                line=rm_space(line)
                pt=out_en(line)
                if line not in stopwords:
                    if line != '\t' and len(line)>0 and len(pt)>0:
                        if line not in data:
                            data.append(line)


            except:
                print(item)
    for xx in data:
        writer2.writerow([xx])
    csvFile.close()
    csvFile2.close()
# temp()
# delwith_tb()
# delet_right_one()
# col_trans(r'E:\兴业银行\中文翻译英文最终数据集\tb_name')
# new_one_hot_label(r'E:\yang_xy_test\T00')
# make_sum_dataset(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测')
# cut_srctb_onelabel(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\deep cut of src_tb')
# tiny_class_cut_src_tb(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\训练集开始集\with double cut dataset\tr')
# tiny_class_deal(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测')
# label_one_dim(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\2\train sum.csv')
filepath=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\总集\no en'
# deep_typer_input(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\deep cut of src_tb')#用于作onehot
# uni_type(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\ten classifty\dataset')
# vocab_num(filepath)
# vocab_sum(filepath)
# filepath=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\make one word'
# make_one_word(filepath)

# tiny_class_deal(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\ten classifty\dataset')
# make_sum_dataset(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\ten classifty\dataset')
# ten_class_one_hot_ipnut(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\ten classifty\dataset')


path=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input dataset\2'
# make_tensor_model(path)
# make_tensor_input(path)
# one_label_input(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\tiny classify\每个类下单独预测\训练集开始集\确定类后再预测细分类\T00')
def test():#用pandas读取数据，但是他做one hot 有个问题 是根据现有标签制作的

    import pandas as pd
    import numpy as np
    import operator
    from functools import reduce #做降维 unstack flatten
    tr_set = r'C:\Users\XUEJW\Desktop\yang_test\test.csv'
    test_file = r'C:\Users\XUEJW\Desktop\yang_test\test2.csv'
    # pwd = os.getcwd()
    # os.chdir(os.path.dirname(tr_set))
    train_data = pd.read_csv(tr_set,header=None)#不能有中文出现
    # os.chdir(os.path.dirname(test_file))
    test_data = pd.read_csv(test_file,header=None)
    # os.chdir(pwd)
    # labels1 = train_data.label.values
    # print('0:',labels1)
    # labels = []
    #
    # for i in labels1:
    #     z = np.zeros((1, 13))
    #
    #     z[0][i] = 1
    #
    #     labels.append(z[0])
    # print('1:', labels)
    from sklearn.utils import shuffle

    xdata=pd.concat([train_data,test_data,test_data,train_data])
    print('0:', xdata)
    pda=xdata.sample(frac=1)
    df=shuffle(xdata)
    print('00:', pda)
    print('000:', df)
    # num_data = train_data.shape[0]
    # print('2:', num_data )
    # train_x_ = train_data.iloc[:,0:-1].values
    # print('3:', train_x_)
    # train_y_=train_data.iloc[:,-1:].values
    # train_1=np.array(train_y_)
    # train_2 = np.array(train_y_).tolist()
    # train_y=reduce(operator.add,train_2)
    #
    # print('40:', train_1)
    # print('41:', train_2)
    #
    # print('4:', train_y)
    # from pandas.core.frame import DataFrame
    # print('43:', DataFrame(train_y))
    # dataSize = train_x_.shape[0]
    # one_hot=pd.get_dummies(train_y)
    # one_hot = one_hot.astype('float')
    # print('00:',one_hot)
    # test_x = test_data.values
    # train_x = []
# make_dnn_model(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\make model input')
# deep_typer_input(r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input onehot\2')
# lth: 76 566 2124 573
# test()
# tiny_class_deal(r'E:\yang_xy_test\ten class\vocab')
# temp_tiny_class_deal(r'E:\yang_xy_test\ten class\temp')
# temp()