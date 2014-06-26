#!/usr/bin/env python
#conding=utf-8

import os
import string

command = "git --version"
os.system(command)

print(os.name)



def run(program, *args):
	#find executable
	for path in string.split(os.environ["PATH"], os.pathsep):
		file = os.path.join(path, program) + ".exe"

	try:
		return os.spawnv(os.P_WAIT, file, (file,) + args)
	except os.error:
		raise os.error, "cannot find executable"

if __name__ == "__main__":
	run("python", "replaceText")
	print("goodbye")