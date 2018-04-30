#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:log
   Author:jasonhaven
   date:2018/4/17
-------------------------------------------------
   Change Activity:2018/4/17:
-------------------------------------------------
"""
import logging
import os
import datetime
import shutil
import codecs

_logs = "logs"
_filefmt = os.path.join(_logs, "%Y-%m-%d.log")


class LoggerHandler(logging.Handler):
	def __init__(self, filefmt=None):
		self.filefmt = filefmt
		if filefmt is None:
			self.filefmt = _filefmt
		logging.Handler.__init__(self)

	def emit(self, record):
		msg = "{} {} {} : {}".format(datetime.datetime.now().strftime("%H:%M:%S"), os.path.abspath(__file__).split(os.sep)[-1], record.levelname,
		                             record.getMessage())
		_filePath = datetime.datetime.now().strftime(self.filefmt)
		_dir = os.path.dirname(_filePath)
		try:
			if os.path.exists(_dir) is False:
				os.makedirs(_dir)
		except Exception:
			print("can not make dirs")
			print("filepath is " + _filePath)
			pass
		try:
			_fobj = codecs.open(_filePath, 'a',encoding='utf-8')
			_fobj.write(msg)
			_fobj.write("\n")
			_fobj.flush()
			_fobj.close()
		except Exception:
			print("can not write to file")
			print("filepath is " + _filePath)
			pass


class Logger():
	def __init__(self, isclean=False):
		'''
		:param isclean:是否清空日志
		'''
		self.logging_format = '[%(levelname)s %(asctime)s %(module)s:%(lineno)d]: %(message)s'
		self.date_format = '%y-%m-%d %H:%M:%S'
		self.filehandler = LoggerHandler()
		if isclean:
			if os.path.exists(_logs):
				self.clean_logs()

	def get_logger(self):
		logging.basicConfig(
			level=logging.INFO,
			format=self.logging_format,
			datefmt=self.date_format
		)
		logger = logging.getLogger("logger")
		logger.addHandler(self.filehandler)
		return logger

	def clean_logs(self):
		delDir = _logs
		delList = os.listdir(delDir)
		for f in delList:
			filePath = os.path.join(delDir, f)
			if filePath and os.path.isfile(filePath):
				os.remove(filePath)
				print(filePath + " was removed!")
			elif filePath and os.path.isdir(filePath):
				shutil.rmtree(filePath, True)
				print("Directory: " + filePath + " was removed!")


if __name__ == '__main__':
	logger = Logger(True).get_logger()
	logger.info("info")
	logger.debug("debug")
	logger.error("error")
