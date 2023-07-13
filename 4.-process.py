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

if __name__ == '__main__':

    a = Process(target=print(fibonnaci(30)))
    b = Process(target=print(fibonnaci(31)))

    a.start()
    b.start()

    a.join()
    b.join()

    print(time.time()- start)
