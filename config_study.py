#!/usr/bin/env python
#conding=utf-8

import os
import string
import ConfigParser

file = "config_Father.ini"

cfg = ConfigParser.ConfigParser()

cfg.read(file)

s = cfg.sections()
print "sections:",s

o = cfg.options('host')
print "options:",o

v = cfg.items("host")
print "host:",v

print '-'*60
host_name = cfg.get("host","name")
print("host name:",host_name)

cfg.set("git remote","time","9:00")
cfg.write(open(file,'w'))