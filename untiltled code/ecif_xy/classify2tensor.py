#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import tensorflow as tf
import numpy as np
import pandas as pd
import operator
from functools import reduce
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
move_average_decay=0.99

learning_rate_decay=0.99


learning_rate_base = 0.8


regularization = 0.0001



batch_size=128

tr_set = r'C:\Users\XUEJW\Desktop\yang_test\data_set\tensor_input_train_set.csv'
test_file = r'C:\Users\XUEJW\Desktop\yang_test\data_set\tensor_input_test_set.csv'
# pwd = os.getcwd()
# os.chdir(os.path.dirname(tr_set))
train_data = pd.read_csv(tr_set,header=None)#不能有中文出现
# os.chdir(os.path.dirname(test_file))
test_data = pd.read_csv(test_file,header=None)


num_data=train_data.shape[0]

train_x = train_data.iloc[:, :-1].values

train_y_ = train_data.iloc[:, -1:].values

train_2 = np.array(train_y_).tolist()
labels=reduce(operator.add,train_2)
one_hot = pd.get_dummies(labels)
one_hot = one_hot.astype('float')

test_x = test_data.iloc[:, 0:-1].values
test_0= test_data.iloc[:, -1:].values

test_1 = np.array(test_0).tolist()
labels_test=reduce(operator.add,test_1)
one_hot1= pd.get_dummies(labels_test)
one_hot1 = one_hot1.astype('float')
dataSize=train_x.shape[0]
print('0:',len(one_hot1))
def inf(x,w0,w1,w2,w3,b0,b1,b2,b3,avgclass=None):
    if avgclass==None:
        y1=tf.nn.relu(tf.matmul(x,w0)+b0)
        y2 = tf.nn.relu(tf.matmul(y1, w1) + b1)
        y3 = tf.nn.relu(tf.matmul(y2, w2) + b2)
        return tf.matmul(y3,w3)+b3
    else:
        y1=tf.nn.relu(tf.matmul(x,avgclass.average(w0))+avgclass.average(b0))
        y2 = tf.nn.relu(tf.matmul(y1, avgclass.average(w1)) + avgclass.average(b1))
        y3 = tf.nn.relu(tf.matmul(y2, avgclass.average(w2)) + avgclass.average(b2))

        return tf.matmul(y3,avgclass.average(w3))+avgclass.average(b3)

x=tf.placeholder(tf.float32,shape=[None,2763],name='x-input')
y_=tf.placeholder(tf.float32,shape=[None,11],name='y-input')
w0=tf.Variable(tf.truncated_normal(shape=[2763,8192],stddev=0.1,dtype=tf.float32))
w1=tf.Variable(tf.truncated_normal(shape=[8192,4096],stddev=0.1,dtype=tf.float32))
w2=tf.Variable(tf.truncated_normal(shape=[4096,1024],stddev=0.1,dtype=tf.float32))
w3=tf.Variable(tf.truncated_normal(shape=[1024,11],stddev=0.1,dtype=tf.float32))
b0=tf.Variable(tf.constant(0.1,shape=[8192]))
b1=tf.Variable(tf.constant(0.1,shape=[4096]))
b2=tf.Variable(tf.constant(0.1,shape=[1024]))
b3=tf.Variable(tf.constant(0.1,shape=[11]))

global_step=tf.Variable(0,trainable=False)

learning_rate=tf.train.exponential_decay(learning_rate_base,global_step,dataSize/batch_size,learning_rate_decay,staircase=False)

# a=tf.nn.relu(tf.matmul(x,w1)+b1)

# y__=tf.matmul(a,w2)+b2

y__=inf(x,w0,w1,w2,w3,b0,b1,b2,b3)



variable_averages=tf.train.ExponentialMovingAverage(
    move_average_decay,global_step
)
variable_averages_op=variable_averages.apply(tf.trainable_variables())#滑动平均的方法更新参数,decay为衰减速率


y=inf(x,w0,w1,w2,w3,b0,b1,b2,b3,variable_averages)

entropy=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y__))+tf.contrib.layers.l2_regularizer(regularization)(w0)+tf.contrib.layers.l2_regularizer(regularization)(w1)+tf.contrib.layers.l2_regularizer(regularization)(w2)+tf.contrib.layers.l2_regularizer(regularization)(w3)

# train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(entropy,global_step)

train_step=tf.train.AdamOptimizer(learning_rate).minimize(entropy)

with tf.control_dependencies([train_step,variable_averages_op]):
    train_op=tf.no_op(name='train')

cor=tf.equal(tf.argmax(y_,1),tf.argmax(y,1))
aur=tf.reduce_mean(tf.cast(cor,tf.float32))
model_path = r'C:\Users\XUEJW\Desktop\yang_test\data_set\model.ckpt'
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()

    sess.run(init_op)

    saver = tf.train.Saver()
    if os.path.isfile(model_path):
        saver.restore(sess, "D:\sample\model.ckpt")
    for i in range(5000):
        if i%100==0 and i>30:
            auc=sess.run(aur,feed_dict={x:test_x,y_:one_hot1})

            print("第{}次，准确率为{}".format(i+100,auc))
        start = (i * batch_size) % (dataSize )
        end = min(start + batch_size, dataSize )
        sess.run(train_op,feed_dict={x:train_x[start:end],y_:one_hot[start:end]})


    save_path = saver.save(sess, model_path)
    # yy = sess.run(y__, feed_dict={x: test_x})
    # yl = sess.run(tf.argmax(yy, 1))
