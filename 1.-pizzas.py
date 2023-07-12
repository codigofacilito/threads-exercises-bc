import time
from threading import Thread

def cook_pizza_a():
    time.sleep(3)
    return "cook_pizza_a..."


def cook_pizza_b():
    time.sleep(3)
    return 'cook_pizza_b...'

start = time.time()

thread_a = Thread(target=lambda: print(cook_pizza_a()))
thread_b = Thread(target=lambda: print(cook_pizza_b()))

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()

print("Eating")
print(time.time() - start)