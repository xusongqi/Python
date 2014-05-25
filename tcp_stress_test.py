#!/usr/bin/env python
#coding=utf-8
# 
# Author:		xusongqi@live.com
# 
# Created Time: 2014年05月25日 星期日 21时17分28秒
# 
# FileName:     tcp_stress_test.py
# 
# Description:  

import math
from socket import *
import os

HOST = 'localhost'	#主机名
PORT = 21567		#端口号，显然要和客户端的端口号保持一致
BUFSIZ = 1024		#缓冲区大小设为1K
ADDR = (HOST, PORT)	#地址为主机名和端口号组成的元组

tcp_sock_client = socket(AF_INET, SOCK_STREAM)	#SOCK_STREAM即选择连接为tcp
tcp_sock_client.connect(ADDR)	#使用connect函数进行连接

for n in range(20):
	os.fork()
	#循环发送与接收，从这句话看这个套结字是个长连接
	while True:		
		data = "test msg\n"
		tcp_sock_client.send(data)	#将数据发送到服务端

tcp_sock_client.close()	#断开连接
