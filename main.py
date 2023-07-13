import time
from threading import Thread
from multiprocessing import Process

def fibonnaci(number):

    if number == 1:
        return 0

    if number == 2:
        return 1
    
    return fibonnaci(number - 1) + fibonnaci(number - 2)


def is_prime(number):
    if number < 2:
        return False
    
    for x in range(2, int(number ** 0.5) + 1):
    # for x in range(2, number):
        if number % x == 0:
            return False
    
    return True
    

start = time.time()

tasks = []
numbers = [174440041, 3657500101, 88362852307, 414507281407, 2428095424619, 4952019383323, 12055296811267, 17461204521323, 28871271685163, 53982894593057]

if __name__ == '__main__':
    for number in numbers:
        thread = Process(target=print(is_prime(number)))
        thread.start()
        tasks.append(thread)


    for task in tasks:
        task.join()

    print(time.time()- start)
