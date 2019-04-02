def Send(socket, text):
	socket.send(text.encode('utf-8'))
def Rec(socket):
	info = (socket.recv(1024)).decode('utf-8')
	return info
def SSend(client, text):
	client.send(text.encode('utf-8'))
def SRec(client):
	info = (client.recv(1024)).decode('utf-8')
	return info
