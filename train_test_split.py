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
if __name__ == '__main__':
	feature = "result/feature2libsvm.csv"
	train_vec, test_vec = ("result/train.vec", "result/test.vec")
	data = []
	with open(feature, 'r', encoding='utf-8') as f:
		data = f.readlines()
	with open(train_vec, 'w', encoding='utf-8') as f:
		f.writelines(''.join(data[:int(len(data) * 0.7)]))
	with open(test_vec, 'w', encoding='utf-8') as f:
		f.writelines(''.join(data[int(len(data) * 0.3):]))
