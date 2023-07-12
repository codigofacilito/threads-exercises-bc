import time
from threading import Thread
from multiprocessing import Process

def fibonnaci(number):

    if number == 1:
        return 0

    if number == 2:
        return 1
    
    return fibonnaci(number - 1) + fibonnaci(number - 2)

start = time.time()

a = Process(target=lambda: print(fibonnaci(41)) )
b = Process(target=lambda: print(fibonnaci(42)) )

a.start()
b.start()

a.join()
b.join()

print(time.time()- start)