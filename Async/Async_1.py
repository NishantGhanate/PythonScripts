import asyncio

async def say(something, delay):
  await asyncio.sleep(delay)
  print(something)
  
loop = asyncio.get_event_loop()
task1 = loop.create_task(say('hi', 1))
task2 = loop.create_task(say('hoi', 2))
loop.run_until_complete(asyncio.gather(task1, task2))