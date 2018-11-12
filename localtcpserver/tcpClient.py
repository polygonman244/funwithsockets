# Client side part of our python TCP server

import socket

def Main():
	# Use loopback address and an unused port so it doesnt interfere
		# with other system processes
	host = '127.0.0.1'
	port = 5000
	
	# Create socket object 
	s = socket.socket()
	
	# Connect host to the local machine
	s.connect((host,port))
	
	# Create input method for the message that you will send
	message = input("->")
	
	# Create while loop for the letter "q"
		# We will have the user type "q" to quit the program
	while message != 'q':
		s.send(message.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		
		# Print statement indicating that the server recieved the message
		print("Recieved from server: " + data)
		message = input("->")
	s.close()
	
if __name__ == '__main__':
	Main()
