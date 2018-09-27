# #!/usr/bin/env python3.6
# # -*- coding: utf-8 -*-
# #@Author: Yang Xiaojun
# import os
# import tensorflow as tf
# #original is 32*32*3
# fixed_height=24
# fixed_width=24
# #train sets is 50000 test sets is 10000
# train_samples_per_epoch=50000
# test_samples_per_epoch=10000
# data_dir=r'C:\Users\XUEJW\Desktop\cifar-10-batches-py'#'latin1
# batch_size=128#128
#
# def read_cifar10(filename_queue):
#     class Image(object):
#         pass
#     image=Image()
#     image.height=32
#     image.width=32
#     image.depth=3
#     label_bytes=1
#     image_bytes=image.height*image.width*image.depth
#     Bytes_to_read=label_bytes+image_bytes
#     #这个读取文件也不是单纯的文件名就可以的，要用tf.train.string_input_producer导入输出队列中的才行
#     reader=tf.FixedLengthRecordReader(record_bytes=Bytes_to_read)#每次从文件读取固定长度，但是该集合的label在data前面
#     image.key,value_str=reader.read(filename_queue)#返回的都是字符串型tensor，当某一个文件读完时，该文件名会dequeue
#     value=tf.decode_raw(bytes=value_str,out_type=tf.uint8)#读取二进制文件，把字符串转成数值向量，每一个数值占一个字节uint8
#     image.label=tf.slice(input_=value,begin=[0],size=[label_bytes])#标签在前，先提取标签
#     #下面要提取图像数据了，有几个转换步骤，纬度转换主要是，因为数据集的纬度是深度*高度*宽度和我们的不符
#     data_mat=tf.slice(input_=value,begin=[label_bytes],size=[image_bytes])
#     data_mat=tf.reshape(data_mat,(image.depth,image.height,image.width))
#     transposed_value=tf.transpose(data_mat,perm=[1,2,0])#纬度对调
#     image.mat=transposed_value
#     return image
#
# def get_batch_samples(img_obj,min_samples_in_queue,batch_size,shuffle_flag):
#     '''tf.train.shuffle_batch()函数每次随机从读取多个文件中内容构成一个batch.
#     这个函数创建了一个shuffling queue,用于把tensors压入该队列
#     一个dequeue_many操作，用于根据队列中的数据创建一个batch
#     创建了一个queuerunner对象，用于启动一个进程压数据到队列
#     capacity参数用于控制shuffling queue的最大长度，就是队列中容量
#     min_after_dequeue参数表示进行一次dequeue操作后队列中元素的最小数量，可以用于确保batch中元素随机性，
#     num_threads参数用于指定多少个threads负责压tensors到队列，
#     enqueue_many参数用于表征是否tensors中每一个tensor 都代表一个样例
#     tf.train.batch()与之类似，只不过顺序地出队列，只能每次从一个data文件中读取batch,少了随机性'''
#     if shuffle_flag==False:
#         image_batch,label_batch=tf.train.batch(tensors=img_obj,batch_size=batch_size,
#                                                num_threads=4,capacity=min_samples_in_queue+3*batch_size)#没有了随机
#     else:
#         image_batch, label_batch = tf.train.shuffle_batch(tensors=img_obj, batch_size=batch_size,
#                                                   num_threads=4,min_after_dequeue=min_samples_in_queue, capacity=min_samples_in_queue + 3 * batch_size)
#
#         #tf.image_summary()已更新，输出预处理后图像的缓存对象，用于在session中写入到事件文件中
#         tf.summary.image('input_name',tensor=image_batch,max_outputs=6)#
#         return image_batch,tf.reshape(label_batch,shape=[batch_size])
# def preprocess_input_data():
# #这部分用于对训练数据集进行数据增强，通过增加数据集大小防止过拟合
#     filenames=[os.path.join(data_dir,'data_batch_%d'%i)for i in range(1,6)]
#     #filenames=[os.path.join(data_dir,'test_batch.bin')]#测试集
#     for f in filenames:#检验训练文件是否存在
#         if not tf.gfile.Exists(f):
#             raise ValueError('fail to find file:'+f)
#     filename_queue=tf.train.string_input_producer(string_tensor=filenames)#把文件名输出到队列中，作为整个data pipe的第一阶段
#     image=read_cifar10(filename_queue)#从文件名队列中读取一个tensor类型的图像
#     new_img=tf.cast(image.mat,tf.float32)
#     tf.summary.image('raw_input_image',tf.reshape(new_img,[1,32,32,3]))#输出预处理前图像的summary缓存对象
#     new_img=tf.random_crop(new_img,size=(fixed_height,fixed_width,3))#从原图像中切出指定大小
#     new_img=tf.image.random_brightness(new_img,max_delta=63)#随机调节亮度
#     new_img=tf.image.random_flip_left_right(new_img)#随机的左右翻转图像
#     new_img=tf.image.random_contrast(new_img,lower=0.2,upper=1.8)#对比度
#     final_img=tf.image.per_image_standardization(new_img)#目的是降低图像冗余性，尽量去除特征间相关性
#
#     min_samples_ratio_in_queue=0.4#用于确保读到的batch中样例的随机性
#     min_samples_in_queue=int(min_samples_ratio_in_queue*train_samples_per_epoch)
#     return get_batch_samples([final_img,image.label],min_samples_in_queue,batch_size,shuffle_flag=True)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
import pickle as pk
import os
import numpy as np
import queue

def load_cifar_batch(filename):
    #load single file
    with open(filename,'rb') as f:
        datadict=pk.load(f,encoding='latin1')
        X=datadict['data']
        Y=datadict['labels']
        X=X.reshape(10000,3,32,32)#.transpose(0,2,3,1).astype('float')
        Y=np.array(Y)
        return  X,Y

def load_cifar_all(root):
    xs=[]
    ys=[]
    for b in range(1,6):

        f=os.path.join(root,'data_batch_%d'%(b,))

        X,Y=load_cifar_batch(f)

        xs.append(X)

        ys.append(Y)

    Xtr=np.concatenate(xs)
    Xtr = Xtr.reshape(50000, 3, 32, 32).transpose(0,2,3,1).astype('float')#(50000,32,32,3)
    Ytr=np.concatenate(ys)#使变成行向量(50000,)
    del X,Y
    Xte,Yte=load_cifar_batch(os.path.join(root,'test_batch'))
    cXte,Yte=load_cifar_batch(os.path.join(root,'test_batch'))
    return Xtr,Ytr,Xte,Yte
def get_batch(file,batch_size,num,label=0):


    alist=[]

    for x in range(num*batch_size,(num+1)*batch_size):
        if label == 1:
            alist.append(file[x]* (1. / 255) - 0.5)
        else:
            alist.append(file[x])
    return np.array(alist)


#
data_dir=r'C:\Users\XUEJW\Desktop\cifar-10-batches-py\data_batch_1'
finame=r'C:\Users\XUEJW\Desktop\cifar-10-batches-py'
try:
    x,y,a,b=load_cifar_all(finame)
    #print(y[0])
    img=get_batch(y,10,1)

    print(':',img[0],img.shape)
except Exception as s:
    print('wrong',s)
# #