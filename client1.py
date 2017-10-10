from socket import *
from multiprocessing import Queue
#from Queue import PriorityQueue

class Client:
    s = socket()
   def _init_ (self, name, port):
        self.name=name
        sethostname(name)
        numofLikes = 0
        host = gethostname()
        self.port = port

    def connection(self):
        s.connect((host, port))

    def send(self):
        s.listen(5)
        while True:
            c, addr = s.accept()
            print('Got connection from')
            print(addr)
            c.send('Thank you for connecting'.encode())
            c.close()
            
    def printValue():
        print(s.recv(1024))
    s.close()
