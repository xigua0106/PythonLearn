# -*- coding: utf-8 -*-
import sys, os
import subprocess
import hashlib
import ctypes
import json
import logging
from .FileUtil import FileUtil

# 版本信息
class VersionInfo():
    pass

# 帮助库
class LogHelper:
	# 生成MD5
	@staticmethod
	def CalcMD5(fullname):
		ret = ''
		with open(fullname, 'rb') as fp:
			md5obj = hashlib.md5()
			md5obj.update(fp.read())
			ret = md5obj.hexdigest()

		return ret

	# 遍历文件夹
	@staticmethod
	def ErgodicDir(path, fileList, ignoreFiles = []):
		files = os.listdir(path)
		
		for f in files :
			fullpath = ''
			if path == './':
				fullpath = f
			else:
				fullpath = path + '/' + f

			if os.path.isdir(fullpath):
				if f[0] != '.' :
					fileList.append(fullpath)
					Helper.ErgodicDir(fullpath, fileList, ignoreFiles)
			else:
				if not f in ignoreFiles:
					fileList.append(fullpath)

	#版本信息
	@staticmethod
	def GetVersionInfo():
		info = VersionInfo()
		info.version 		= "1.01.001"
		info.versionMain 	= "ios_release_101"
		info.name 			= "dk"
		info.target 		= "test"

		filename = FileUtil.PathTo(os.getcwd()+"/../version/updatePackage/version")
		if os.path.exists(filename):
			content = FileUtil.ReadFile(filename)
			verJson = json.loads(content)
			name = verJson['name']
			version = verJson['version']

			arrCode = version.split('.')
			info.version = version
			info.versionMain = "%s_release_%s%s"%(name, arrCode[0], arrCode[1])

			if verJson.has_key('target_name'):
				info.name = verJson['target_name']

			if verJson.has_key('target'):
				info.target = verJson['target']

		return info

	@staticmethod
	def InitLog():
		if not os.path.exists('log'):
			os.makedirs('log')

		logging.basicConfig(level=logging.INFO,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='log/myapp.log',
            filemode='w')
		console = logging.StreamHandler()
		console.setLevel(logging.INFO)
		formatter = logging.Formatter('%(levelname)-8s %(message)s')
		console.setFormatter(formatter)
		logging.getLogger('').addHandler(console)

	# 调用外部命令
	@staticmethod
	def CallCommand(cmd):
		return subprocess.call(cmd, shell=True)


