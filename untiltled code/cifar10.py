#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import tensorflow as tf
import readcifar10 as cf10
#
# height=cf10.fixed_height
# width=cf10.fixed_width
# train_samples_per_epoch=cf10.train_samples_per_epoch
# test_samples_per_epoch=cf10.test_samples_per_epoch
#
# moving_average_decay=0.9999#the decay to use for the moving average
# num_epochs_per_decay=350.0#衰减呈阶梯函数，控制衰减周期（阶梯宽度）
# learning_rate_decay_factor=0.1#学习率衰减因子
# initial_learning_rate=0.1#初始学习率
#
# def variable(name,shape,dtype,stddev,wd):
#     weight=tf.get_variable(name=name,shape=shape,initializer=tf.truncated_normal_initializer(stddev=stddev,dtype=dtype))
#     if wd is not None:
#         weight_decay=tf.multiply(tf.nn.l2_loss(weight),wd,name='weight_loss')
#
#         tf.add_to_collection(name='losses',value=weight_decay)
#     return weight
# def losses_summary(total_loss):
#     #通过使用指数衰减，来维护变量的滑动均值。当训练模型时，维护训练参数的滑动均值是有好处的，在测试过程中使用滑动参数比最终训练的参数值本身
#     average_op=tf.train.ExponentialMovingAverage(decay=0.9)#创建一个新的指数滑动均值对象
#     losses = tf.get_collection(key='losses')#从字典集合中返回关键字'losses'对应的所有变量，包括交叉熵和正则项损失项
#     maintain_averages_op=average_op.apply(losses+[total_loss])#维护变量的滑动均值，返回一个能够更新shadow variables的操作
#     for i in losses+[total_loss]:
#         tf.summary.scalar(i.op.name+'_raw',i)#保存变量到summary缓存对象，以便写入文件
#         tf.summary.scalar(i.op.name,average_op.average(i))#average()returns the shadow variable for a given variable
#     return maintain_averages_op#返回损失变量的更新操作
#
# # testbatch=r'C:\Users\XUEJW\Desktop\cifar-10-batches-py\test_batch'
# # def load_file(filename):
# #     with open(filename,'rb') as fo:
# #         data=pickle.load(fo,encoding='latin1')
# #     return data
# # data=load_file(testbatch)
# # #fd=pd.read_table(data)
# # #print(data.keys())['batch_label', 'labels', 'data', 'filenames']
# # #print(data['filenames'][6])#10000个图片名称'shooting_brake_s_000973.png'
# # #print(len(data['batch_label']),'\n',data['batch_label'])testing batch 1 of 1
# # print(data['data'][1:3])#10000*3072(32*32*3)个数据[235 231 232 ..., 178 191 199]
# #print(len(data['labels']),'\n',data['labels'][1:5])#10000个数字代表当前所属类别共10个类别
#
#
# #
# data,label=cf10.preprocess_input_data()
#
# init=tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#     coord=tf.train.Coordinator()
#     threads=tf.train.start_queue_runners(coord=coord)
#     #tf.train.start_queue_runners(sess=sess)
#     for i in range(1):
#         labely=sess.run(label)
#         x=sess.run(data)
#         y_label = tf.cast(x=labely, dtype=tf.int32)
#         #print(x.shape)
#         yy=sess.run(y_label)
#         print(yy)
#     coord.request_stop()
#     coord.join(threads)
#     print('ok')
data_dir=r'C:\Users\XUEJW\Desktop\cifar-10-batches-py'#'latin1
img_tr,label_tr,img_test,label_test=cf10.load_cifar_all(data_dir)
print(img_tr.shape,label_tr.shape,img_test.shape)