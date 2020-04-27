#!/usr/bin/python


from sys import argv, exit
from getopt import getopt, GetoptError
from signal import pause, signal,SIGUSR2
from os import kill, _exit, getpid, fork, getppid
from time import sleep


def emptyTempFile():
    fd = open("/tmp/ej8_childpids.txt", "w")
    fd.close

def handler(sid, frame):
    if sid == 12:
        print("Soy el PID: ", getpid(), ", recibí la señal: ", sid, "de mi padre PID: ", getppid())
        _exit(0)

def readArgs():
    try:
        opts, args = getopt(argv[1:], 'p:', ['process='])
        if len(opts) != 1:
            raise GetoptError("Entered a different number of options than 1")
    except GetoptError as error:
        print(error)
        exit(0)
    return opts[0][1]

def main():
    fpid = None
    try:
        p = int(readArgs())
    except ValueError:
        print("Entered argument is not an integer")
    if not p:
        exit(0)
    emptyTempFile()
    for _ in range(p):
        if not fork():
            print("Creando proceso: ", getpid())
            signal(SIGUSR2, handler)
            w = open("/tmp/ej8_childpids.txt", "a")
            w.write(str(getpid()) + "-")
            w.close()
            pause()
        else:
            fpid = getpid()
    if getpid() == fpid:
        sleep(0.15)
        print("Padre PID: ", fpid)
        fd = open("/tmp/ej8_childpids.txt", "r")
        pids = fd.read()
        fd.close()
        pid_list = list(map(int, pids.split("-")[:-1]))
        for pid in pid_list:
            kill(pid, SIGUSR2)
        exit(0)


if __name__ == '__main__':
    main()
