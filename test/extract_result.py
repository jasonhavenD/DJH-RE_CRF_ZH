#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:count_entities
   Author:jasonhaven
   date:18-6-1
-------------------------------------------------
   Change Activity:18-6-1:
-------------------------------------------------
"""

import pandas as pd
import datetime
from pymongo import MongoClient
from util.log import Logger
logger = Logger().get_logger()


if __name__ == '__main__':
	client = MongoClient()
	client = MongoClient('127.0.0.1', 27017)
	db = client.relation_extraction  # 连接数据库，没有则自动创建
	distant_supervised = db.distant_supervised  # 使用集合，没有则自动创建
	begin = datetime.datetime.now()
	cursor=distant_supervised.find()

	df=pd.DataFrame()
	rels=[]
	e1s=[]
	e2s=[]
	dicts={}
	for tpl in cursor:
		e1,rel,e2=tpl['e1'],tpl['rel'],tpl['e2']
		e1s.append(e1)
		e2s.append(e2)
		rels.append(rel)
		if rel not in dicts.keys():
			dicts[rel]=1
		else:
			dicts[rel] +=1

	print(len(e1s),len(e2s),len(rels))

	#保存三元组
	# df['e1']= e1s
	# df['e2'] = e2s
	# df['rel'] = rels
	# df.to_csv('./extract_rels.csv',sep=',',encoding='utf-8')

	#保存全部实体
	print(len(e1s+e2s))
	print(len((set(e1s+e2s))))

	#保存全部关系
	print(len(rels))
	print(len((set(rels))))

	#保存关系和频数
	# print(len(dicts.items()))
	# print(len(dicts.items()))
	# df['rel'] = dicts.keys()
	# df['value'] = dicts.values()
	# df.to_csv('./rel_values.csv', sep=',', encoding='utf-8')

	end = datetime.datetime.now()
	logger.info("finish in {}s.".format(end - begin))
