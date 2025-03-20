import asyncio
import logging
import time
import concurrent.futures
from pandas.core._numba import executor
format = '%(asctime)s: %(message)s'

logging.basicConfig(level=logging.INFO, format=format, datefmt="%H:%M:%S")

def sleeping(sleep_time):
    logging.info(f"Sleeping {sleep_time} seconds")
    time.sleep(sleep_time)
    return f"Done Sleeping {sleep_time} seconds"

async def async_with_multi():
    loop = asyncio.get_running_loop()
    temp_result = await loop.run_in_executor(None, sleeping, 1)
    logging.info(temp_result)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        result = await loop.run_in_executor(executor, sleeping, 2)
        logging.info(result)
        result = await loop.run_in_executor(executor, sleeping, 4)
        logging.info(result)
if __name__ == "__main__":
    asyncio.run(async_with_multi())
    
#  adde methods to create event loop , new_evet_loop and run_in_executor get_evet_loop, SET_event_loop
