#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:eval
   Author:jasonhaven
   date:2018/4/29
-------------------------------------------------
   Change Activity:2018/4/29:
-------------------------------------------------
"""
import os
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

if __name__ == '__main__':
	test_file = 'libsvm-3.22/windows/test.vec'
	test_predict = 'libsvm-3.22/windows/test.vec.out'
	result = 'libsvm-3.22/windows/result.csv'

	with open(test_file, 'r', encoding='utf-8') as f:
		df1 = pd.read_csv(f, sep='\t', header=None)
	with open(test_predict, 'r', encoding='utf-8') as f:
		df2 = pd.read_csv(f, sep='\t', header=None)
	df = pd.DataFrame()
	for i in list(df1.columns)[1:]:
		df[i - 1] = df1[i]
	df[df1.shape[1] - 1] = df1[0]
	df[df1.shape[1]] = df2
	df.to_csv('libsvm-3.22/windows/result.csv', header=None, sep='\t', index=None)

	with open(result, 'r', encoding='utf-8') as f:
		df = pd.read_csv(f, sep='\t', header=None)

	y_true = df[df.shape[1] - 2]
	y_pre = df[df.shape[1] - 1]
	p = precision_score(y_true, y_pre, average='macro')  # binary micro macro weighted samples
	r = recall_score(y_true, y_pre, average='macro')
	f1 = f1_score(y_true, y_pre, average='macro')
	print('精確度:{}\n召回率:{}\nF1值:{}'.format(p, r, f1))
