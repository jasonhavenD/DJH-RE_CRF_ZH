#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:feature
   Author:jasonhaven
   date:2018/4/27
-------------------------------------------------
   Change Activity:2018/4/27:
-------------------------------------------------
"""
import pickle


def set_entity_pos(num, feature, entity, index, sent, is_entity=False):
	if is_entity:
		feature['E' + str(num)] = entity
		feature['NE' + str(num)] = sent[index].split('/')[2]
	feature['POS' + str(num)] = sent[index].split('/')[1]


'''
特征加入相对位置
ORDER
0:e1 e2
1:e2 e1
'''

if __name__ == '__main__':
	input = '../corpora/sents_with_pos.txt'
	features_file = '../result/features.pickle'

	with open(input, 'r', encoding='utf-8') as f:
		rows = f.readlines()

	features = []
	for row in rows:  # 关系
		feature = { 'ORDER': '0','rel': 'None', 'E1-0': 'None', 'NE1-0': 'None', 'POS1-0': 'None', 'POS1-2': 'None', 'POS1-1': 'None',
		           'POS1+1': 'None', 'POS1+2': 'None', 'E2-0': 'None', 'NE2-0': 'None', 'POS2-0': 'None',
		           'POS2-2': 'None', 'POS2-1': 'None', 'POS2+1': 'None', 'POS2+2': 'None'}

		pre, sent = row.strip().split('||')
		rel, E1, E2, b1, e1, b2, e2 = pre.strip().split('\t')
		b1, e1, b2, e2 = int(b1), int(e1), int(b2), int(e2)

		# 设置相对位置
		if b1 < b2:
			feature['ORDER'] = '0'
		else:
			feature['ORDER'] = '1'

		# 设置关系
		feature['rel'] = rel
		sent = sent.strip().split('\t')
		# 设置实体1
		set_entity_pos('1-0', feature, E1, b1, sent, True)
		# 设置实体1左2
		if b1 >= 2:
			index = b1 - 2
			e = sent[index].split('/')[0]
			set_entity_pos('1-2', feature, e, index, sent)
		# 设置实体1左1
		if b1 >= 1:
			index = b1 - 1
			e = sent[index].split('/')[0]
			set_entity_pos('1-1', feature, e, index, sent)
		# 设置实体1右1
		if e1 < len(sent) - 1:
			index = e1 + 1
			e = sent[index].split('/')[0]
			set_entity_pos('1+1', feature, e, index, sent)
		# 设置实体1右2
		if e1 < len(sent) - 2:
			index = e1 + 2
			e = sent[index].split('/')[0]
			set_entity_pos('1+2', feature, e, index, sent)

		# 设置实体2
		set_entity_pos('2-0', feature, E2, b2, sent, True)
		# 设置实体2左2
		if b2 >= 2:
			index = b2 - 2
			e = sent[index].split('/')[0]
			set_entity_pos('2-2', feature, e, index, sent)
		# 设置实体2左1
		if b2 >= 1:
			index = b2 - 1
			e = sent[index].split('/')[0]
			set_entity_pos('2-1', feature, e, index, sent)
		# 设置实体2右1
		if e2 < len(sent) - 1:
			index = e2 + 1
			e = sent[index].split('/')[0]
			set_entity_pos('2+1', feature, e, index, sent)
		# 设置实体2右2
		if e2 < len(sent) - 2:
			index = e2 + 2
			e = sent[index].split('/')[0]
			set_entity_pos('2+2', feature, e, index, sent)
		features.append(feature)
		print(feature)

	with open(features_file, 'wb') as f:
		pickle.dump(features, f)
