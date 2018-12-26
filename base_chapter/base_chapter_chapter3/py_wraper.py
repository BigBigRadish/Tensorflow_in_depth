# -*- coding: utf-8 -*-
'''
Created on 2018年12月26日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#python装饰器
import time
def out_wrapper(func):
    def inner_wrapper():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('used time {}'.format(stop_time-start_time))
    return inner_wrapper()
@out_wrapper
def test1():
    time.sleep(1)
    print('I am a test')

        
    