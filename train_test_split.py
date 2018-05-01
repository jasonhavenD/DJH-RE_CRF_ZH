#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:train_test_split
   Author:jasonhaven
   date:2018/4/29
-------------------------------------------------
   Change Activity:2018/4/29:
-------------------------------------------------
"""
import os

'''
Training large data is time consuming. Sometimes one should work on a
smaller subset first. The python script subset.py randomly selects a
specified number of samples. For classification data, we provide a
stratified selection to ensure the same class distribution in the
subset.

Usage: subset.py [options] dataset number [output1] [output2]

'''

if __name__ == '__main__':
	feature = "result/feature2libsvm.csv"
	train_vec, test_vec = ("result/train.vec", "result/test.vec")
	data = []
	with open(feature, 'r', encoding='utf-8') as f:
		data = f.readlines()
	size = int(0.1 * len(data))
	os.system('python libsvm-3.22/tools/subset.py -s 1 {} {} {} {}'.format(feature, size, os.path.abspath(test_vec),
	                                                                  os.path.abspath(train_vec)))