# -*- coding: utf-8 -*-
'''
Created on 2018年12月10日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#模型载体：操作
#计算节点：对应的是无状态的计算或控制操作，主要负责算法的逻辑表达式或流程控制
#存储节点：对应的是有状态的变量操作，通常用来存储模型参数
#数据节点：对应的是特殊的占位符操作，用于描述输入数据的属性
#计算节点：Operation
import tensorflow as tf
from tensorflow.python.ops import gen_state_ops
#创建名字作用域AddExample
with tf.name_scope('AddExample'):
    #创建变量a和b
    a=tf.Variable(1.0,name='a')
    b=tf.Variable(2.0,name='b')
    #使用add操作函数创建张量c
    c=tf.add(a,b,name='add')
    print(c)
#存储节点：Variable
#主要作用是在多次执行相同数据流图时存储特定的参数，会受到内部保存的状态值的影响
#一个变量通常由如下四个字节点构成：变量初始值，更新变量值的操作，读取变量值的操作，变量操作（inital_value,Assign,read,a）,前三种对应无状态，后一种变量操作为有状态
# def variable_op_v2(shape,name='Variable',container='',shared_name=''):
#     #创建变量操作
#     return gen_state_ops._variable_v2(shape=shape,dtype=dtype,name=name,container=container,shared_name=shared_name)
#数据节点
#tensorflow 数据节点由占位符操作实现，对应的操作函数为tf.placeholder.针对稀疏数据，也提供了稀疏占位操作，tf.sparse_placeholder
import numpy as np
with tf.name_scope('PlaceholderExample'):
    #定义形状为[2，2]的单精度浮点型矩阵
    x=tf.placeholder(tf.float32,shape=(2,2),name='x')
    y=tf.matmul(x,x,name='matmul')
with tf.Session() as sess:
    rand_array=np.random.rand(2,2)
    print(sess.run(y,feed_dict={x:rand_array}))