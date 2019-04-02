import socket, random
from sandr import Rec, Send
IP = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket Made')

s.connect((IP, PORT))
print ("Established connection with the server.")
s.send('1'.encode('utf-8'))
s.send('bot'.encode('utf-8'))
Send(s, '1')
Send(s, 'bot')
if Rec(s):
	while True:
		message = str(random.randint(0,10))
		if message == 'break':
			s.send('break'.encode('utf-8'))
			break
		s.send(message.encode('utf-8'))

		if (s.recv(1024)).decode('utf-8') == 'Won':
			print ('You won')
			break



s.close()