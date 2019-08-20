#!/usr/bin/env python3

import socket
import struct # to send `int` as  `4 bytes`
import time
from config import *

#FILENAME = 'chart.png'  # File to send


''' Return a file as byte string '''
def get_file(filename):
	with open(filename, 'rb') as fp:
		data = fp.read()
	return data


''' Send image to socket '''
def send_image(sock,FILENAME):

#    sock.sendall(GET_IMAGE.encode())
#    data = sock.recv(50)
#    print('Received from server: ',data.decode())

#    while data.decode() != QUIT_COMMAND: # Loop - send images until receives QUIT_COMMAND
	#message_type = struct.pack('!i', 2147483647)
	#sock.sendall(message_type)
	fdata = get_file(FILENAME)
	print('Opened file of length:', len(fdata))
	len_str = struct.pack('!i', len(fdata))     # send string size                
	sock.sendall(len_str)
	print('Sent filesize size to client: ',len_str,'(',len(fdata),')')
	# send bytes to socket
	sock.sendall(fdata)
	print('Sent data, will wait.')
	data = sock.recv(50)
	print('Received from server: ',data.decode())
	


''' Open socket and send image to server '''
def run(socket_address):
	
	s = socket.socket()

	s.connect(socket_address)
	i = 1
	while True:
		string = 'img'+str(i)+'.png'
		print('sending ' + string)
		send_image(s,string)
		i=i+1
		if i > 147:
			i = 1 
		time.sleep(0.5)


	# exit*
	print("Closing socket, will exit.")
	
#    s.close()

# --- main ---

run(CAMERA_ADDRESS)