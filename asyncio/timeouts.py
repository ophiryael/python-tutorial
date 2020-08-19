import asyncio


async def one_hour_sleep():
    await asyncio.sleep(3600)
    print("Finished nap time")


async def main():
    try:
        await asyncio.wait_for(one_hour_sleep(), timeout=1.0)
    except asyncio.TimeoutError:
        print("Timeout!")


asyncio.run(main())
