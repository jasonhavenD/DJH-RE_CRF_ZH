#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:check_data
   Author:jasonhaven
   date:2018/5/1
-------------------------------------------------
   Change Activity:2018/5/1:
-------------------------------------------------
"""
import os

if __name__ == '__main__':
	train_vec, test_vec = ("result/train.vec", "result/test.vec")
	print('check.... for {}'.format(train_vec))
	os.system('python libsvm-3.22/tools/checkdata.py {}'.format(train_vec))
	print('check.... for {}'.format(test_vec))
	os.system('python libsvm-3.22/tools/checkdata.py {}'.format(test_vec))
