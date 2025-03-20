import asyncio 
import logging
logging.basicConfig(level=logging.INFO)

async def fn():
    logging.info('This is ')
    # await asyncio.sleep(1)
    logging.info('asynchronous programming')
    # await asyncio.sleep(1)
    logging.info('and not multi-threading')

    
async def asyncronus_function():
    task= asyncio.create_task(fn())
    logging.info('asynchronous function started')
    await asyncio.sleep(1)
    # await fn()
    logging.info('fn function started')
    await asyncio.sleep(1)
    logging.info('asynchronous function ended')

if __name__ == '__main__':
    asyncio.run(asyncronus_function())
    

