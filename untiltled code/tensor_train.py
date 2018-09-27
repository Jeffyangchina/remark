#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
# !/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author: Yang Xiaojun
# !/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author: Yang Xiaojun
import tensorflow as tf
import numpy as np
import readcifar10 as cf10

data_dir=r'C:\Users\XUEJW\Desktop\cifar-10-batches-py\data_batch_1'
finame=r'C:\Users\XUEJW\Desktop\cifar-10-batches-py'

# load data
# x_image,ys=cf10.preprocess_input_data()#[-1,24,24,3]
# y_label=tf.cast(x=ys,dtype=tf.int32)
fixed_height=24
fixed_width=24
num_class=10
size_depth=3
in_size = 3072
out_size = 10
# define placeholder
xs = tf.placeholder(tf.float32, [None,32,32,3])
ys = tf.placeholder(tf.int32,[None,1])
keep_prob = tf.placeholder(tf.float32)
batch_size=128

# new_img=tf.random_crop(xs,size=(fixed_height,fixed_width,3))#从原图像中切出指定大小
# new_img=tf.image.random_brightness(new_img,max_delta=63)#随机调节亮度
# new_img=tf.image.random_flip_left_right(new_img)#随机的左右翻转图像
# new_img=tf.image.random_contrast(new_img,lower=0.2,upper=1.8)#对比度
# final_img=tf.image.per_image_standardization(new_img)#目的是降低图像冗余性，尽量去除特征间相关性
# num_sample,28x28,num_channel



def Weights(shape):
    w = tf.truncated_normal(shape, stddev=0.1, dtype=tf.float32)
    return tf.Variable(w)


def Biases(shape):
    bas = tf.constant(0.1, shape=shape, dtype=tf.float32)
    return tf.Variable(bas)


def conv2d(x, W):
    # must strides[1,x_move,y_move,1]
    conv1 = tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')  # VALID 全在图片里 ，SAME则在图片外以0填充
    return conv1


def maxpool(inx):
    # ksize is the pool patch size, strides is move step
    mp = tf.nn.max_pool(inx, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')  # tf.nn.avg_pool()
    return mp


# define conv1 layer1
W_conv1 = Weights([5, 5, size_depth, 32])  # 5x5 is cnn patch size,1 is in size depth,32 is out size depth
b_conv1 = Biases([32])
h_conv1 = tf.nn.relu(conv2d(xs, W_conv1) + b_conv1)  # output size 24x24x32
out_con1 = maxpool(h_conv1)  # output size 12x12x32
# define conv2 layer2
W_conv2 = Weights([5, 5, 32, 64])
b_conv2 = Biases([64])
h_conv2 = tf.nn.relu(conv2d(out_con1, W_conv2) + b_conv2)
out_con2 = maxpool(h_conv2)  # output size 10,6x6x64

# define function layer1
W_func1 = Weights([6 * 6 * 64, 1024])  # insize,outsize
tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(0.0003)(W_func1))
b_func1 = Biases([1024])  # outsize
out_conv2_flat = tf.reshape(out_con2, [-1, 6 * 6 * 64])  # [n_sample,6,6,64]>>[n_sample,6*6*64]
out_func1 = tf.nn.relu(tf.matmul(out_conv2_flat, W_func1) + b_func1)
out_drop = tf.nn.dropout(out_func1, keep_prob)
# define function layer2
W_func2 = Weights([1024, num_class])  # insize1024,outsize
tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(0.0003)(W_func2))
b_func2 = Biases([num_class])  # outsize

#prediction =tf.matmul(out_drop, W_func2) + b_func2
prediction =tf.nn.softmax(tf.matmul(out_drop, W_func2) + b_func2)
# loss between prediction and real data
with tf.name_scope('loss'):
#这个函数的输入logits需要时未经tf.nn.softmax的，
    #cross_entropy_loss=tf.nn.sparse_softmax_cross_entropy_with_logits(logits=prediction,labels=ys)
    ylabel=tf.one_hot(ys,num_class,1,0)


    cross_entropy_loss=-tf.reduce_sum(tf.cast(ylabel,tf.float32)*tf.log(tf.cast(prediction,tf.float32)),reduction_indices=[1])
    cross_entropy=tf.reduce_mean(cross_entropy_loss)
    #cross_entropy = -tf.reduce_sum(y_label * tf.log(prediction))  # adam适合这种
    tf.add_to_collection('losses', cross_entropy)
    losses = tf.add_n(tf.get_collection("losses"))
    # tf.summary.scalar('loss',cross_entropy)
# define train
# train_step=tf.train.GradientDescentOptimizer(0.1).minimize(losses)
train_step = tf.train.AdamOptimizer(1e-4).minimize(losses)  # 和GD差不多的准确率,大规模数据用adam
correct_predict = tf.equal(tf.argmax(prediction, 1), tf.argmax(ys, 1))  # 返回的是bool值
accuracy = tf.reduce_mean(tf.cast(correct_predict, 'float'))
saver = tf.train.Saver()
# init
sess = tf.Session()
# merged=tf.summary.merge_all()#这是显示集合
# writer=tf.summary.FileWriter('logs/',sess.graph)#输出文件，用add
sess.run(tf.global_variables_initializer())
# train
try:
    x,y,X,Y=cf10.load_cifar_all(finame)
    all_size=len(x)
    rod=int(all_size/batch_size)

except Exception as s:
    print('wrong0',s)
with sess.as_default():
    # coord = tf.train.Coordinator()
    # threads = tf.train.start_queue_runners(coord=coord)
    # x_image,label = cf10.preprocess_input_data()  # [-1,24,24,3]


    for i in range(50):  #
        try:

            img = cf10.get_batch(x, batch_size, i%rod,label=1)
            label=cf10.get_batch(y,batch_size,i%rod)

        except Exception as s:
            print('wrong1', s)
        #tf.train.start_queue_runners(sess=sess)

        #y_label = tf.cast(x=yl, dtype=tf.int32)
        #batch = mnist.train.next_batch(50)
        # x_data_train = batch[0]
        # y_data_train = batch[1]
        # x_data_train =

        # y_data_train =y_data_trian_Adm

        try:


            sess.run(train_step, feed_dict={xs:img,ys:label, keep_prob: 0.5})  # x_data,y_data为数据集
        except Exception as s:
            print('wrong2', s)
        if i % 10 == 0:
            try:
                train_accuracy = accuracy.eval(feed_dict={ keep_prob: 1})
                print('step%d,trianing accuracy is %g' % (i, train_accuracy))
            except Exception as s:
                print('wrong3', s)
            # train_result =sess.run(merged,feed_dict={xs:x_data_train,ys:y_data_train,keep_prob:1})
            # test_result = sess.run(merged, feed_dict={xs: x_data_test, ys: y_data_test,keep_prob:1})
            # writer.add_summary(train_result,i)
            # writer.add_summary(test_result, i)
    # coord.request_stop()
    # coord.join(threads)
    print('finished')
    save_path = saver.save(sess, 'train/tensor.ckpt')
    #test_len = int(mnist.test.num_examples / 50) + 1
    test_count_all = 0
    test_correct = 0

    # for i in range(test_len):
    #     test_batch = mnist.test.next_batch(50)
    #     test_x = test_batch[0]
    #     test_y = test_batch[1]
    #     test_correct += accuracy.eval(feed_dict={xs: test_x, ys: test_y, keep_prob: 1})
    #     test_count_all += 1
    # print('test accuracy%g' % (test_correct / test_len))
    # print(test_count_all, test_len)



