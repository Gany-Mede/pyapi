import asyncio
from datetime import datetime as dt
import time

def sundial():
    """
    This function sleeps for 1 second,
    then prints out the current time.

    Notice that this is a task that "blocks" 
    execution of other code
    """

    time.sleep(1)
    print(f"Sundial: {dt.now()}")

# For advanced use cases when you can't turn your blocking 
# code into async code
async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.run_in_executor(None, sundial)
    task2 = loop.run_in_executor(None, sundial)
    tasks = [await task for task in [task1, task2]]


if __name__ == "__main__":
    asyncio.run(main())

