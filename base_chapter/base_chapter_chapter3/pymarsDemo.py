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
a=np.random.rand(1000,2000)
print((a+1).sum(axis=1))
'''
pamars多核并行 处理数据
'''
import mars.tensor as mt
a=mt.random.rand(1000,2000)
print((a+1).sum(axis=1).execute())
