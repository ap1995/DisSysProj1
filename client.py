# -*- coding: utf-8 -*-
#Created on Thu Oct 5 14:07:10 2017

# @author: ashwini

from socket import *
# from functions import *
import sys
import errno
import lamportclock
# from Queue import PriorityQueue
from multiprocessing import Queue

s = socket()
class Client:
    hostname = ''
    port = 0
    def _init_ (self, hostname, port, processID):
        self.hostname=hostname
        sethostname(hostname)
        numofLikes = 0
        # self.hostname = gethostname()
        self.port = port
        self.processID = processID
        q = Queue.PriorityQueue

    def connection(self, other):
        try:
            self.socket=socket()
            self.socket.bind((self.hostname, self.port))
            # self.socket.create_connection((other.hostname, other.port))
            self.socket.connect((other.hostname, other.port))
            self.socket.listen(5)
            while True:
                c, addr = s.accept()
                print('Got connection from')
                print(addr)
                c.send('Thank you for connecting'.encode())
                c.close()
        except(gaierror):
            print('There was an error resolving the host')
            sys.exit()

    def sendLike(self, numofLikes, currentLikes):
        self.numofLikes = self.numofLikes + currentLikes

    def receive(self):
        s.listen(5)
        while True:
            c, addr = s.accept()
            print('Got connection from')
            print(addr)
            c.send('Thank you for connecting'.encode())
            c.send('Num of Likes'+numofLikes)
            c.close()
    # def readLike(self):
        # data

    def printValue(self):
        print(s.recv(1024))

    s.close()

"""class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item
"""
