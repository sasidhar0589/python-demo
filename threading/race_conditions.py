import time
import concurrent.futures
class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f'{name}: {self.value}')

            
# due to in efficent use of fake database even though we us multiple threads the  data is not getting updated as expected

# To solve this issue we can use a lock to ensure that only one thread can update the database at a time.
import threading

class FakeDatabaseWithLock:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        print(f'Thread {name} starting')
        with self._lock:
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f'{name}: {self.value}')

if __name__ == '__main__':
    database = FakeDatabase()
    database_with_lock = FakeDatabaseWithLock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(10):
            executor.submit(database.update, i)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(10):
            executor.submit(database_with_lock.update, i)
# synchronization can be achived with locking,
# 1. Locks are a low-level way of synchronizing threads.
# 2. Locks are acquired and released.

database_lock = threading.Lock()
print('Before first acquire')
database_lock.acquire()

print('After first acquire')
database_lock.release()
print('After first release')
database_lock.acquire()
print('After second acquire')