import threading 
import time
import random

class FittingRoom:
    def __init__(self, capacity):
        self.room = threading.BoundedSemaphore(capacity) 
        self.mutex = threading.Lock() 
        self.green_customers_done = 0 
        self.blue_customers_done = 0 
        self.switch = capacity # How many green customers can enter before allowing blue to enter
        self.customer_id = 1 
       
    def green_room(self):
        # Fitting room thread for green customers
        print("\n ID: "+ str(self.customer_id) + " Color: [Green]")
        self.green_customers_done += 1
        self.customer_id += 1
        time.sleep(3) 
        self.room.release() 
        if self.room._value == self.switch: 
            print("\nEmpty fitting room!")
            
    def blue_room(self):
        # Fitting room thread for blue customers
        print("\n ID: "+ str(self.customer_id) + " Color: Blue")
        self.blue_customers_done += 1
        self.customer_id += 1
        time.sleep(3) 
        self.room.release()
        if self.room._value == self.switch:
            print("\nEmpty fitting room!")

    def green(self):
        counter = 0
        while self.green_customers_done != green_customers: 
            self.mutex.acquire()
            print("Green Only")
            temp = True
            while temp:
                self.room.acquire()
                threading.Thread(target=self.green_room).start()
                time.sleep(1) 
                if self.green_customers_done != green_customers: 
                    if counter == self.switch - 1: 
                        if self.blue_customers_done != blue_customers:
                            while self.room._value != capacity:
                                pass
                            self.mutex.release() 
                            time.sleep(1)
                            temp = False 
                            counter = 0 
                    else:
                        counter += 1 
                elif self.green_customers_done == green_customers:
                    counter = 0
                    while self.room._value != capacity: 
                        pass
                    self.mutex.release()
                    time.sleep(1)
                    temp = False 

    def blue(self):
        counter = 0
        while self.blue_customers_done != blue_customers:
            self.mutex.acquire()
            print("Blue Only")
            temp = True
            while temp:
                self.room.acquire()
                threading.Thread(target=self.blue_room).start()
                time.sleep(1)
                if self.blue_customers_done != blue_customers:
                    if counter == self.switch - 1:
                        if self.green_customers_done != green_customers:
                            while self.room._value != capacity:
                                pass
                            self.mutex.release()
                            time.sleep(1)
                            temp = False
                            counter = 0
                    else:
                        counter += 1
                elif self.blue_customers_done == blue_customers:
                    counter = 0
                    while self.room._value != capacity:
                        pass
                    self.mutex.release()
                    time.sleep(1)
                    temp = False
                    
if __name__ == "__main__":
    capacity, blue_customers, green_customers = map(int, input("n,b,g :").split())

    room = FittingRoom(capacity)

    # Generate a random number between 0 and 1
    start_green = random.randint(0, 1)

    if start_green:
        green = threading.Thread(target=room.green, daemon=True)
        blue = threading.Thread(target=room.blue, daemon=True)
    else:
        green = threading.Thread(target=room.blue, daemon=True)
        blue = threading.Thread(target=room.green, daemon=True)

    green.start()
    time.sleep(1)
    blue.start()

    # join threads
    green.join()
    blue.join()



