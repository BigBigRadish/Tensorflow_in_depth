# -*- coding: utf-8 -*-
'''
Created on 2018年12月10日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#创建
import tensorflow as tf
a=tf.constant(1.0)
b=tf.constant(2.0)
c=tf.add(a,b)
print([a,b,c])
#求解
with tf.Session() as sess:
    print(c.eval())
    print(sess.run([a,b,c]))
#典型用例
a=tf.constant([1,1])
b=tf.constant([2,2])
c=tf.add(a,b)
with tf.Session() as sess:
    print('a[0]=%s,a[1]=%s' %(a[0].eval(),a[1].eval()))
    print('c.name=%s' % c.name)
    print('c.value=%s' % c.eval())
    print('c.shape=%s' % c.shape)
    print('a.consumers=%s' % a.consumers())
    print('b.consumers=%s' % b.consumers())
    print('[c.op] :\n%s' % c.op)