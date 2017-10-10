from socket import *
from multiprocessing import Queue
#from Queue import PriorityQueue

class Client:
    s = socket()
    def _init__ (self):
        sethostname('Ash')
        numofLikes = 0
        host = gethostname()
        port = 12345
        Queue.PriorityQueue

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
