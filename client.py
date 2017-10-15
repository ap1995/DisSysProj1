# -*- coding: utf-8 -*-
#Created on Thu Oct 5 14:07:10 2017

# @author: ashwini

from socket import *
from _thread import *
import json
import socialmedia
import threading
# from multiprocessing import Process
import time
import sys
# import lamportclock

# To connect to the other client/server

class Client:
    hostname = ''
    port = 0
    s = None

# Initializing Client and its attributes
    def __init__ (self, ID):
        self.numofLikes = 0
        print("System running: "+ ID)
        port = configdata["systems"][ID][1]
        self.port = port
        self.hostname = gethostname()
        #q = Queue.PriorityQueue
        self.s = socket(AF_INET, SOCK_STREAM)
        # self.connectToAll()

        start_new_thread(self.startListening, ())
        start_new_thread(self.awaitInput, ())
        # time.sleep(configdata["delay"])
        while True:
            pass

    def receiveMessages(self, conn, addr):
        # while True:
            print('Message received from Client at port '+ str(addr[1]))
            print(conn.recv(1024).decode())

    def awaitInput(self):
        # time.sleep(delay)
        while True:
            # print(self.s.recv(1024))
            message = input('Enter 1 to like: ')
            message = int(message)
            if (message == 1):
                sm.numofLikes = sm.numofLikes + 1  # start thread to send current likes, with socialmedia object, to everyone and then kill
                self.numofLikes = sm.numofLikes
                tosend = "Post: \n" + str(sm.string1) + "\nCurrent like count " + str(sm.numofLikes)
                print(tosend)
                self.sendToAll(tosend)
            # else:
            #     print('Invalid input')
                # self.sendToAll(sm.string1 + "Total number of likes "+ str(sm.numofLikes))
                # cSocket.send(b'numofLikes' + b'str(socialmedia.numofLikes)'
            # if ((message != 1) and (message != 0)):
            #     print('Invalid Input')

# To start the server part of the Client
    def startListening(self):
        try:
            self.s.bind((self.hostname, int(self.port)))
            self.s.listen(4)
            print("server started on port " + str(self.port))
            while True:
                c, addr = self.s.accept()
                conn = c
                print('Got connection from')
                print(addr)
                start_new_thread(self.receiveMessages, (conn, addr)) # connection dictionary
                # c.close()
        except(gaierror):
            print('There was an error connecting to the host')
            self.s.close()
            sys.exit()

# To send updated likes to everyone
    def sendToAll(self, message):
        for i in configdata["systems"]:
            if (configdata["systems"][i][1] == self.port):
                continue
            else:
                cSocket = socket(AF_INET, SOCK_STREAM)
                ip, port = configdata["systems"][i]
                port = int(port)
                cSocket.connect((gethostname(), port))
                print('Connected to port number ' + configdata["systems"][i][1])
                cSocket.send(message.encode())
                print('Message sent to Client at port '+ str(port))
                cSocket.close()

    def closeSocket(self):
        self.s.close()

######## MAIN #########

with open('config.json') as configfile:
    configdata = json.load(configfile)

sm = socialmedia.Socialmedia
delay = configdata["delay"]
ID = sys.argv[1]
c = Client(ID)
