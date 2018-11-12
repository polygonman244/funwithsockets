# UDP server with python3
import socket

def Main():
	
	host = '127.0.0.1'
	port = 5000
	
	# This time we have to convert our sockets object to listen on UDP
	# Sockets listens on TCP by default
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# Bind to our port
	s.bind((host,port))
	
	# Tell the user the server has started
	print("Server Started")
	
	# Create while loop for connection
	while True:
		# Since UDP doesnt use addresses, we have to store the data
			# and the address
		data, addr = s.recvfrom(1024)
		
		# Decode data and print
		data = data.decode('utf-8')
		print("Message From: " + str(addr))
		print("From connected user: " + data)
		
		# Print data in upper case
		data = data.upper()
		print("Sending: " + data)
		
		# Reencode data and tell it where to go
		s.sendto(data.encode('utf-8'), addr)
		
	# Close the program
	c.close()

if __name__ == '__main__':
	Main()
		
	
		
	
	
	
