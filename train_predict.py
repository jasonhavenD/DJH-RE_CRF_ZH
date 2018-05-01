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
import os

sys.path.append('libsvm-3.22\python')
sys.path.append('libsvm-3.22/tools')
import json
from svmutil import *
from grid import *
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score


def eval_p_r_f(y_true, y_pre):
	'''
	计算精确度、召回率、F值
	'''
	p = precision_score(y_true, y_pre, average='macro')  # binary micro macro weighted samples
	r = recall_score(y_true, y_pre, average='macro')
	f = f1_score(y_true, y_pre, average='macro')
	output = {}
	output['precision'] = p
	output['recall'] = r
	output['f-value'] = f
	return json.dumps(output)


def get_params(train_txt):
	'''
	grid.py is a parameter selection tool for C-SVM classification（参数选优工具） using the RBF (radial basis function)（核函数） kernel.
	It uses cross validation (CV) technique（交叉检验技术） to estimate the accuracy of each parameter combination in the specified range and helps you to decide the best parameters for your problem.
	'''
	# 默认参数为：
	# fold = 5
	# c_begin, c_end, c_step = -5, 15, 2
	# g_begin, g_end, g_step = 3, -15, -2
	fold = 10
	c_begin, c_end, c_step = -5, 15, 2
	g_begin, g_end, g_step = 3, -15, -2
	options='-log2c %s,%s,%s -log2g %s,%s,%s -v %s -out result/grid.out -png result/grid.png'%(c_begin, c_end, c_step, g_begin, g_end, g_step, fold)
	rate, param = find_parameters(train_txt,options)
	print('CV Rate = {}'.format(rate))  # 交叉验证精度，最优结果
	c = param['c']
	g = param['g']
	params = "-c {} -g {} -q".format(float(c), float(g))
	return params


def save2file(p_acc, predict_label, p_label):
	output['ACC'] = p_acc[0]
	output['MSE'] = p_acc[1]
	output['SCC'] = p_acc[2]
	fout.write(json.dumps(output))
	fout.write('\t')
	fout.write(eval_p_r_f(predict_label, p_label))
	fout.write('\n')


if __name__ == '__main__':
	evaluation = 'evaluation.txt'
	output = {}
	train_vec, test_vec = ("result/train.vec", "result/test.vec")
	train_label, train_value = svm_read_problem(train_vec)  # 训练数据集
	predict_label, predict_value = svm_read_problem(test_vec)  # 预测数

	train_vec_scale, test_vec_scale = ("result/train_vec.scale", "result/test_vec.scale")
	# scale_exe = os.path.abspath('libsvm-3.22/windows/svm-scale.exe')
	# os.system('{} {} > {}'.format(scale_exe, os.path.abspath(train_vec), os.path.abspath(train_vec_scale)))
	# os.system('{} {} > {}'.format(scale_exe, os.path.abspath(test_vec), os.path.abspath(test_vec_scale)))
	train_scale_label, train_scale_value = svm_read_problem(train_vec_scale)  # 训练数据集
	predict_scale_label, predict_scale_value = svm_read_problem(test_vec_scale)  # 预测数

	fout = open(evaluation, 'a', encoding='utf-8')

	# 第一阶段
	# model = svm_train(train_label, train_value, '-q')  # 训练模型
	# p_label, p_acc, p_val = svm_predict(predict_label, predict_value, model)
	# save2file(p_acc, predict_label, p_label)
	#
	# # 第二阶段 数据缩放
	# model = svm_train(train_scale_label, train_scale_value, '-q')  # 训练模型
	# p_label, p_acc, p_val = svm_predict(predict_scale_label, predict_scale_value, model)
	# save2file(p_acc, predict_scale_label, p_label)

	# # 第三阶段 优化参数
	# params = get_params(train_vec)
	# model = svm_train(train_label, train_value, params)  # 训练模型
	# p_label, p_acc, p_val = svm_predict(predict_label, predict_value, model)
	# save2file(p_acc, predict_label, p_label)

	# 第四阶段  优化参数+ 数据缩放
	# params = get_params(train_vec_scale)
	# model = svm_train(train_scale_label, train_scale_value, params)  # 训练模型
	# p_label, p_acc, p_val = svm_predict(predict_scale_label, predict_scale_value, model)
	# svm_save_model("result/model.txt", model)  # 保存模型
	# save2file(p_acc, predict_scale_label, p_label)

	fout.close()
