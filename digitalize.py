#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:dignitalize
   Author:jasonhaven
   date:2018/4/27
-------------------------------------------------
   Change Activity:2018/4/27:
-------------------------------------------------
"""
import pickle
import pandas as pd


def digitalize_with_dict(feature, key, dict):
	if feature[key] in dict:
		return dict.index(feature[key])
	return -1


if __name__ == '__main__':
	features_file = 'result/features.pickle'
	rels_dict_file = 'dict/rels.dict'
	entities_dict_file = 'dict/entities.dict'
	postag_dict_file = 'dict/postags.dict'
	nes_dict_file = 'dict/nes.dict'

	feature_vec = 'result/features.vec'
	feature_vec_file = 'result/features.vec.csv'

	with open(features_file, 'rb') as f:
		features = pickle.load(f)

	with open(rels_dict_file, 'r', encoding='utf-8') as f:
		rels_dict = [word.strip() for word in f.readlines()]

	with open(entities_dict_file, 'r', encoding='utf-8') as f:
		entities_dict = [word.strip() for word in f.readlines()]

	with open(postag_dict_file, 'r', encoding='utf-8') as f:
		postag_dict = [word.strip() for word in f.readlines()]

	with open(nes_dict_file, 'r', encoding='utf-8') as f:
		nes_dict = [word.strip() for word in f.readlines()]

	vectors = []
	for feature in features:
		vec = {'rel': -1, 'E1-0': -1, 'NE1-0': -1, 'POS1-0': -1, 'POS1-2': -1, 'POS1-1': -1,
		       'POS1+1': -1, 'POS1+2': -1, 'E2-0': -1, 'NE2-0': -1, 'POS2-0': -1,
		       'POS2-2': -1, 'POS2-1': -1, 'POS2+1': -1, 'POS2+2': -1}
		# 设置关系
		if feature['rel'] in rels_dict:
			vec['rel'] = rels_dict.index(feature['rel'])
		# 设置实体
		entities_lst = ['E1-0', 'E2-0']
		for k in entities_lst:
			vec[k] = digitalize_with_dict(feature, k, entities_dict)
		# 设置词性
		postag_lst = ['POS1-0', 'POS1-2', 'POS1-1', 'POS1+1', 'POS1+2', 'POS2-0', 'POS2-2', 'POS2-1', 'POS2+1',
		              'POS2+2']
		for k in postag_lst:
			vec[k] = digitalize_with_dict(feature, k, postag_dict)
		# 设置实体标记
		nes_lst = ['NE1-0', 'NE2-0']
		for k in nes_lst:
			vec[k] = digitalize_with_dict(feature, k, nes_dict)
		vectors.append(vec)
	# print(vec)

	data = []
	for vec in vectors:
		data.append(list(vec.values()))
	df = pd.DataFrame(data=data, columns=list(vec.keys()))
	df.to_csv(feature_vec_file, encoding='utf-8')
