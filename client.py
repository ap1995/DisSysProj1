# -*- coding: utf-8 -*-
#Created on Thu Oct 5 14:07:10 2017

# @author: ashwini

from socket import *
from Queue import PriorityQueue

class Client:
    s = socket()
    def _init_ self:
        # sethostname('Ash')
        numofLikes = 0
        host = gethostname()
        port = 12345
        # queue.PriorityQueue

    def connection:
        s.connect((host, port))

    def send:
        s.listen(5)
        while True:
            c, addr = s.accept()
            print('Got connection from')
            print(addr)
            c.sendall('Thank you for connecting'.encode())
            c.close()

    print(s.recv(1024))
    s.close()
