#!/usr/bin/env python
#coding=utf-8
# 
# Author:		xusongqi@live.com
# 
# Created Time: 2014年04月30日 星期三 14时46分18秒
# 
# FileName:     fork.py
# 
# Description:  

import os
from time import sleep

pid=os.fork()

if not pid:
	sleep(2)
	print "world"
else:
	print "hello"
	sleep(3)

