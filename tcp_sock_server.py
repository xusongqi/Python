#!/usr/bin/env python
#coding=utf-8
# 
# Author:		xusongqi@live.com
# 
# Created Time: 2014年04月21日 星期一 11时59分44秒
# 
# FileName:     tcp_sock_server.py
# 
# Description:  单线程tcp套结字服务端

from socket import *
from time import ctime

HOST = ''				#主机名为空，表示bind()可以绑定在所有的有效地址上
PORT = 21567			#端口号要和客户端一样
BUFSIZ = 1024			#缓冲区，此处设为和客户端一样大小
ADDR = (HOST, PORT)		#地址元组

tcp_sock_server = socket(AF_INET, SOCK_STREAM)	#SOCK_STREAM：使用tcp协议
tcp_sock_server.bind(ADDR)		#bind()绑定地址元组，当前为绑定端口21567，允许所有访问该端口的主机访问服务端
tcp_sock_server.listen(5)		#listen方法的参数指定了最大连接数

while True:		#开启服务器
	print 'waiting for connection...'	#启动反馈
	tcp_sock_client, addr = tcp_sock_server.accept()	#新的描述符接收来访的客户
	print '...connection from:',addr	#接收反馈

	while True:		#死循环代表了长连接
		data = tcp_sock_client.recv(BUFSIZ)	#接收客户端信息
		if not data:	#为空则断开
			break
		tcp_sock_client.send('[%s]%s' % (ctime(), data))	#返回带时间戳的回执

	tcp_sock_client.close()	#关闭客户端描述符
tcp_sock_server.close()	#关闭服务端描述符
