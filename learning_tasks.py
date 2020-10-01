#!/usr/bin/env python3

import asyncio
from datetime import datetime as dt
import time

async def swiss():
    await asyncio.sleep(1)
    print(f"Swiss: {dt.now()}")

async def main():
    # Most preferred way to write async code
    task3 = asyncio.create_task(swiss())
    task4 = asyncio.create_task(swiss())
    await asyncio.gather(task3, task4)


if __name__ == "__main__":
    asyncio.run(main())
 
