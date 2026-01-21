import time
import asyncio


async def function1():
    await asyncio.sleep(1)
    print("func1")


async def function2():
    await asyncio.sleep(1)
    print("func2")


async def function3():
    await asyncio.sleep(4)
    print("func3")


async def main():
    task = asyncio.create_task(function1())  # It runs when it get time
    # await function1()
    await function2()
    await function3()


# asyncio.run(main())


import requests


async def function1():
    print("function1")
    url = "https://images.pexels.com/photos/35389652/pexels-photo-35389652.jpeg"
    r = requests.get(url)
    open("image1.jpg", "wb").write(r.content)
    return "func1"


async def function2():
    print("function2")
    url = "https://images.pexels.com/photos/33325739/pexels-photo-33325739.jpeg"
    r = requests.get(url)
    open("image2.jpg", "wb").write(r.content)
    return "func2"


async def function3():
    print("function3")
    url = "https://images.pexels.com/photos/34972781/pexels-photo-34972781.jpeg"
    r = requests.get(url)
    open("image3.jpg", "wb").write(r.content)
    return "func3"


async def main():
    # await function1()
    # await function2()
    # await function3()
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)


asyncio.run(main())
