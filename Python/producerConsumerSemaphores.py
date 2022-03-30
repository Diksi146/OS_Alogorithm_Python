import threading
import time

# Shared Memory variables
CAPACITY = 10
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0

# Declaring Semaphores
# mutex is to show whether buffer is in excution or not 1 shows free while 0 shows in execution
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)
print(threading.Semaphore(0))
# Producer Thread Class
# The acquire() method decreases the semaphore count if the count is greater than zero. Else it blocks till the count is greater than zero.
# The release() method increases the semaphore count and wakes up one of the threads waiting on the semaphore.


class Producer(threading.Thread):
    def run(self):

        global CAPACITY, buffer, in_index, out_index
        global mutex, empty, full

        items_produced = 0
        counter = 0

        while items_produced < 20:
            empty.acquire()  # decreases empty by 1
            mutex.acquire()

            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1) % CAPACITY
            print("Producer produced : ", counter)
            if(full._value == CAPACITY):
                print("Buffer is full.")

            mutex.release()
            full.release()

            time.sleep(1)

            items_produced += 1


# Consumer Thread Class


class Consumer(threading.Thread):
    def run(self):

        global CAPACITY, buffer, in_index, out_index, counter
        global mutex, empty, full

        items_consumed = 0

        while items_consumed < 20:
            full.acquire()
            mutex.acquire()

            item = buffer[out_index]
            out_index = (out_index + 1) % CAPACITY
            print("Consumer consumed item : ", item)
            if(full._value == 0):
                print("Buffer is Empty.")

            mutex.release()
            empty.release()

            time.sleep(2.5)

            items_consumed += 1


# Creating Threads
producer = Producer()
consumer = Consumer()

# Starting Threads
consumer.start()
producer.start()

# Waiting for threads to complete
producer.join()
consumer.join()
