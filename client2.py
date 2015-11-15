import sys
import select
import socket

PORT=5003
HOST='127.0.0.1'
BUFFER_MAX=1024

def client():
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.connect((HOST,PORT))
	print 'connected...'
	while 1:
		rlist,wlist,elist=select.select([sys.stdin,client_socket],[],[])
		for s in rlist:
			if s is client_socket:
				data=s.recv(BUFFER_MAX)
				print data
			else:
				message=raw_input()
				client_socket.send(message)
	client_socket.close()
		
client()
