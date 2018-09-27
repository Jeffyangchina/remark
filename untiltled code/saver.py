#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist=input_data.read_data_sets('MNIST_data',one_hot=True)

#load data
x_data_test=mnist.test.images
y_data_test=mnist.test.labels
x_data_trian_Adm=mnist.train.images
y_data_trian_Adm=mnist.train.labels
in_size=784
out_size=10
#define placeholder
xs=tf.placeholder(tf.float32,[None,in_size])
ys=tf.placeholder(tf.float32,[None,out_size])
keep_prob=tf.placeholder(tf.float32)
#define init
def xaiver(fan_in,fan_out,constant=1):
    low=-constant*np.sqrt(6.0/(fan_in+fan_out))
    high=constant*np.sqrt(6.0/(fan_in+fan_out))
    return tf.random_uniform((fan_in,fan_out),minval=low,maxval=high)

#define layer
def add_layer(input,insize,outsize,layer_name=None,activation_function=None,keep_prob=1):
    layer='layer%s'%layer_name
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weight=tf.Variable(xaiver(insize,outsize),name='W',dtype=tf.float32)
            tf.summary.histogram(layer+'/weights',Weight)
        with tf.name_scope('biases'):
            biases=tf.Variable(tf.zeros([1,outsize])+0.1,name='b',dtype=tf.float32)
            tf.summary.histogram(layer + '/biases', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b=tf.add(tf.matmul(input,Weight),biases)
            Wx_plus_b=tf.nn.dropout(Wx_plus_b,keep_prob)
        if activation_function is None:
            outputs=Wx_plus_b
        else:
            outputs=activation_function(Wx_plus_b)
        tf.summary.histogram(layer+'/output',outputs)
    return outputs
#add output layer
l1=add_layer(xs,in_size,100,'l1',activation_function=tf.nn.relu)
prediction=add_layer(l1,100,out_size,'l2',activation_function=tf.nn.softmax)

#loss between prediction and real data
with tf.name_scope('loss'):

    cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
    tf.summary.scalar('loss',cross_entropy)
#define train
#train_step=tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)#和GD差不多的准确率
correct_predict=tf.equal(tf.argmax(prediction,1),tf.argmax(ys,1))#返回的是bool值
accuracy=tf.reduce_mean(tf.cast(correct_predict,'float'))
#save
saver=tf.train.Saver()
#init
sess=tf.Session()
merged=tf.summary.merge_all()#这是显示集合
writer=tf.summary.FileWriter('logs/',sess.graph)#输出文件，用add
sess.run(tf.global_variables_initializer())
#train
with sess.as_default():
    # for i in range(5000):#5000就稳定了0.97 从tensorboard的loss里看出来
    #
    #     batch=mnist.train.next_batch(100)
    #     x_data_train =batch[0]
    #     y_data_train = batch[1]
    #     #x_data_train =x_data_trian_Adm
    #     #y_data_train =y_data_trian_Adm
    #     sess.run(train_step, feed_dict={xs: x_data_train, ys: y_data_train, keep_prob: 0.5})  # x_data,y_data为数据集
    #
    #     if i%100==0:
    #         train_accuracy=accuracy.eval(feed_dict={xs:x_data_train,ys:y_data_train,keep_prob:1})
    #         print('step%d,trianing accuracy is %g'%(i,train_accuracy))
    #         train_result =sess.run(merged,feed_dict={xs:x_data_train,ys:y_data_train,keep_prob:1})
    #         test_result = sess.run(merged, feed_dict={xs: x_data_test, ys: y_data_test,keep_prob:1})
    #         writer.add_summary(train_result,i)
    #         writer.add_summary(test_result, i)
    saver.restore(sess,'yangcnn/tensor.ckpt')

    print('test accuracy%g'%accuracy.eval(feed_dict={xs: x_data_test, ys: y_data_test,keep_prob:1}))



