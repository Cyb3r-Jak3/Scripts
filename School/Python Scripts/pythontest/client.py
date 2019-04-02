import socket, random
IP = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket Made')

s.connect((IP, PORT))
print ("Established connection with the server.")
def Mode0():
	while True:
		message = input('What would you like to say \n')
		if message == 'break':
			s.send('break'.encode('utf-8'))
			break
		s.send(message.encode('utf-8'))

		if (s.recv(1024)).decode('utf-8') != 'ack':
			print ('Message Failed')
		else:
			print ('\n')
def Mode1():
	while True:
		message = input('What would you like to guess \n')
		if message == 'break':
			s.send('break'.encode('utf-8'))
			break
		s.send(message.encode('utf-8'))

		if (s.recv(1024)).decode('utf-8') == 'Won':
			print ('You won')
			break

chocie = input('Mode?\n')
name = input('What do you call yourself?\n')
if chocie == '0':
	s.send('0'.encode('utf-8'))
	s.send(name.encode('utf-8'))
	Mode0()
if chocie == '1':
	s.send('1'.encode('utf-8'))
	s.send(name.encode('utf-8'))
	Mode1()

s.close()