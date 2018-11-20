# Client for our UDP server in python 3

# Import the sockets module for networking
# Import hashlib so we can securely hash our message digest
import hashlib
import socket

def Main():
	host = '127.0.0.1'
	# Use different port because UDP is weird like that
	port = 5001
	
	# Create tuple that lists our server address and port
	server = ('127.0.0.1', 5000)
	
	# Convert the socket to listen to UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# Bind to our port
	s.bind((host,port))
	
	# Create input for message
	message = input("->")
	
	# Create while loop for connection
	while message != 'q':
		
		# Encode/decode the message and tell it where to go
		s.sendto(message.encode('utf-8'), server)
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		
		# Let the user know that the message was received
		print("Recieved from server: " + data)
		message = input("->")
		
	# Close the program	
	s.close()		
		
if __name__ == '__main__':
	Main()
