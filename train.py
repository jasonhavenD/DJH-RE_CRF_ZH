#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:train
   Author:jasonhaven
   date:2018/4/28
-------------------------------------------------
   Change Activity:2018/4/28:
-------------------------------------------------
"""
import sys

sys.path.append('libsvm-3.22\python')
sys.path.append('libsvm-3.22/tools')

import os
import datetime
from svmutil import *


def get_params():
	# 命令结果分别表明使用RBF核函数的c-svm的最佳的：c、g、识别率
	# path = os.path.abspath('libsvm-3.22/tools/grid.py')
	# os.system('python {} {} > params.txt'.format(path, os.path.abspath(train_vec)))
	c = 0.5
	g = 0.00048828125
	params = "-c {} -g {}".format(float(c), float(g))
	return params


if __name__ == '__main__':
	train_vec, test_vec = ("result/train.vec", "result/test.vec")
	evaluation = "evaluation.txt"
	# open file
	f_evaluation = open(evaluation, 'a', encoding='utf-8')

	train_label, train_value = svm_read_problem(train_vec)  # 训练数据集
	predict_label, predict_value = svm_read_problem(test_vec)  # 预测数
	print('\n***************train***************\n')
	model = svm_train(train_label, train_value)  # 训练模型
	# svm_save_model("result/model.txt", model)  # 保存模型

	# 第一阶段
	# f_evaluation.write('baseline：\n')
	print('\n***************predict***************\n')
	p_label, p_acc, p_val = svm_predict(predict_label, predict_value, model)
	print('\n***************result***************\n')
	output = ['ACC = {}'.format(p_acc[0]), 'MSE = {}'.format(p_acc[1]), 'SCC = {}'.format(p_acc[2])]
	print('\n'.join(output))
	# f_evaluation.write('\n'.join(output))
	# 第二阶段
	# f_evaluation.write('\n优化参数：\n')
	# params = get_params()  # 优化参数
	# print('\n***************train***************\n')
	# model = svm_train(train_label, train_value,params)  # 训练模型
	# # svm_save_model("result/model.txt", model)  # 保存模型
	# print('\n***************predict***************\n')
	# p_label, p_acc, p_val = svm_predict(predict_label, predict_value, model)
	# print('\n***************result***************\n')
	# output = ['ACC = {}'.format(p_acc[0]), 'MSE = {}'.format(p_acc[1]), 'SCC = {}'.format(p_acc[2])]
	# print('\n'.join(output))
	# f_evaluation.write('\n'.join(output))

	#第三阶段
	# f_evaluation.write('\n特征缩放：\n')
	# train_vec, test_vec = ("result/train_scale.vec", "result/test_scale.vec")
	# print('\n***************train***************\n')
	# model = svm_train(train_label, train_value)  # 训练模型
	# # svm_save_model("result/model.txt", model)  # 保存模型
	# print('\n***************predict***************\n')
	# p_label, p_acc, p_val = svm_predict(predict_label, predict_value, model)
	# print('\n***************result***************\n')
	# output = ['ACC = {}'.format(p_acc[0]), 'MSE = {}'.format(p_acc[1]), 'SCC = {}'.format(p_acc[2])]
	# print('\n'.join(output))
	# f_evaluation.write('\n'.join(output))


	#close file
	f_evaluation.close()
