#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:visualization_evaluation
   Author:jasonhaven
   date:2018/4/30
-------------------------------------------------
   Change Activity:2018/4/30:
-------------------------------------------------
"""
import json
import matplotlib

if __name__ == '__main__':
	input = 'evaluation.txt'
	with open(input, 'r', encoding='utf-8') as f:
		text = f.readlines()
	data={}
	data['baeline'] = json.loads(text[0].strip())
	data['numeric sacle'] = json.loads(text[0].strip())
	data['numeric scale&params optimization'] = json.loads(text[0].strip())