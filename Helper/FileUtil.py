# -*- coding: utf-8 -*-
import sys, os
import shutil
import logging as Log
import re

#小写名字是shutil库接口的重写，基本只是做了路劲转换
#camel命名的是二次封装的工具接口

# 文件帮助库
class FileUtil():
	#读取文件内容，用于文件做简单配置的情况
	@staticmethod
	def ReadFile(filename):
		f = open(filename)
		ctx = f.read()
		f.close()
		return ctx
	
	@staticmethod
	def makedirs(path):
		path = os.path.normcase(path)
		os.makedirs(path)

	#删除目录下的所有内容
	@staticmethod
	def rmtree(path):
		path = os.path.normcase(path)
		if os.path.exists(path):
			Log.info("Help.rmtree:%s======"%path)
			shutil.rmtree(path)
		else:
			Log.info("Help.rmtree:%s, path not exist"%path)

	#删除满足条件的文件
	@staticmethod
	def RmMatchFiles(dstPath, strPattner, includeChild = False):
		fileList = FileUtil.GetMatchFiles(dstPath, strPattner, includeChild)
		for file in fileList:
			os.remove(file)

	#删除满足条件的文件夹
	@staticmethod
	def RmMatchPaths(dstPath, strPattner):
		pathList = FileUtil.GetMatchPaths(dstPath, strPattner, False)
		for file in pathList:
			FileUtil.rmtree(file)

	#移动文件（目录） 目录的情况：newpos不存在的话，oldpos会变成newpos的名字，如果存在变成newpos的子目录
	@staticmethod
	def move(fromPath, toPath):
		fromPath = os.path.normcase(fromPath)
		if not os.path.exists(fromPath):
			Log.warning("========FileUtil.move, fromPath:%s is not exist========"%fromPath)
			return
		toPath = os.path.normcase(toPath)
		shutil.move(fromPath, toPath)


	#移动满足条件的文件到目录
	@staticmethod
	def MoveMatchFiles(fromPath, strPattner, toPath, includeChild = False):
		fileList = FileUtil.GetMatchFiles(fromPath, strPattner, includeChild)
		toPath = os.path.normcase(toPath)
		for file in fileList:
			shutil.move(file, toPath)

	#移动满足条件的目录到目录
	@staticmethod
	def MoveMatchPathes(fromPath, strPattner, toPath):
		pathList = FileUtil.GetMatchPaths(fromPath, strPattner, False)
		toPath = os.path.normcase(toPath)
		for file in pathList:
			shutil.move(file, toPath)


	#复制目录下的所有内容 fromPath和topath都只能是目录，且topath必须不存在
	#如果topath中已经有内容，可以使用MergePath接口
	@staticmethod
	def copytree(fromPath, topath, includeSelf = False):
		
		fromPath = os.path.normcase(fromPath)
		if not os.path.exists(fromPath):
			Log.warning("========FileUtil.copytree, fromPath:%s is not exist========"%fromPath)
			return

		Log.info("Help.copytree:%s-->%s======"%(fromPath, topath))

		if includeSelf:
			selfname = fromPath.split(os.sep)[-1]
			topath  +=  os.sep
			topath += selfname

		topath = os.path.normcase(topath)
		if os.path.exists(topath):
			shutil.rmtree(topath)
		shutil.copytree(fromPath, topath)

	#复制文件，fromPath 和 topath只能是文件
	@staticmethod
	def copyfile(fromPath, topath):
		#Log.info("Help.copyfile:%s-->%s======"%(fromPath, topath))
		fromPath = os.path.normcase(fromPath)
		if not os.path.exists(fromPath):
			Log.warning("========FileUtil.copyfile, fromPath:%s is not exist========"%fromPath)
			return

		topath = os.path.normcase(topath)
		shutil.copyfile(fromPath, topath)

	#复制一个文件到一个文件或一个目录
	@staticmethod
	def copy(fromPath, topath):
		#Log.info("Help.copy:%s-->%s======"%(fromPath, topath))
		fromPath = os.path.normcase(fromPath)
		if not os.path.exists(fromPath):
			Log.warning("========FileUtil.copy, fromPath:%s is not exist========"%fromPath)
			return

		topath = os.path.normcase(topath)
		if not os.path.exists(topath):
			os.mkdir(topath)
		shutil.copy(fromPath, topath)

	#复制目录下 满足正则表达式规则的目录到目标路径
	@staticmethod
	def CopyMatchPaths(fromPath, strPattner, toPath, includeChild=False):
		pathlist = FileUtil.GetMatchPaths(fromPath, strPattner, includeChild)
		toPath = os.path.normcase(toPath)
		for path in pathlist:
			FileUtil.copytree(path, toPath, includeSelf = True)
	
	#复制目录下 满足正则表达式规则的文件到目标路径
	@staticmethod
	def CopyMatchFiles(fromPath, strPattner, toPath, includeChild = False):
		fileList = FileUtil.GetMatchFiles(fromPath, strPattner, includeChild)
		toPath = os.path.normcase(toPath)
		for file in fileList:
			shutil.copy(file, toPath)
	

	#根据正则表达式匹配路径，不匹配文件, strPattner是正则表达式字符串，includeChild 是否匹配子目录，默认不匹配
	@staticmethod
	def GetMatchPaths(srcPath, strPattner, includeChild=False):
		srcPath = os.path.normcase(srcPath)
		pattner = re.compile(strPattner)
		return FileUtil.GetPattnerPaths(srcPath, pattner, includeChild)

	#pattner是正则表达式
	@staticmethod
	def GetPattnerPaths(srcPath, pattner, includeChild):
		fileList = os.listdir(srcPath)
		result = []
		for file in fileList:
			filename = srcPath + os.sep + file
			if not os.path.isdir(filename):
				continue
			if pattner.search(file):
				result.append(filename)
			if includeChild:
				childPaths = result.extend(FileUtil.GetPattnerPaths(filename, pattner, includeChild))
				result = result + childPaths
		return result

	#根据正则表达式匹配文件, strPattner是正则表达式字符串，includeChild 是否匹配子目录，默认不匹配
	@staticmethod
	def GetMatchFiles(srcPath, strPattner, includeChild=False):
		srcPath = os.path.normcase(srcPath)
		pattner = re.compile(strPattner)
		return FileUtil.GetPattnerFiles(srcPath, pattner, includeChild)

	#pattner是正则表达式
	@staticmethod
	def GetPattnerFiles(srcPath, pattner, includeChild):
		fileList = os.listdir(srcPath)
		result = []
		for file in fileList:
			filename = srcPath + os.sep + file
			if os.path.isfile(filename):
				#print("deal file:"+file)
				if pattner.search(file):
					result.append(filename)
			elif includeChild and os.path.isdir(filename):
				childFiles = FileUtil.GetPattnerFiles(filename, pattner, includeChild)
				result = result + childFiles
		return result

	#合并目录，将fromPath目录的内如合并到topath
	@staticmethod
	def MergePath(fromPath, toPath):
		if not os.path.exists(toPath):
			os.mkdir(toPath)
		fileList = os.listdir(fromPath)
		for filename in fileList:
			fromFile = fromPath + os.sep + filename
			toFile = toPath + os.sep + filename
			if os.path.isdir(fromFile):
				FileUtil.MergePath(fromFile, toFile)
			else:
				FileUtil.copyfile(fromFile, toFile)

	#将合并过来的内容删除
	#disPath 需要DisMerge的目录
	#refPath 原来Merge过来的目录，作为剔除的依据
	@staticmethod
	def DisMergePath(disPath, refPath):
		if not os.path.exists(disPath):
			Log.warning('DisMergePath:%s not exist'%disPath)
			return 
		refList = os.listdir(refPath)
		for name in refList:
			refFile = refPath + os.sep + name
			disFile = disPath +os.sep + name
			if os.path.isdir(refFile):
				FileUtil.DisMergePath(disFile, refFile)
			elif os.path.exists(disFile):
				os.remove(disFile)
		newlist = os.listdir(disPath)
		if len(newlist)==0:
			os.rmdir(disPath)

	@staticmethod
	def MergeList(fromList, toList):
		if not fromList or not toList :
			return
		for item in fromList:
			toList.append(item)
