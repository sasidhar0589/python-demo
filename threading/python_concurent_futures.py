import concurrent.futures
import logging 
# from django.db.migrations import executor
import time


def any_thread_function(name):
    logging.info(f"Thread {name} started.")
    time.sleep(5)
    logging.info(f"Thread {name} finished.")



if __name__ == '__main__':
    format = '%(asctime)s:%(message)s'
    logging.basicConfig(format = format, level = logging.INFO, datefmt="%H:%M:%S")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(any_thread_function, range(3),)
                
# creat a new file with package asyncio and create a thread pool executor similar 
        