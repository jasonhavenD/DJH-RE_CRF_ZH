#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:io
   Author:jasonhaven
   date:2018/4/17
-------------------------------------------------
   Change Activity:2018/4/17:
-------------------------------------------------
"""
import codecs
import os


class IOHelper():
	@classmethod
	def read(cls, file):
		if os.path.exists(file):
			return codecs.open(file, 'r', encoding='utf-8').read()
		else:
			return None

	@classmethod
	def read_lines(cls, file):
		if os.path.exists(file):
			return codecs.open(file, 'r', encoding='utf-8').readlines()
		else:
			return None

	@classmethod
	def write(cls, file, text):
		with codecs.open(file, 'w', encoding='utf-8') as f:
			f.write(text)

	@classmethod
	def write_lines(cls, file, sents):
		with codecs.open(file, 'w', encoding='utf-8') as f:
			f.writelines('\n'.join(sents))

	@classmethod
	def write_tokenses(cls, file, tokenses):
		with codecs.open(file, 'w', encoding='utf-8') as f:
			for tokens in tokenses:
				f.write('\t'.join(tokens))  # [token,token,token...]
				f.write("\n")

	@classmethod
	def write_triples(cls, file, triples_sents):
		with codecs.open(file, 'w', encoding='utf-8') as f:
			for triples in triples_sents:
				if triples == []:
					continue
				f.write('\n'.join(triples))
				f.write('\n')


if __name__ == '__main__':
	input = "D:\github\A_DJH\DJH-OpenRE\chinese\data\\raw\chinaautonews.txt"
	output = "test2.py"

	text = IOHelper.read(input)
	print(text[:10])
