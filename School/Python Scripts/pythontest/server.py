import socket, threading, os, random
from sandr import SSend, SRec
open(os.getcwd() + "/stuff.txt", 'w').close()
f = open(os.getcwd() + "/stuff.txt", 'r+')

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        print("Server Up")
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            print (address[1], "Connected")
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        data = list(SRec(client))
        mode = data[0]
        # print(mode)


        if mode == '0':
            print (address[1], "Mode 0", " Called", name)
            while True:
                try:
                    data = SRec(client)
                    if data:
                        if data == 'break':
                            print (address[1], 'Connection ended')
                            return False
                        else:
                            f.write('%s %s\n' % (str(address[1]), data))
                            response = 'ack'
                            SSend(client, response)
                    else:
                        raise error('Client disconnected')
                except:
                    client.close()
                    return False
        if mode == '1':
            SSend(client, 'ready')
            print (address[1], "Mode 1")
            hidden = random.randint(0,10)
            print(hidden)
            while True:
                try:
                    data = (client.recv(1024)).decode('utf-8')
                    print(data)
                    if data:
                        if data == 'break':
                            print (address[1], 'Connection ended')
                            return False
                        else:
                            if data == str(hidden):
                                client.send('Won'.encode('utf-8'))
                                print (address[1], "Got it Ending Connection")
                                break
                            else:
                                client.send("Fail".encode('utf-8'))
                except:
                    client.close()
                    return False




if __name__ == "__main__":
    #port_num = int(input("Port? "))
    port_num = 5000
    ThreadedServer('',port_num).listen()
