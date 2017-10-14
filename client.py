# -*- coding: utf-8 -*-
#Created on Thu Oct 5 14:07:10 2017

# @author: ashwini

from socket import *
from _thread import *
import json
import socialMedia
import threading
import time
import sys
import lamportclock
# from Queue import PriorityQueue
from multiprocessing import Queue


# def awaitInput(self, conn):
#     try:
#         while True:
#             print(conn.recv(1024))
#     except:
#         print('Exception in awaitInput function')

# To connect to the other client/server

with open('config.json') as configfile:
    configdata = json.load(configfile)

class Client:
    hostname = ''
    port = 0
    client_list = []
    s = None
    socialmedia = socialMedia()

# Initializing Client and its attributes
    def __init__ (self, ID):
        self.numofLikes = 0
        port = configdata["systems"][ID]
        self.port = port
        self.hostname = gethostname()
        #q = Queue.PriorityQueue
        self.s = socket(AF_INET, SOCK_STREAM)
        self.startClient(configdata)
        # self.awaitInput()
        
        # self.startListening()

    def startClient(self, configdata):
        # try:
            cSocket = socket(AF_INET, SOCK_STREAM)
            # self.socket.create_connection((other.hostname, other.port))
            for i in configdata["systems"]:
                cSocket.connect((gethostname(), configdata["systems"][i]))


                    # cSocket.send(self.numofLikes)
        # except:
        #     print('exception')
        #     cSocket.close()


    def awaitInput(self):
        while True:
            # dummy = sys.stdin.readline().strip()
            message = input('Enter 1 to like:')
            message = int(message)
            if (message == 1):
                socialmedia.numofLikes = socialmedia.numofLikes + 1  # start thread to send current likes, with socialmedia object, to everyone and then kill
                self.numofLikes = socialmedia.numofLikes
                self.sendToAll(socialmedia.string1 + "Total number of likes "+ socialmedia.numofLikes)
                # cSocket.send(b'numofLikes' + b'str(socialmedia.numofLikes)')
            # if (message == 0):
            #     cSocket.close()
            # if ((message != 1) and (message != 0)):
            #     print('Invalid Input')

# To start the server part of the Client
    def startListening(self): ### Threading part is incomplete here
        try:
            self.s.bind((self.hostname, self.port))
            self.s.listen(4)
            print("server started on port " + str(self.port))
            while True:
                c, addr = self.s.accept()
                print('Got connection from')
                print(addr)
                start_new_thread(self.startClient, (configdata,)) # conneciton dictionary
                # c.close()
        except(gaierror):
            print('There was an error connecting to the host')
            sys.exit()
            self.s.close()

    def sendToAll(self, message):
        for i in configdata["systems"]:
            self.s.send(message)

    def closeSocket(self):
        self.s.close()


# # Waits for input from user to add likes
#     def runCLient(self):
#         m.getch()

# # To add likes to the post
#     def addLike(self, numofLikes, currentLikes):
#         self.numofLikes = self.numofLikes + currentLikes

# To receive info from other client/servers when they update the likes on the post
    # def receive(self):
    #     s.listen(5)
    #     while True:
    #         c, addr = s.accept()
    #         print('Got connection from')
    #         print(addr)
    #         c.send('Thank you for connecting'.encode())
    #         c.send('Num of Likes'+numofLikes)
    #         c.close()
    # def readLike(self):
        # data
#
#     def printValue(self):
#         print(s.recv(1024))
#
#     s.close()

# class MyPriorityQueue(PriorityQueue):
#     def __init__(self):
#         PriorityQueue.__init__(self)
#         self.counter = 0
#
#     def put(self, item, priority):
#         PriorityQueue.put(self, (priority, self.counter, item))
#         self.counter += 1
#
#     def get(self, *args, **kwargs):
#         _, _, item = PriorityQueue.get(self, *args, **kwargs)
#         return item

