#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime
import data_helpers
from text_cnn import TextCNN
from tensorflow.contrib import learn
import csv
# Parameters
# ==================================================

# Data loading params
tf.flags.DEFINE_float("dev_sample_percentage", .1, "Percentage of the training data to use for validation")
# tf.flags.DEFINE_string("positive_data_file", "./data/rt-polaritydata/rt-polarity.pos", "Data source for the positive data.")
# tf.flags.DEFINE_string("negative_data_file", "./data/rt-polaritydata/rt-polarity.neg", "Data source for the negative data.")

# Model Hyperparameters
tf.flags.DEFINE_integer("embedding_dim", 128, "Dimensionality of character embedding (default: 128)")
tf.flags.DEFINE_string("filter_sizes", "3,4,5", "Comma-separated filter sizes (default: '3,4,5')")
tf.flags.DEFINE_integer("num_filters", 128, "Number of filters per filter size (default: 128)")
tf.flags.DEFINE_float("dropout_keep_prob", 0.5, "Dropout keep probability (default: 0.5)")
tf.flags.DEFINE_float("l2_reg_lambda", 0.0, "L2 regularization lambda (default: 0.0)")

# Training parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_integer("num_epochs", 200, "Number of training epochs (default: 200)")
tf.flags.DEFINE_integer("evaluate_every", 200, "Evaluate model on dev set after this many steps (default: 100)")
tf.flags.DEFINE_integer("checkpoint_every",200, "Save model after this many steps (default: 100)")
tf.flags.DEFINE_integer("num_checkpoints", 5, "Number of checkpoints to store (default: 5)")
# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")

FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")


# Data Preparation
# ==================================================
import sqlite3
import jieba
import re

from sklearn.preprocessing import OneHotEncoder

# print('yang:',os.getcwd())
path_db='./cnn-text-classification-tf-master/Db_classify.db'
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
def rm_puc(line):
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
def out_en(astr):
    outstr = re.sub("[a-zA-Z]", "", astr)
    outstr=outstr.strip()
    return outstr
def out_num(instr):
    outstr = re.sub('[0-9]+$', '', instr)
    return outstr
def jieba_cut(astr,conn):
    command = 'select * from fenci'
    sql = command
    cursor = conn.cursor()
    res = cursor.execute(sql)
    tempx = res.fetchall()
    fenci = []
    data=[]
    if tempx:
        for x in tempx:
            if x not in fenci:
                fenci.append(x[0])
    fenci_set=set(fenci)
    jieba.load_userdict(fenci_set)
    # jieba.load_userdict(r"E:\兴业银行\中文翻译英文最终数据集\切词时用\分词库.txt")
    astr = astr.strip()
    ostr = rm_puc(astr)
    olist = list(jieba.cut(ostr))

    olist=rm_same(olist)
    olist = rm_null(olist)
    stopwords = stopwordslist('./cnn-text-classification-tf-master/stopword_zh_en.txt')
    for item in olist:
        if item:
            try:
                line = out_num(item).upper()
                line = rm_space(line)
                pt = out_en(line)
                if line not in stopwords:
                    if line != '\t' and len(line) > 0 and len(pt) > 0:
                        if line not in data:
                            data.append(line)


            except:
                print(item)

    zh_out = ' '.join(data)
    return zh_out
def temp_tensor_get(path):
    conn = sqlite3.connect(path)
    command = 'select * from cleaned_temp_train'#这个表去掉了测试集
    sql = command
    cursor = conn.cursor()
    res = cursor.execute(sql)
    tempx = res.fetchall()
    train_data=[]
    out_y=[]
    i=0
    ohe = OneHotEncoder()
    ohe.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])

    if tempx:
        for tx in tempx:
            src0=tx[0].strip().upper()
            src1=tx[1].strip()
            src2=tx[2].strip()
            if len(src0)!=0 or len(src1)!=0 or len(src2)!=0 :
                src_sum=src1+src2
                temp_src_li=jieba_cut(src_sum,conn)
                src_li=src0+' '+temp_src_li
                tgt_word=tx[3].strip()
                if tgt_word == 'T00':
                    tgt = [0]
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
                union=[src_li]+tgt
                out_y.append(union)
                if i<2:
                    print('i=:',temp_src_li)
                    print('i2:',out_y)
                    i+=1
    conn.close()
    return out_y


def get_fr_csv(path):
    import csv
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    data_out=[]
    for item in reader:
        if item:
            data_out.append(item)
    return data_out
def load_data(path):
    train_data = get_fr_csv(path)
    # train_data = temp_tensor_get(path)
    tr_x_= [x[:-1] for x in train_data]
    tr_y_ = [[x[-1]] for x in train_data]
    ohe = OneHotEncoder()
    ohe.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
    tr_y = ohe.transform(tr_y_).toarray()
    tr_x=[]
    for x in tr_x_:
        tr_x+=x
    return tr_x,tr_y
def load_first_data(path):
    import csv
    from sklearn import preprocessing
    from sklearn.utils import shuffle
    from sklearn.model_selection import train_test_split
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    data_out = []
    for item in reader:
        if item:
            data_out.append(item)
    train_data=shuffle(data_out)
    tr_x_ = [x[1:] for x in train_data]
    tr_y_ = [x[0] for x in train_data]
    # X_train, X_test, y_train, y_test = train_test_split(tr_x_, tr_y_, test_size=0.3, random_state=42)
    mlb = preprocessing.LabelBinarizer() # 将标签编码
    # mlb = preprocessing.MultiLabelBinarizer()  # 将标签编码
    orin_mlb = mlb.fit(tr_y_)
    orin_label = mlb.classes_.tolist()
    y_ = mlb.transform(tr_y_)
    y=y_
    tr_x=[]
    for x in tr_x_:
        tr_x+=x
    return tr_x,y,orin_label
# Load data
# create_data(r'E:\yang_xy_test\ten class\test\te')
print("Loading data...")
# data_path='./train_dataset.csv'
first_path='./data_first.csv'
# x_text, y = data_helpers.load_data_and_labels(FLAGS.positive_data_file, FLAGS.negative_data_file)
# x_text, y = load_data(data_path)
x_text,y,label=load_first_data(first_path)
# x_text, y = load_data(path_db)


# Build vocabulary
max_document_length = max([len(x.split(" ")) for x in x_text])
vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
x = np.array(list(vocab_processor.fit_transform(x_text)))

# Randomly shuffle data
np.random.seed(10)
shuffle_indices = np.random.permutation(np.arange(len(y)))
x_shuffled = x[shuffle_indices]
y_shuffled = y[shuffle_indices]

# Split train/test set
# TODO: This is very crude, should use cross-validation
dev_sample_index = -1 * int(FLAGS.dev_sample_percentage * float(len(y)))
x_train, x_dev = x_shuffled[:dev_sample_index], x_shuffled[dev_sample_index:]
y_train, y_dev = y_shuffled[:dev_sample_index], y_shuffled[dev_sample_index:]

del x, y, x_shuffled, y_shuffled

print("Vocabulary Size: {:d}".format(len(vocab_processor.vocabulary_)))
print("Train/Dev split: {:d}/{:d}".format(len(y_train), len(y_dev)))


# Training
# ==================================================

with tf.Graph().as_default():
    session_conf = tf.ConfigProto(
      allow_soft_placement=FLAGS.allow_soft_placement,
      log_device_placement=FLAGS.log_device_placement)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        cnn = TextCNN(
            sequence_length=x_train.shape[1],
            num_classes=y_train.shape[1],
            vocab_size=len(vocab_processor.vocabulary_),
            embedding_size=FLAGS.embedding_dim,
            filter_sizes=list(map(int, FLAGS.filter_sizes.split(","))),
            num_filters=FLAGS.num_filters,
            l2_reg_lambda=FLAGS.l2_reg_lambda)

        # Define Training procedure
        global_step = tf.Variable(0, name="global_step", trainable=False)
        optimizer = tf.train.AdamOptimizer(1e-3)
        grads_and_vars = optimizer.compute_gradients(cnn.loss)
        train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)

        # Keep track of gradient values and sparsity (optional)
        grad_summaries = []
        for g, v in grads_and_vars:
            if g is not None:
                grad_hist_summary = tf.summary.histogram("{}/grad/hist".format(v.name), g)
                sparsity_summary = tf.summary.scalar("{}/grad/sparsity".format(v.name), tf.nn.zero_fraction(g))
                grad_summaries.append(grad_hist_summary)
                grad_summaries.append(sparsity_summary)
        grad_summaries_merged = tf.summary.merge(grad_summaries)

        # Output directory for models and summaries
        timestamp = str(int(time.time()))
        out_dir = os.path.abspath(os.path.join(os.path.curdir, "runs", timestamp))
        print("Writing to {}\n".format(out_dir))

        # Summaries for loss and accuracy
        loss_summary = tf.summary.scalar("loss", cnn.loss)
        acc_summary = tf.summary.scalar("accuracy", cnn.accuracy)

        # Train Summaries
        train_summary_op = tf.summary.merge([loss_summary, acc_summary, grad_summaries_merged])
        train_summary_dir = os.path.join(out_dir, "summaries", "train")
        train_summary_writer = tf.summary.FileWriter(train_summary_dir, sess.graph)

        # Dev summaries
        dev_summary_op = tf.summary.merge([loss_summary, acc_summary])
        dev_summary_dir = os.path.join(out_dir, "summaries", "dev")
        dev_summary_writer = tf.summary.FileWriter(dev_summary_dir, sess.graph)

        # Checkpoint directory. Tensorflow assumes this directory already exists so we need to create it
        checkpoint_dir = os.path.abspath(os.path.join(out_dir, "checkpoints"))
        checkpoint_prefix = os.path.join(checkpoint_dir, "model")
        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)
        saver = tf.train.Saver(tf.global_variables(), max_to_keep=FLAGS.num_checkpoints)

        # Write vocabulary
        vocab_processor.save(os.path.join(out_dir, "vocab"))

        # Initialize all variables
        sess.run(tf.global_variables_initializer())

        def train_step(x_batch, y_batch):
            """
            A single training step
            """
            feed_dict = {
              cnn.input_x: x_batch,
              cnn.input_y: y_batch,
              cnn.dropout_keep_prob: FLAGS.dropout_keep_prob
            }
            _, step, summaries, loss, accuracy = sess.run(
                [train_op, global_step, train_summary_op, cnn.loss, cnn.accuracy],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            # print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            train_summary_writer.add_summary(summaries, step)

        def dev_step(x_batch, y_batch, writer=None):
            """
            Evaluates model on a dev set
            """
            feed_dict = {
              cnn.input_x: x_batch,
              cnn.input_y: y_batch,
              cnn.dropout_keep_prob: 1.0
            }
            step, summaries, loss, accuracy = sess.run(
                [global_step, dev_summary_op, cnn.loss, cnn.accuracy],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            if writer:
                writer.add_summary(summaries, step)

        # Generate batches
        batches = data_helpers.batch_iter(
            list(zip(x_train, y_train)), FLAGS.batch_size, FLAGS.num_epochs)
        # Training loop. For each batch...
        for batch in batches:
            x_batch, y_batch = zip(*batch)
            train_step(x_batch, y_batch)
            current_step = tf.train.global_step(sess, global_step)
            if current_step % FLAGS.evaluate_every == 0:
                print("\nEvaluation:")
                dev_step(x_dev, y_dev, writer=dev_summary_writer)
                print("")
            if current_step % FLAGS.checkpoint_every == 0:
                path = saver.save(sess, checkpoint_prefix, global_step=current_step)
                print("Saved model checkpoint to {}\n".format(path))
