# -*- coding: utf-8 -*-
'''
Created on 2018年12月10日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
import tensorflow as tf
#普通会话
#（1）创建会话（2）运行会话（3）关闭会话
#假如没有GPU时，tensorflow能够自动将计算任务转移到cpu上运行，并希望通过日志验证放置情况
sess=tf.Session(config=tf.ConfigProto(allow_soft_placement=True,log_device_placement=True))
#创建数据流图c=a*b
a=tf.constant(5.0)
b=tf.constant(6.0)
c=a*b
sess=tf.Session()
#求解张量c的值，没有依赖数据节点，所以无需填充数据
print(sess.run(c))
#对于存在数据依赖的张量，调用Session.run方法时，则需要制定数据填充字典
x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)
z=x*y
print(sess.run(z,feed_dict={x:3.0,y:3.0}))
w=tf.Variable(1.0)
b=tf.Variable(1.0)
y=w*x+b
with tf.Session() as sess:
    tf.global_variables_initializer().run()#operation.Run()
    fetch=y.eval(feed_dict={x:3.0})
    print(fetch)
#交互式会话：InteractiveSession 
