# micropython-uasyncio-uwebsockets-modules

Patched [uasyncio](https://github.com/micropython/micropython-lib/tree/master/uasyncio) and [@danni's uwebsockets](https://github.com/danni/uwebsockets) as `modules` to compile into Micropython firmware.

## Get:

### The Lazy way:

If you are the sort doesn't mind downloading binary firmware from some 
website and running on your machines, get the firmware here:

https://github.com/hiway/micropython-uasyncio-uwebsockets-modules/releases/tag/0.1

I have built the firmware from latest micropython source as of 16 Dec 
with only the .py files in this repository added to `modules`.

### The Other Way

If you prefer to compile your own firmware, I'll assume you have the 
toolchain set up already. If not, here's a great tutorial:

https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/overview

Once you have that up and running, locate the correct directory within your micropython repo:

    micropython/esp8266/modules/

Copy the files into modules directory, and run `make` while in `micropython/esp8266` directory.

Flash the firmware.

In serial/websocket REPL:

    >>> import test_ws
    RECV Hello, world!
    

## Why?

So you can write async websocket clients (http only!) on your ESP8266 :-D

```python
import uasyncio as asyncio
import uwebsockets.client as websockets


async def test_websockets(endpoint):
    async with websockets.connect(endpoint) as websocket:
        await websocket.send('Hello, world!')
        echo = await websocket.recv()
        print('RECV', echo)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_websockets('ws://echo.websocket.org/'))
```
