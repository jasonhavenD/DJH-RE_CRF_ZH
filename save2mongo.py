#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:save_dbpedia2db
   Author:jasonhaven
   date:2018/4/19
-------------------------------------------------
   Change Activity:2018/4/19:
-------------------------------------------------
"""
import re
import sys
import datetime
from pymongo import MongoClient
from util.log import Logger
from util.io import IOHelper

logger = Logger().get_logger()

if __name__ == '__main__':
	input_triples = "result/triples.txt"

	client = MongoClient()
	client = MongoClient('127.0.0.1', 27017)
	db = client.relation_extraction  # 连接数据库，没有则自动创建
	triples = db.distant_supervised  # 使用集合，没有则自动创建

	triples_sents = IOHelper.read_lines(input_triples)
	triples_sents = list(set(triples_sents))

	if triples_sents == None:
		logger.error('read failed!')
		sys.exit(0)
	begin = datetime.datetime.now()
	try:
		count = 1
		for sent in triples_sents:
			if sent.strip() == '':
				continue
			doc = {}
			doc['e1'], doc['rel'], doc['e2'] = sent.strip().split('\t')
			if doc['rel'] == '中文名':  # 中文名字涉及的实体是一样的，所以过滤
				continue
			triples.insert(doc)
			logger.info('insert {} triples'.format(count))
			count += 1
	except Exception as e:
		logger.error(e)
	triples.ensure_index([("e1", 1)])
	triples.ensure_index([("e2", 1)])
	triples.ensure_index([("rel", 1)])
	triples.ensure_index([("e1", 1), ("e2", 1)])
	end = datetime.datetime.now()
	logger.info("finish in {}s.".format(end - begin))
