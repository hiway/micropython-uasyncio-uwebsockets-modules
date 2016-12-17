# micropython-uasyncio-uwebsockets-modules

Patched [uasyncio](https://github.com/micropython/micropython-lib/tree/master/uasyncio) and [@danni's uwebsockets](https://github.com/danni/uwebsockets) as `modules` to compile into Micropython firmware.

Note: For steps below, you will need a toolchain set up to compile Micropython firmware 

Locate the correct directory within your micropython repo:

    micropython/esp8266/modules/

Copy the files into modules directory, and run `make` while in `micropython/esp8266` directory.

Flash the firmware.

In serial/websocket REPL:

    >>> import test_ws
    RECV Hello, world!
