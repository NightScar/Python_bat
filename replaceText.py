#!/usr/bin/env python
#conding=utf-8

import os
import string

def replace(file, search_for, replace_with):
	#replace string in a text file
	back = os.path.splitext(file)[0] + ".bak"
	temp = os.path.splitext(file)[0] + ".tmp"

	try:
		#remove old temp file, if any
		os.remove(temp)
	except os.error:
		pass

	fi = open(file)
	fo = open(temp, "w")

	for s in fi.readlines():
		fo.write(string.replace(s, search_for, replace_with))

	fi.close()
	fo.close()

	try:
		#remove old backup file, if any
		os.remove(back)
	except os.error:
		pass

	#remane original to backup...
	os.rename(file,back)

	# ...any temporary to original
	os.rename(temp,file)


if __name__ == "__main__":
	fp = raw_input("Please Enter File Path:")
	sf = raw_input("Please Enter search_for:")
	rw = raw_input("Please Enter replace_with:")
	replace(fp,sf,rw)