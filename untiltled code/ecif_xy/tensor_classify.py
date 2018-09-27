#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import numpy as np
import os
from tensorflow.contrib.learn.python import SKCompat



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def make_one_hot():
    labels=[3,7,9]
    # batch_size = tf.size(labels)
    batch_size=3

    labels = tf.expand_dims(labels, 1)
    indices = tf.expand_dims(tf.range(0, batch_size, 1), 1)
    concated = tf.concat([indices, labels],1)
    # [[0 3]就是标序号，labels是个输入标签批次。
    #  [1 7]
    #  [2 9]]
    onehot_labels = tf.sparse_to_dense(concated, tf.stack([batch_size, 10]), 1.0, 0.0)
    # [[ 0.  0.  0.  1.  0.  0.  0.  0.  0.  0.]
    #  [ 0.  0.  0.  0.  0.  0.  0.  1.  0.  0.]
    #  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]]

def read_csv(tr_set):

    if not os.path.exists(tr_set):
        print('no such file')

    training_set = tf.contrib.learn.datasets.base.load_csv_without_header(
        filename=tr_set,
        target_dtype=np.int,
        features_dtype=np.int)
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=2763)]
    return training_set

def get_train_inputs(training_set):
    x = tf.constant(training_set.data)
    y = tf.constant(training_set.target)
    return x,y

# tset=read_csv()
# x,y=get_train_inputs(tset)
def classify(tr_file,test_file):
    # 数据集名称，数据集要放在你的工作目录下

    if not os.path.exists(tr_file):
        print('no such train file')
    if not os.path.exists(test_file):
        print('no such test_file')
    train_data= tr_file
    test_data=test_file
    # 数据集读取，训练集和测试集
    training_set = tf.contrib.learn.datasets.base.load_csv_without_header(
        filename=train_data,
        target_dtype=np.int,
        features_dtype=np.float32)
    test_set = tf.contrib.learn.datasets.base.load_csv_without_header(
        filename=test_data,
        target_dtype=np.int,
        features_dtype=np.float32)

    # 特征
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=2763)]

    # 构建DNN网络，3层，每层分别为10,20,10个节点
    classifier =  SKCompat(tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units=[4096,8192, 4096,2048,512,128,32],
                                                n_classes=13,
                                                model_dir=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input dataset\model'))

    # 拟合模型，迭代2000步

    classifier.fit(x=training_set.data,
                   y=training_set.target,
                   steps=2000)

    # 计算精度
    accuracy_score = classifier.evaluate(x=test_set.data, y=test_set.target)["accuracy"]

    print('Accuracy: {0:f}'.format(accuracy_score))

    # 预测新样本的类别

tr_set = r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input dataset\train\tensor_input_train_set.csv'
test_file=r'C:\Users\XUEJW\Desktop\兴业数据\分类用数据集\数据集\input dataset\test\tensor_input_test_set.csv'
def xaiver(fan_in,fan_out,constant=1):
    low=-constant*np.sqrt(6.0/(fan_in+fan_out))
    high=constant*np.sqrt(6.0/(fan_in+fan_out))
    return tf.random_uniform((fan_in,fan_out),minval=low,maxval=high)

def inf(x,avgclass,w1,w2,b1,b2):
    if avgclass==None:
        y1=tf.nn.relu(tf.matmul(x,w1)+b1)
        return tf.matmul(y1,w2)+b2
    else:
        y1=tf.nn.relu(tf.matmul(x,avgclass.average(w1))+avgclass.average(b1))
        return tf.matmul(y1,avgclass.average(w2))+avgclass.average(b2)
def classify2(tr_file,test_file):


    x = tf.placeholder(tf.float32, shape=[None, 784], name='x-input')
    y_ = tf.placeholder(tf.float32, shape=[None, 10], name='y-input')

    w1 = tf.Variable(tf.truncated_normal(shape=[2763, 4096], stddev=0.1, dtype=tf.float32))

    w2 = tf.Variable(tf.truncated_normal(shape=[4096, 2048], stddev=0.1, dtype=tf.float32))
    w3= tf.Variable(tf.truncated_normal(shape=[2048, 512], stddev=0.1, dtype=tf.float32))
    w4 = tf.Variable(tf.truncated_normal(shape=[512, 13], stddev=0.1, dtype=tf.float32))
    b1 = tf.Variable(tf.constant(0.1, shape=[4096]))
    b2 = tf.Variable(tf.constant(0.1, shape=[2048]))
    b3 = tf.Variable(tf.constant(0.1, shape=[512]))
    b4 = tf.Variable(tf.constant(0.1, shape=[13]))
    global_step = tf.Variable(0, trainable=False)
    move_average_decay = 0.99

    learning_rate_decay = 0.99

    learning_rate_base = 0.8

    regularization = 0.0001


    batch_size=128

    learning_rate = tf.train.exponential_decay(learning_rate_base, global_step, dataSize / batch_size,
                                               learning_rate_decay, staircase=False)

    entropy = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y)) + tf.contrib.layers.l2_regularizer(
        regularization)(w1) + tf.contrib.layers.l2_regularizer(regularization)(w2)
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(entropy, global_step)
    cor = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))
    aur = tf.reduce_mean(tf.cast(cor, tf.float32))


sess=tf.Session()
sess.run(tf.global_variables_initializer())
with sess.as_default():
    classify(tr_set,test_file)


