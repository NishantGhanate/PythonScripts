import asyncio
import time

class A:
    async def fucn_1(self):
        await asyncio.sleep(3)
        print('hello')
    
    async def fucn_2(self):
        await asyncio.sleep(1)
        print('yellow')

a = A()
loop = asyncio.get_event_loop()
task1 = loop.create_task(a.fucn_1())
task2 = loop.create_task(a.fucn_2())
loop.run_until_complete(asyncio.gather(task1, task2))

