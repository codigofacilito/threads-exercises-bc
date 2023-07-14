import time
from threading import Thread
from itertools import cycle
from concurrent.futures import Future

def loading(future):

    for element in cycle('\|/-'):
        if future.done():
            break
        
        print(element, end='\r', flush=True)
        time.sleep(0.5)

def get_response(future):

    try:
        # raise Exception('Lo sentimos, no podemos continuar.')
    
        response = {
            'status': 200,
            'message': 'Petición realizada con exito.'
        }

        time.sleep(2)
        future.set_result(response) # Done = Se cumplio
    
    except Exception as err:
        future.set_exception(err) # Done 



def future_wrapper(function):
    def wrapper(future):
        
        if future.exception():
            return None

        if future.done():
            return function( future.result() )

    return wrapper


@future_wrapper
def print_status_code(response):
    print(response)




future = Future()
future.add_done_callback(print_status_code)

thread = Thread(target=loading, args=(future,))
thread.start()

thread_b = Thread(target=get_response, args=(future,))
thread_b.start()

thread.join()
thread_b.join()
