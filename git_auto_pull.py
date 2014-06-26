#!/usr/bin/env python
#coding=utf-8

import os
import string
import ConfigParser

def Ensure_Operate_Dir():
	path = raw_input("输入文件夹位置：")
	if path == "here":
		return os.getdir()
	else:
		os.chdir(path)
		return path


def Get_Repo_Name(filename):
	#读取要同步的仓库名字
	cfg = ConfigParser.ConfigParser()
	cfg.optionxform = str
	cfg.read(filename)

	opt = cfg.options("repo")
	# print "rp is ",opt
	deal = []
	for rp in opt:
		if cfg.get("repo",rp) == '1':
			deal.append(rp)
	return deal

def Check_Repo_Exists(input, exist, not_exist, path):
	#检查是否存在
	for rp in input:
		if os.path.exists(path + '\\' + rp):
			exist.append(rp)
		else:
			not_exist.append(rp)

def test():
	path = Ensure_Operate_Dir()
	fn = "config.ini"
	rp_name = Get_Repo_Name(fn)
	ex_name = []
	not_ex_name = []
	Check_Repo_Exists(rp_name, ex_name, not_ex_name, path)
	remote_ip = Get_Remote_Ip(fn)
	git_Clone(not_ex_name,remote_ip)

def git_Clone(new_repo,ip):
	for rp in new_repo:
		command = "git clone git@" + ip + ":" + rp + ".git"
		print(command)
		os.system(command)

def Get_Remote_Ip(filename):
	cfg = ConfigParser.ConfigParser()
	cfg.read(filename)
	return cfg.get("config","Server_Ip")

if __name__ == '__main__':
	# main()
	test()

