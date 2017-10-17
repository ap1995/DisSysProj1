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
        # self.numofLikes = 0
        print("System running: "+ ID)
        port = configdata["systems"][ID][1]
        self.port = port
        self.processID = int(self.port) - 4000
        self.hostname = gethostname()
        # self.reqQueue = PriorityQueue
        self.reqQueue = []
        self.lc = lamportclock.LamportClock(time, self.processID, self.reqQueue)
        self.replyList = []
        self.lock = threading.RLock()
        self.s = socket(AF_INET, SOCK_STREAM)
        # self.connectToAll()
        start_new_thread(self.startListening, ())
        start_new_thread(self.awaitInput, ())

        while True:
            pass

    def receiveMessages(self, conn, addr):
        # while True:
            print('Message received from Client at port '+ str(addr[1]))
            msg = conn.recv(1024).decode()
            time.sleep(delay)
            if "release" in msg:
                removed = self.removefromRequestQ(self.reqQueue)
                self.printRequestQ(self.reqQueue)
                print("Enter 1 to like: ")
                # self.lc.incrementTime()
            if "Reply" in msg:
                seen = set(self.replyList) # Checking for duplicate replies if any
                if msg[-4:] not in seen:
                    seen.add(msg[-4:])
                    self.replyList.append(msg[-4:])
                self.lc.incrementTime()
                print("Reply list is ")
                self.printReplyList(self.replyList)
            if "Add" in msg:
                port = msg.split()[3]
                ltime = msg.split()[4]
                # likes = msg.split()[5]
                self.addtoRequestQueue(self.reqQueue, ltime, "S"+str(port[-1:]))
                self.lc.incrementTime()
                self.sendReply(configdata["systems"]["S"+str(port[-1:])][1])

                # self.reqQueue.put("S"+str(msg[-1:]))
                # self.numofLikes = likes
                self.printRequestQ(self.reqQueue)
            if "Post" in msg:
                likes = msg.split()[-1]
                sm.numofLikes = int(likes)
            print(msg)


    def awaitInput(self):
        # time.sleep(delay)
        while True:
            # print(self.s.recv(1024))

            message = input('Enter 1 to like: ')
            message = int(message)

            if (message == 1):

                # self.lc.incrementTime()
                systemName = "S"+ str(self.processID)
                # self.lock.acquire()
                self.addtoRequestQueue(self.reqQueue, self.lc.getLamportTime(), systemName)

                print("My request Queue")
                self.printRequestQ(self.reqQueue)
                print("Over")
                # self.lc.incrementTime()
                time.sleep(delay)
                addMessage = "Add to queue " + str(self.port) + " "+ str(self.lc.getLamportTime())
                print(addMessage)
                self.sendToAll(addMessage)# Add to all request Queues
                self.printRequestQ(self.reqQueue)
                time.sleep(delay)

                # qcopy = self.reqQueue
                # while self.reqQueue:
                topofQ = self.reqQueue[0][1]
                print("Top of Queue is " + str(topofQ))

                while True:
                    topofQ = self.reqQueue[0][1]
                    if topofQ == ("S" + str(self.processID)) and len(self.replyList) == 3:
                        break
                    else:
                        self.printRequestQ(self.reqQueue)
                        time.sleep(delay)

                time.sleep(delay)

                if topofQ == ("S"+str(self.processID)) and len(self.replyList)==3:
                    self.lock.acquire(sm.numofLikes)
                    sm.numofLikes = sm.numofLikes + 1
                    # self.numofLikes = sm.numofLikes
                    tosend = "Post: \n" + str(sm.string1) + "\nCurrent like count " + str(sm.numofLikes)
                    print(tosend)
                    self.sendToAll(tosend)
                    time.sleep(delay)
                    releaseMessage = "Resource release message from port " + str(self.port)
                    self.sendToAll(releaseMessage)
                    self.removefromRequestQ(self.reqQueue)
                    self.replyList.clear()
                    self.lock.release()
                # else:
                #     self.sendReply(configdata["systems"][topofQ][1])
            else:        # if len(self.reqQueue) !=0:
                # self.sendReply(configdata["systems"][self.removefromRequestQ(self.reqQueue)[1]][1])
                sys.exit()

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
                # time.sleep(delay)
                start_new_thread(self.receiveMessages, (conn, addr)) # connection dictionary
                # c.close()
        except(gaierror):
            print('There was an error connecting to the host')
            self.s.close()
            sys.exit()

    def sendReply(self, port):
        rSocket = socket(AF_INET, SOCK_STREAM)
        rSocket.connect((gethostname(), int(port)))
        reply = "Reply from " + str(self.port)
        rSocket.send(reply.encode())
        # self.lc.incrementTime()
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
                time.sleep(delay)
                print('Message sent to Client at port '+ str(port))
                # self.lc.incrementTime()
                cSocket.close()

    def addtoRequestQueue(self, reqQueue, time, item):
        heappush(reqQueue, (time, item))
        # reqQueue.put(item, self.lc.getLocalTime())
        # reqQueue.put(item, int(self.processID))
        # self.queue.put(("S" + str(self.processID)), self.processID)

    def removefromRequestQ(self, queue):
        return heappop(queue)
        # return queue.get()

    def printRequestQ(self, queue):
        q1 = queue
        print("Current Request Queue is")
        # while len(q1) !=0:
        #     print(heappop(q1))
        for i in q1:
            print(i)
            # print(q1.get())

    def printReplyList(self, rlist):
        for i in rlist:
            print(i)


    def closeSocket(self):
        self.s.close()

######## MAIN #########

with open('config.json') as configfile:
    configdata = json.load(configfile)

sm = socialmedia.Socialmedia(0)
delay = configdata["delay"]
ID = sys.argv[1]
# lc = lamportclock.LamportClock(int(ID[-1:]))
c = Client(ID)
