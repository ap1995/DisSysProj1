# -*- coding: utf-8 -*-
#Created on Thu Oct 5 14:07:10 2017

# @author: ashwini

from socket import *
from _thread import *
import json
import socialmedia
import threading
from heapq import *
from queue import PriorityQueue
from multiprocessing import Queue
import time
import sys
import lamportclock

# To connect to the other client/server
# from Queue import PriorityQueue

class Client:
    hostname = ''
    port = 0
    s = None
    # queue = Queue()
    processID = 0
    replyList = []
    time =0

# Initializing Client and its attributes
    def __init__(self, ID):
        self.numofLikes = 0
        print("System running: "+ ID)
        port = configdata["systems"][ID][1]
        self.port = port
        self.processID = int(self.port) - 4000
        self.hostname = gethostname()
        # self.reqQueue = PriorityQueue
        self.reqQueue = PriorityQueue()
        self.lc = lamportclock.LamportClock(time, self.processID, self.reqQueue)
        self.replyList = []

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
            msg = conn.recv(1024).decode()

            if "release" in msg:
                removed = self.removefromRequestQ(self.reqQueue)
                self.lc.incrementTime()
            if "Reply" in msg:
                seen = set(self.replyList) # Checking for duplicate replies if any
                if msg[-4:] not in seen:
                    seen.add(msg[-4:])
                    self.replyList.append(msg[-4:])
            if "Add" in msg:
                self.addtoRequestQueue(self.reqQueue, "S"+str(msg[-1:]))
                self.lc.incrementTime()
                # self.reqQueue.put("S"+str(msg[-1:]))
                self.printRequestQ(self.reqQueue)
            print(msg)


    def awaitInput(self):
        # time.sleep(delay)
        while True:
            # print(self.s.recv(1024))
            message = input('Enter 1 to like: ')
            message = int(message)
            if (message == 1):

                self.lc.incrementTime()
                systemName = "S"+ str(self.processID)
                self.addtoRequestQueue(self.reqQueue, systemName)


                print("My request Queue")
                self.printRequestQ(self.reqQueue)
                print("Over")
                self.lc.incrementTime()

                addMessage = "Add to queue " + str(self.port)
                self.sendToAll(addMessage)# Add to all request Queues
                self.printRequestQ(self.reqQueue)
                qcopy = self.reqQueue
                topofQ = self.removefromRequestQ


                if topofQ == ("S"+str(self.processID)) and len(self.replyList)==3:
                    sm.numofLikes = sm.numofLikes + 1
                    self.numofLikes = sm.numofLikes
                    tosend = "Post: \n" + str(sm.string1) + "\nCurrent like count " + str(sm.numofLikes)
                    print(tosend)
                    releaseMessage = "Resource release message from port " + str(self.port)
                    self.sendToAll(releaseMessage)
                else:
                    if(not self.reqQueue.empty()):
                     self.sendReply(configdata["systems"][topofQ][1])

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

    def sendReply(self, port):
        rSocket = socket(AF_INET, SOCK_STREAM)
        rSocket.connect((gethostname(), port))
        reply = "Reply from " + str(self.port)
        rSocket.send(reply.encode())
        self.lc.incrementTime()
        print("Sent reply to port " + str(port))
        rSocket.close()

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
                self.lc.incrementTime()
                # if option ==0:
                #
                #     cSocket.send(message.encode())
                #     cSocket.close()
                #     # Add to request q option
                # if option == 1:
                #
                #     cSocket.send(releaseMessage)
                cSocket.close()

    def addtoRequestQueue(self, reqQueue, item):
        heappush(reqQueue, (self.lc.getLocalTime(), item))
        # reqQueue.put(item, self.lc.getLocalTime())
        # reqQueue.put(item, int(self.processID))
        # self.queue.put(("S" + str(self.processID)), self.processID)

    def removefromRequestQ(self, queue):
        return heappop(queue)
        # return queue.get()

    def printRequestQ(self, queue):
        q1 = queue
        while queue.qsize() !=0:
            print(heappop(queue))
            # print(q1.get())


    def closeSocket(self):
        self.s.close()

######## MAIN #########

with open('config.json') as configfile:
    configdata = json.load(configfile)

sm = socialmedia.Socialmedia
delay = configdata["delay"]
ID = sys.argv[1]
# lc = lamportclock.LamportClock(int(ID[-1:]))
c = Client(ID)
