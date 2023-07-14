import time
import asyncio

async def cooking_pizza_a():
    print("Cooking pizza A")
    await asyncio.sleep(2)
    print("Finish pizza A")


async def cooking_pizza_b():
    print("Cooking pizza B")
    await asyncio.sleep(2)
    print("Finish pizza B")


async def cooking_pizza_c():
    print("Cooking pizza C")
    await asyncio.sleep(2)
    print("Finish pizza C")


async def main():
    start = time.time()

    print(">>> Comenzamos la Elaboración de pizzas.")

    asyn_tasks = [ asyncio.create_task( task() ) for task in [ cooking_pizza_a, cooking_pizza_b, cooking_pizza_c]]

    await asyncio.gather(*asyn_tasks)

    print("Hora de comer.")
    print(time.time() - start)


asyncio.run( 
    main()
)

