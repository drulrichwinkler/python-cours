"""Exercise 01 -- A port is a number a program asks for.

Bind a socket to port 0 on `127.0.0.1`, which asks the operating system for any free
port. Then print four lines:

  1. whether the port you got is above 1024 and below 65536
  2. the address the socket is bound to
  3. the exception class name and the message, separated by a space, from a second
     socket asking for the same port
  4. what `localhost` resolves to

Expected output:

    True
    127.0.0.1
    OSError Address already in use
    127.0.0.1

Hint: `socket.socket()`, `bind(("127.0.0.1", 0))`, `getsockname()` gives back
`(address, port)`. `err.strerror` is the message without the number -- the number
itself is 48 on macOS and 98 on Linux, which is why the expected output does not
contain it.
"""

import socket

# TODO: bind, then four prints
