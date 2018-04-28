#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:convert2libsvm
   Author:jasonhaven
   date:2018/4/28
-------------------------------------------------
   Change Activity:2018/4/28:
-------------------------------------------------
"""
import pandas as pd

if __name__ == '__main__':
	feature_vec_file = 'result/features.vec.csv'
	feature2libsvm = 'result/feature2libsvm.csv'
	with open(feature_vec_file, 'r', encoding='utf-8') as f:
		df = pd.read_csv(f)

	with open(feature2libsvm, 'w', encoding='utf-8') as f:
		for i, row in df.iterrows():
			line = []
			line.append(str(row[1]))  # rel
			for i, val in enumerate(row[2:]):
				line.append("{}:{}".format(str(i + 1), str(val)))
			f.writelines('\t'.join(line))
			f.write('\n')
