#!/usr/bin/env python
#coding=utf-8
# 
# Author:		xusongqi@live.com
# 
# Created Time: 2014年04月30日 星期三 13时19分56秒
# 
# FileName:     tcp_sock_client.py
# 
# Description: 单线程tcp套结字客户端 

from socket import *

HOST = 'localhost'	#主机名
PORT = 21567		#端口号，显然要和客户端的端口号保持一致
BUFSIZ = 1024		#缓冲区大小设为1K
ADDR = (HOST, PORT)	#地址为主机名和端口号组成的元组

tcp_sock_client = socket(AF_INET, SOCK_STREAM)	#SOCK_STREAM即选择连接为tcp
tcp_sock_client.connect(ADDR)	#使用connect函数进行连接

#循环发送与接收，从这句话看这个套结字是个长连接
while True:		
	data = raw_input('>')
	if not data:	#如果没有写入数据，跳出循环并断开连接
		break
	tcp_sock_client.send(data)	#将数据发送到服务端
	data = tcp_sock_client.recv(BUFSIZ)	#接收从服务器发来的带时间戳的返回信息
	if not data:	#如果从服务器收到的信息为空：跳出循环并断开连接
		break
	print data		#打印服务器发来的信息

tcp_sock_client.close()	#断开连接
