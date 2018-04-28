#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:test
   Author:jasonhaven
   date:2018/4/27
-------------------------------------------------
   Change Activity:2018/4/27:
-------------------------------------------------
"""
import re
from stanfordcorenlp import StanfordCoreNLP


def split(rows):
	rels = []
	E1s = []
	E2s = []
	E1_begin_ends = []
	E2_begin_ends = []
	sents = []
	for row in rows:
		rel, E1, E2, b1, e1, b2, e2, sent = row.strip().split('\t')
		E1s.append(E1)
		E2s.append(E2)
		rels.append(rel)
		E1_begin_ends.append(b1 + '\t' + e1)
		E2_begin_ends.append(b2 + '\t' + e2)
		sents.append(sent)
	return rels, E1s, E2s, E1_begin_ends, E2_begin_ends, sents


if __name__ == '__main__':
	# 关系，实体1,实体1开始、实体1结束，实体2，实体2开始，实体2结束，句子
	input = 'corpora/corpus1.txt'

	rels_dict = 'dict/rels.dict'
	entities_dict = 'dict/entities.dict'
	postags_dict = 'dict/postags.dict'
	nes_dict = 'dict/nes.dict'

	sents_with_pos = 'corpora/sents_with_pos.txt'
	sents_file = 'corpora/sents.txt'

	nlp = StanfordCoreNLP("c:/stanford-corenlp-full-2018-02-27", lang='zh')

	with open(input, 'r', encoding='utf-8') as f:
		rows = f.readlines()[:1000]

	rels, E1s, E2s, E1_begin_ends, E2_begin_ends, sents = split(rows)

	# '''
	# 生成关系字典
	# '''
	# rels = sorted(list(set(rels)))
	# with open(rels_dict, 'w', encoding='utf-8') as f:
	# 	f.writelines('\n'.join(rels))
	#
	# print('saveed {}'.format('rels'))
	#
	# '''
	# 生成实体字典
	# '''
	# entities = sorted(list(set(E1s + E2s)))
	# with open(entities_dict, 'w', encoding='utf-8') as f:
	# 	f.writelines('\n'.join(entities))
	#
	# print('saveed {}'.format('entities'))

	'''
	生成word+postag+netag
	'''
	postags_lst = set()
	ne_lst = set()
	sentences = []
	with open(sents_with_pos, 'w', encoding='utf-8') as f:
		for i in range(len(rels)):
			line = ''
			rel = rels[i]
			E1 = E1s[i]
			E2 = E2s[i]
			E1_b_e = E1_begin_ends[i]
			E2_b_e = E2_begin_ends[i]
			sent = sents[i]
			line += rel + '\t'
			line += E1 + '\t'
			line += E2 + '\t'
			line += E1_b_e + '\t'
			line += E2_b_e + '\t'
			line += '||'
			p = re.compile("\[?\]?'?")
			tokens = re.sub(p, '', sent).split(', ')
			words = [t.split('/')[0] for t in tokens]
			tags = [t.split('/')[1] for t in tokens]
			string = ' '.join(words)
			postags = nlp.pos_tag(string)
			row = []
			for postag, tag in zip(postags, tags):
				row.append('/'.join([postag[0], postag[1], tag]))
				postags_lst.add(postag[1])
				ne_lst.add(tag)
			line += '\t'.join(row) + '\n'
			f.write(line)
			sentences.append(string.replace(' ', ''))
	print('saveed {}'.format('word_pos_ne'))
	# '''
	# 生成词性字典
	# '''
	# with open(postags_dict, 'w', encoding='utf-8') as f:
	# 	postags_lst = sorted(list(postags_lst))
	# 	f.writelines('\n'.join(postags_lst))
	# print('saveed {}'.format('postag_lst'))
	# '''
	# 生成实体标注字典
	# '''
	# with open(nes_dict, 'w', encoding='utf-8') as f:
	# 	ne_lst = sorted(list(ne_lst))
	# 	f.writelines('\n'.join(ne_lst))
	# print('saveed {}'.format('ne_lst'))

	'''
	生成原来句子
	'''
	with open(sents_file, 'w', encoding='utf-8') as f:
		f.writelines('\n'.join(sentences))
	print('saveed {}'.format('sents_file'))