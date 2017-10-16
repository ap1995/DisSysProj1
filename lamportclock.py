import threading
import time
from heapq import *
from multiprocessing import Queue
from queue import PriorityQueue

class LamportClock:
    time = 0
    processID = 0
    def __init__(self, time, processID, queue):
        self.lock = threading.Lock()
        self.time = 0
        self.processID = processID
        self.queue = queue

    def incrementTime(self):
        # self.lock.acquire()
        # try:
        self.time = self.time +1
        # finally:
        #     self.lock.release()
        print("Current Lamport time is "+ self.getLamportTime())
        # print("Current Lamport time "+ str(self.time)+"."+str(self.processID))

    def getLocalTime(self):
        return self.time

    def getLamportTime(self):
        # self.lock.acquire()
        # try:
        return (str(self.time) + "."+ str(self.processID))
        # finally:
        #     self.lock.release()

    """def getTotallyOrderedTime(self):
        self.lock.acquire()
        try:
            return (self.time+'.'+other.time+'.'+self.processID)
        finally:
            self.lock.release()
            """

    def compareTime(self, other):
        # self.lock.acquire()
        # try:
        self.time = max(self.time, other) +1
        return self.time
        # finally:
            # self.lock.release()
