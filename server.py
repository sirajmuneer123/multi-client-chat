# multi client chating 
import sys
import socket
import select

HOST="127.0.0.1"
PORT=5003
DATA_BUFFER=1024
SOCKET_LIST=[]
BROADCAST_LIST=[]

def broadcast_data(sock,message):
	for socket in BROADCAST_LIST:
		if socket != sock:
			socket.send(message)


def server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	
	server_socket.bind((HOST,PORT))
	server_socket.listen(5)
	print 'Waiting for clients..........'
	SOCKET_LIST.append(server_socket)
	

	while 1:
		read_sockets,write_sockets,error_sockets=select.select(SOCKET_LIST,[],[])
		for sock in read_sockets:
			if sock == server_socket:
				sock_fd,addr=server_socket.accept()
				SOCKET_LIST.append(sock_fd)
				BROADCAST_LIST.append(sock_fd)
			else:
				data=sock.recv(DATA_BUFFER)
				print '<',str(sock.getpeername()),'> ',data
				broadcast_data(sock,"\r" + '<' + str(sock.getpeername()) + '> ' + data)
	sock.close()
			
			
server()
