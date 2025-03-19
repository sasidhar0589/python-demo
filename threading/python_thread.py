import threading
import logging
import time
# from pandas.tests.indexing.multiindex.test_loc import test_loc_getitem_index_differently_ordered_slice_none_duplicates
# from pickletools import name2i

def any_thread_function(name):
    logging.info(f"Thread {name} started.")
    time.sleep(5)
    logging.info(f"Thread {name} finished.")
    return name

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,level = logging.INFO,datefmt="%H:%M:%S")
    logging.info("main: before creating thread")
    # thread1= threading.Thread(target=any_thread_function, args=("swetha",))
    # thread1.start()
    # logging.info(": thread started running")
    # thread1.join()
    # logging.info(": thread joined")
    
# Daemon thread
    logging.info("main: before creating daemon thread")
    thread2 = threading.Thread(target=any_thread_function, args=("rahul",), daemon=True)
    thread2.start()
    logging.info(": daemon thread started running")
    logging.info("main: all threads started")
    thread2.join()
    threads = list()
    for i in range(5):
        thread = threading.Thread(target=any_thread_function, args=(f"Thread {i}",))
        thread.start()
        threads.append(thread)
        logging.info(f": thread {i} started running")
        time.sleep(1)
    for index, thread in enumerate(threads):
        thread.join()
        logging.info(f": thread {index} joined")


