#!/usr/bin/python

import sys
import time
from os import fork, getpid, wait, _exit, kill, getppid
import signal


def handler(sid, frame):
    pass


def main():
    signal.signal(signal.SIGUSR1, handler)
    count = 10
    if fork():
        pid2 = fork()
        if pid2:
            while count:
                signal.pause()
                kill(pid2, signal.SIGUSR1)
                count -= 1
            wait()
            sys.exit(0)
        else:
            while count:
                signal.pause()
                print("Soy el hijo2, con PID: ", getpid(), "pong")
                count -= 1
            _exit(0)
    else:
        for _ in range(10):
            kill(getppid(), signal.SIGUSR1)
            print("Soy el hijo1, con PID: ", getpid(), "ping")
            time.sleep(5)
        _exit(0)


main()
