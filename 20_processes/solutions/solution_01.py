"""Solution 01 -- A port is a number a program asks for."""

import socket

listener = socket.socket()
listener.bind(("127.0.0.1", 0))  # 0 means "any free one -- you choose"
port = listener.getsockname()[1]

print(1024 < port < 65536)
print(listener.getsockname()[0])

second = socket.socket()
try:
    second.bind(("127.0.0.1", port))
    print("bound twice")
except OSError as err:
    # The number differs per system -- 48 on macOS, 98 on Linux -- so code that
    # reacts to it tests errno.EADDRINUSE rather than a literal.
    print(type(err).__name__, err.strerror)

listener.close()
second.close()

print(socket.gethostbyname("localhost"))
