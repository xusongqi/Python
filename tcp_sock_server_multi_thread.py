#!/usr/bin/env python
#coding=utf-8
# 
# Author:		xusongqi@live.com
# 
# Created Time: 2014年04月30日 星期三 14时42分03秒
# 
# FileName:     tcp_sock_server_multi_thread.py
# 
# Description:  

from socket import *
from time import ctime
import traceback
import os
import sys

HOST = ''				#主机名为空，表示bind()可以绑定在所有的有效地址上
PORT = 21567			#端口号要和客户端一样
BUFSIZ = 1024			#缓冲区，此处设为和客户端一样大小
ADDR = (HOST, PORT)		#地址元组

tcp_server = socket(AF_INET, SOCK_STREAM)	#SOCK_STREAM：使用tcp协议
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)	#设置端口重用
tcp_server.bind(ADDR)		#bind()绑定地址元组，当前为绑定端口21567，允许所有访问该端口的主机访问服务端
tcp_server.listen(1)		#listen方法的参数指定了最大连接数

"""开启服务器"""
while True:		
	print 'waiting for connection...'	#启动反馈
	tcp_client, addr = tcp_server.accept()	#新的描述符接收来访的客户
	print '...connection from:',addr	#接收反馈
	
	"""fork子进程"""
	pid = os.fork()
	if not pid:		#pid=0：子进程	
		while True:		#死循环代表了长连接
			tcp_server.close()	#关闭服务端描述符
			data = tcp_client.recv(BUFSIZ)	#接收客户端信息
			if not data:	#为空则断开
				break
			tcp_client.send('[%s]%s' % (ctime(), data))	#返回带时间戳的回执
		tcp_client.close()	#关闭客户端描述符
		sys.exit(0)
	else:	#父进程
		tcp_client.close()	#关闭客户端描述符

tcp_server.close()
