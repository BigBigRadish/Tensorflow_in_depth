# -*- coding: utf-8 -*-
'''
Created on 2018年12月26日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
'''
numpy 处理数据
'''
import numpy as np
import time
def out_wrapper(func):
    def inner_wrapper():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('used time {}'.format(stop_time-start_time))
    return inner_wrapper()
# @out_wrapper
# def test1():#10w数据内存溢出
#     a=np.random.rand(100000,200000)
#     (a+1).sum(axis=1)
'''
pamars多核并行 处理数据
'''
@out_wrapper
def test2():#10w数据内存没有溢出
    import mars.tensor as mt
    a=mt.random.rand(100000,200000)
    (a+1).sum(axis=1).execute()
