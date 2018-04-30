#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:neo4j
   Author:jason
   date:18-4-23
-------------------------------------------------
   Change Activity:18-4-23:
-------------------------------------------------
"""
import datetime
from pymongo import MongoClient
from py2neo import Graph, Node, Relationship


def init():
	# create from mongodb.ne_triples
	cursor = triples.find()
	insert_triples(cursor)


# def clean():
# 	statement = '''match(n) optional match(n)-[r]-() delete n,r'''
# 	graph.run(statement)


def insert_triples(triples):
	'''
	triple={'e1':value,'e2':value,'rel':value}
	'''
	for triple in triples:
		e1 = triple['e1'].strip()
		e2 = triple['e2'].strip()
		if len(e1) < 2 or len(e2) < 2:
			continue
		rel = triple['rel'].strip()
		e1_node = Node('Sub', name=e1)
		e2_node = Node('Obj', name=e2)
		# find first
		exist_e1_node = graph.find_one('Sub', 'name', e1)
		exist_e2_node = graph.find_one('Obj', 'name', e2)
		if exist_e1_node != None:
			e1_node = exist_e1_node
		if exist_e2_node != None:
			e2_node = exist_e2_node
		relation_node = Relationship(e1_node, rel, e2_node)
		all = e1_node | e2_node | relation_node
		graph.create(all)


def query_by_node(name):
	# find node either is Sub or Obj
	statement1 = "match (e1:Sub {name:'%s'})-[r]-(e2) return e1,r,e2" % name
	statement2 = "match (e1)-[r]-(e2:Obj {name:'%s'}) return e1,r,e2" % name

	result1 = graph.run(statement1).data()
	result2 = graph.run(statement2).data()

	lst = []
	for rst in result1:
		e1, rel, e2 = rst['e1'], rst['r'], rst['e2']
		# print(e1['name'], rel.type(), e2['name'])
		dct = {}
		dct['e1'] = e1['name']
		dct['rel'] = rel.type()
		dct['e2'] = e2['name']
		lst.append(dct)
	return lst


def query_by_relation(relation):
	lst = []
	results = graph.match(rel_type=relation)
	for rst in results:
		e1, e2 = rst.nodes()
		dct = {}
		dct['e1'] = e1['name']
		dct['rel'] = relation
		dct['e2'] = e2['name']
		lst.append(dct)
	return lst


if __name__ == '__main__':
	begin = datetime.datetime.now()
	graph = Graph('http://172.19.12.30:7474/db/data', username='neo4j', password='root')
	client = MongoClient()
	client = MongoClient('172.19.12.30', 27017)
	db = client.relation_extraction  # 连接数据库，没有则自动创建
	triples = db.distant_supervised  # 使用集合，没有则自动创建

	cursor = triples.find()
	insert_triples(cursor)

	end = datetime.datetime.now()
	print("finish in {}s.".format(end - begin))
