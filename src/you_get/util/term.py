#!/usr/bin/env python

import fcntl
import struct
import termios

def get_terminal_size():
    """Get (width, height) of the current terminal."""
    try:
        return struct.unpack('hh', fcntl.ioctl(1, termios.TIOCGWINSZ, struct.pack('hh', 0, 0)))
    except Exception:
        return (40, 80)
