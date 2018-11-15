# Building a TCP server with Python 3

# Import the sockets module for networking
import socket

def Main():
	# Use loopback address and an unused port so it doesnt interfere
		# with other system processes
	host = '127.0.0.1'
	port = 5000
	
	# Create socket object 
	s = socket.socket()
	
	# Bind host to the loopback address
	s.bind((host,port))

	# Tell user that server has started
	print ("Server has started.")
	
	# Set to listen on port 5000
	s.listen(1)
	
	# Accept connection from client
	c, addr = s.accept()
	
	# Print where connection is coming from
	print ("Connection from: " + str(addr))
	
	# Create loop to make server run indefinently
	while True:
		data = c.recv(1024).decode('utf-8')
		# If there is no data coming through, break the while loop
		if not data:
			break
		print ("From connected user: " + data)
		
		# Send data back to client only in upper case characters
		data = data.upper()
		print ("Sending: " + data)
		c.send(data.encode('utf-8'))
		
	# Close the program
	c.close()
	
if __name__ == '__main__':
	Main()
	
