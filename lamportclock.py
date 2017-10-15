import threading
import time

from multiprocessing import Queue



class LamportClock:
    def _init_ (self, processID, queue):
        self.lock = threading.Lock()
        self.time = 0
        # self.processID = processID
        # self.queue = queue

    def addtoRequestQueue(self, queue, item):
        queue.put(item)
        # self.queue.put(("S" + str(self.processID)), self.processID)

    def removefromRequestQ(self, queue):
        return queue.get()

    def printRequestQ(self, queue):
        q1= queue
        while q1.qsize() != 0:
            print(q1.get())

    def incrementTime(self):
        self.lock.acquire()
        try:
            self.time = self.time +1
        finally:
            self.lock.release()

    def getLocalTime(self):
        self.lock.acquire()
        try:
            return self.time
        finally:
            self.lock.release()

    """def getTotallyOrderedTime(self):
        self.lock.acquire()
        try:
            return (self.time+'.'+other.time+'.'+self.processID)
        finally:
            self.lock.release()
            """

    # def addToQueue(self, port):
    #     PriorityQueue.put(port, int(port)-4000)

    def compareTime(self, other):
        self.lock.acquire()
        try:
            self.time = max(self.time, other) +1
            return self.time
        finally:
            self.lock.release()
