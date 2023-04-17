import threading # Import necessary libraries 
import time
import random

class FittingRoom:
    def __init__(self, capacity):
        self.room = threading.BoundedSemaphore(capacity) #Semaphore with capacity (n) 
        self.mutex = threading.Lock() #creates lock
        self.green_customers_done = 0 # counter to detect
        self.blue_customers_done = 0 # counter to detect
        self.switch = capacity # set switch to capacity. for blue 
        self.customer_id = 1 #ids they start at 1 so it is 1
       
    def green_room(self):# Fitting room thread for green customers
        
        print("\n ID: "+ str(self.customer_id) + " Color: [Green]")
        self.green_customers_done += 1 # customer counter for green 
        self.customer_id += 1 # increment id
        time.sleep(3) 
        self.room.release() # release semaphore to allow customer
        if self.room._value == self.switch: # if current val of semaphore counter is equal to fitting room
            print("\nEmpty fitting room!")
            
    def blue_room(self):
        # Fitting room thread for blue customers
        print("\n ID: "+ str(self.customer_id) + " Color: Blue")
        self.blue_customers_done += 1
        self.customer_id += 1
        time.sleep(4) 
        self.room.release()
        if self.room._value == self.switch:
            print("\nEmpty fitting room!")

    def green(self):
        counter = 0 # track of how many guess 
        while self.green_customers_done != green_customers: # loop until all customers are done used while because bugs in for
            self.mutex.acquire()# for lock
            print("Green Only")
            temp = True
            while temp:
                self.room.acquire() # for semaphore
                threading.Thread(target=self.green_room).start()# create new thread to allow many customers
                time.sleep(1) 
                if self.green_customers_done != green_customers: # if more green customers wait
                    if counter == self.switch - 1: # if enough g customers entered
                        if self.blue_customers_done != blue_customers:# if there are blue waiting
                            while self.room._value != capacity: # condition until room is empty
                                pass
                            self.mutex.release() # if empty relase
                            time.sleep(1)
                            temp = False #stops the loop
                            counter = 0 # reset
                    else:
                        counter += 1 
                elif self.green_customers_done == green_customers:# if no gren customer waiting
                    counter = 0# reset
                    while self.room._value != capacity: #condition until empty
                        pass
                    self.mutex.release()# if empty relase
                    time.sleep(1)
                    temp = False # stop loops



##Same Logic as green
    def blue(self):
        counter = 0# to keep track of b customer
        while self.blue_customers_done != blue_customers:# condition until done
            self.mutex.acquire()
            print("Blue Only")
            temp = True
            while temp:
                self.room.acquire()# acquire sema
                threading.Thread(target=self.blue_room).start()#new thread
                time.sleep(1)
                if self.blue_customers_done != blue_customers:# more blue customer waiting
                    if counter == self.switch - 1:# if blue customer have entered
                        if self.green_customers_done != green_customers:# if green waiting
                            while self.room._value != capacity:# until room is ready
                                pass
                            self.mutex.release()# rlease lock
                            time.sleep(1)
                            temp = False #stop the loop
                            counter = 0#reset
                    else:
                        counter += 1# increment
                elif self.blue_customers_done == blue_customers:
                    counter = 0
                    while self.room._value != capacity:
                        pass
                    self.mutex.release()
                    time.sleep(1)
                    temp = False
                    
if __name__ == "__main__":
    capacity, blue_customers, green_customers = map(int, input("n,b,g :").split())

    room = FittingRoom(capacity)# object 

    # Generate a random number between 0 and 1
    start_green = random.randint(0, 1)

    if start_green:
        green = threading.Thread(target=room.green, daemon=True)
        blue = threading.Thread(target=room.blue, daemon=True)
    else:
        green = threading.Thread(target=room.blue, daemon=True)
        blue = threading.Thread(target=room.green, daemon=True)

    #starting them
    green.start()
    time.sleep(1)# used to avoid deadlock
    blue.start()

    # join threads (to finish before they exit)
    green.join()
    blue.join()


