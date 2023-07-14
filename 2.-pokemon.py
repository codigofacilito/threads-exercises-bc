import requests
import logging
from threading import Thread

logging.basicConfig(
    level=10,
    format='%(threadName)s:%(levelname)s-%(message)s'
)

def get_pokemon_by_id(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("forms")[0].get('name')

    return None


def print_name(pokemon_id):
    name = get_pokemon_by_id(pokemon_id)
    logging.info(name)
    
   

for i in range(1, 101):
    thread = Thread(
        target=print_name,
        args=(i, )
    )

    thread.start()