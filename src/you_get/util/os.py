#!/usr/bin/env python

from platform import system

def detect_os():
    """Detect operating system."""
    syst = system().lower()

    if 'cygwin' in syst:
        return 'cygwin'
    elif 'darwin' in syst:
        return 'mac'
    elif 'linux' in syst:
        # detect WSL
        try:
            with open('/proc/version', 'r') as f:
                if 'microsoft' in f.read().lower():
                    return 'wsl'
        except: 
            return 'linux'
        return 'linux'
    elif 'windows' in syst:
        return 'windows'
    elif 'bsd' in syst:
        return 'bsd'

    return 'unknown'
