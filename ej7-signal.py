#!/usr/bin/python


from sys import exit
from time import sleep
from os import fork, getpid, wait, _exit, kill, getppid
from signal import signal, SIGUSR1, pause


def handler(sid, frame):
    pass


def main():
    signal(SIGUSR1, handler)
    if fork():
        count = 10
        pid2 = fork()
        if pid2:
            while count:
                pause()
                kill(pid2, SIGUSR1)
                count -= 1
            wait()
            exit(0)
        else:
            while count:
                pause()
                print("Soy el hijo2, con PID: ", getpid(), "pong")
                count -= 1
            _exit(0)
    else:
        for _ in range(10):
            kill(getppid(), SIGUSR1)
            print("Soy el hijo1, con PID: ", getpid(), "ping")
            sleep(5)
        _exit(0)


main()
