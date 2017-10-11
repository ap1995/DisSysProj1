import threading

class LamportClock:
    def _init_ (self):
        self.lock = threading.Lock()
        self.time = 0

    def increment(self):
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

    def compareTime(self, other):
        self.lock.acquire()
        try:
            self.time = max(self.time, other) +1
            return self.time
        finally:
            self.lock.release()
