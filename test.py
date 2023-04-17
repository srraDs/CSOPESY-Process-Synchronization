import threading
import time

class FittingRoom:
    def __init__(self, n):
        self.room = threading.BoundedSemaphore(n)
        self.mutex = threading.Lock()
        self.blue_done = 0
        self.green_done = 0
        self.switch = n
        self.id = 1
    
    def fit_roomg(self):
        # Fitting room thread for green
        print("\n ID: "+ str(self.id) + " Color: Green")
        self.green_done += 1
        self.id += 1
        time.sleep(3)
        self.room.release()
        if self.room._value == n:
            print("\nEmpty fitting room")
    
    def fit_roomb(self):
        # Fitting room thread for blue
        print("\n ID: "+ str(self.id) + " Color: Blue")
        self.blue_done += 1
        self.id += 1
        time.sleep(3)
        self.room.release()
        if self.room._value == n:
            print("\nEmpty fitting room")

    def green_func(self):
        ctr = 0
        while self.green_done != g:
            self.mutex.acquire()
            print("Green Only")
            temp = 1;
            while temp == 1:
                self.room.acquire()
                threading.Thread(target=self.fit_roomg).start()
                time.sleep(1)
                if self.green_done != g:
                    if ctr == self.switch - 1:
                        if self.blue_done != b:
                            while self.room._value != n:
                                pass
                            self.mutex.release()
                            time.sleep(1)
                            temp = 0
                            ctr = 0
                    else:
                        ctr += 1
                elif self.green_done == g:
                    ctr = 0
                    while self.room._value != n:
                        pass
                    self.mutex.release()
                    time.sleep(1)
                    temp = 0

    def blue_func(self):
        ctr = 0
        while self.blue_done != b:
            self.mutex.acquire()
            print("Blue Only")
            temp = 1;
            while temp == 1:
                self.room.acquire()
                threading.Thread(target=self.fit_roomb).start()
                time.sleep(1)
                if self.blue_done != b:
                    if ctr == self.switch - 1:
                        if self.green_done != g:
                            while self.room._value != n:
                                pass
                            self.mutex.release()
                            time.sleep(1)
                            temp = 0
                            ctr = 0
                    else:
                        ctr += 1
                elif self.blue_done == b:
                    ctr = 0
                    while self.room._value != n:
                        pass
                    self.mutex.release()
                    time.sleep(1)
                    temp = 0

if __name__ == "__main__":
    n,b,g=map(int, input("Enter n , b , g  values: ").split())

    room = FittingRoom(n)

    green = threading.Thread(target=room.green_func)
    blue = threading.Thread(target=room.blue_func)

    green.start()
    time.sleep(1)
    blue.start()
