import time
import logging
from threading import Thread
from multiprocessing import Process

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(
    level=10,
    format="%(threadName)s:%(message)s"
)

def is_prime(number):
    if number < 2:
        return False
    
    for x in range(2, int(number ** 0.5) + 1):
    # for x in range(2, number):
        if number % x == 0:
            return False
    
    return True
    
def print_is_prime(number):
    message = f"Number: {number} is prime: " + str(is_prime(number))
    logging.info(message)


start = time.time()

tasks = []
numbers = [174440041, 3657500101, 88362852307, 414507281407, 2428095424619, 4952019383323, 12055296811267, 17461204521323, 28871271685163, 53982894593057]

"""
for number in numbers:
    thread = Thread(target=print_is_prime, args=(number,))
    thread.start()

    tasks.append(thread)


for task in tasks:
    task.join()
"""

with ProcessPoolExecutor(max_workers=4) as executor:
    
    for number in numbers:
        executor.submit(print_is_prime, number)


print(time.time()- start)