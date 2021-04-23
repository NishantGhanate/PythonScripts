import asyncio
import time

class A:
    async def fucn_1(self):
        time.sleep(1)
        print('hello')
    
    async def fucn_2(self):
        time.sleep(1)
        print('yellow')

a = A()

loop = asyncio.get_event_loop()
loop.run_until_complete(a.fucn_1())

task1 = loop.create_task(a.fucn_1())
task2 = loop.create_task(a.fucn_2())
loop.run_until_complete(asyncio.gather(task1, task2))

time.sleep(1)

# In order to callback same function need to create same task asgain
task1 = loop.create_task(a.fucn_1())
task2 = loop.create_task(a.fucn_2())
loop.run_until_complete(asyncio.gather(task1, task2))

loop.run_until_complete(a.fucn_1())

# for i in range(1,10):
#     if i%2 == 0:
        # loop.run_until_complete(asyncio.gather(task1, task2))


    