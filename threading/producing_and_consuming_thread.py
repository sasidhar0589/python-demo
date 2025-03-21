import random 
import threading
import concurrent.futures
SENTEL = object()
class Pipeline:
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
    def get_message(self, name):
        print(f'{name} is waiting for a message')
        self.consumer_lock.acquire()
        message = self.message
        print(f'{name} got message: {message}')
        self.producer_lock.release()
        return message
    def set_message(self, message, name):
        print(f'{name} is setting message: {message}')
        self.producer_lock.acquire()
        self.message = message
        print(f'{name} set message: {message}')
        self.consumer_lock.release()



def producer(pipeline):
    for _ in range(10):
        message = random.randint(1,101)
        print(f'Producer got message: {message}')
        pipeline.set_message(message, "Producer")
    pipeline.set_message(SENTEL, "Producer")
def consumer(pipeline):
    message = 0
    while message is not SENTEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTEL:
            print(f'Consumer got message: {message}')
if __name__ == "__main__":
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)