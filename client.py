# -*- coding: utf-8 -*-
#Created on Thu Oct 5 14:07:10 2017

# @author: ashwini

from socket import *
# from thread import *
import sys
import lamportclock
# from Queue import PriorityQueue
from multiprocessing import Queue

class Client:
    hostname = ''
    port = 0
    client_list = []
    s = None

# Initializing Client and its attributes
    def __init__ (self, port, processID):
        self.numofLikes = 0
        self.port = port
        self.hostname = gethostname()
        self.processID = processID
        #q = Queue.PriorityQueue
        self.s = socket(AF_INET, SOCK_STREAM)

# To start the server part of the Client
    def startServer(self): ### Something is missing here
        try:
            self.s.bind((self.hostname, self.port))
            self.s.listen(5)
            print("server started on port " + str(self.port))
            while True:
                c, addr = self.s.accept()
                print('Got connection from')
                print(addr)
                # c.send(b'Thank you for connecting')
                #self.client_list.append(c)
                # print(c.recv(1024))
                # c.close()
        except(gaierror):
            print('There was an error connecting to the host')
            sys.exit()
            self.s.close()

# To connect to the other client/server
    def startClient(self, port):
        try:
            cSocket=socket(AF_INET, SOCK_STREAM)
            # self.socket.create_connection((other.hostname, other.port))
            cSocket.connect((gethostname(), port))
            while True:
                print('Enter 1 to like, 0 to exit:')
                message = sys.stdin.readline().strip()
                if (message == 1):
                    self.numofLikes = self.numofLikes+1;
                if (message == 0):
                    cSocket.close()
                if((message != 1) and (message != 0))
                    print('Invalid Input')
                cSocket.send(self.numofLikes)
        except:
            cSocket.close()



    def sendToAll(self, message):
        for client in client_list:
            try:
                client.send(message)
            except:
                client.close()

    def closeSocket(self):
        self.s.close()


# # Waits for input from user to add likes
#     def runCLient(self):
#         m.getch()
#
# # To add likes to the post
#     def addLike(self, numofLikes, currentLikes):
#         self.numofLikes = self.numofLikes + currentLikes
#
# # To receive info from other client/servers when they update the likes on the post
#     # def receive(self):
#     #     s.listen(5)
#     #     while True:
#     #         c, addr = s.accept()
#     #         print('Got connection from')
#     #         print(addr)
#     #         c.send('Thank you for connecting'.encode())
#     #         c.send('Num of Likes'+numofLikes)
#     #         c.close()
#     # def readLike(self):
#         # data
#
#     def printValue(self):
#         print(s.recv(1024))
#
#     s.close()

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
