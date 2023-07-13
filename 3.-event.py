import time
import sys

sys.getrefcount
from itertools import cycle
import logging
from threading import Thread, Lock, Event

lock = Lock()

logging.basicConfig(
    level=10,
    format='%(threadName)s:%(levelname)s-%(message)s'
)

class BankFacilito:

    def __init__(self):
        self.balance = 0
    
    def deposit(self):
        for _ in range(1_000_000):
            with lock:
                self.balance += 1


    def withdraw(self):
        for _ in range(1_000_000):
            with lock:
                self.balance -= 1


def loading(event):
    for c in cycle('|/-|'):
        if event.wait(.1):
            break

        print(c, end="\r", flush=True)

bank = BankFacilito()
start = time.time()

event = Event()

thread_a = Thread(target=bank.deposit) 
thread_b = Thread(target=bank.withdraw) 
thread_loading = Thread(target=loading, args=(event, )) 

thread_a.start()
thread_b.start()
thread_loading.start()

thread_a.join()
thread_b.join()

event.set()

print("El programa demoro: ", time.time() - start)

print(bank.balance)