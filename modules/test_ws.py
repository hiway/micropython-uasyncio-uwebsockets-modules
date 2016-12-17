import uasyncio as asyncio
import uwebsockets.client as websockets


async def test_websockets(endpoint):
    async with websockets.connect(endpoint) as websocket:
        await websocket.send('Hello, world!')
        echo = await websocket.recv()
        print('RECV', echo)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_websockets('ws://echo.websocket.org/'))
