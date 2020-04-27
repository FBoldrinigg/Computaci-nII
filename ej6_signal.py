#!/usr/bin/python


from time import sleep
from sys import exit
from os import fork, getpid, wait, kill
from signal import signal, SIGUSR1, pause, SIGINT, SIGTERM, SIG_IGN


def logPid(pid):
    fd = open("/tmp/ej6_pidlog.txt", "w")
    fd.write(str(pid))
    fd.close()

def readPidlog():
    fd = open("/tmp/ej6_pidlog.txt", "r")
    pid = fd.readline()
    fd.close()
    return int(pid)

def handler(sid, frame):
    if sid == 2:
        print("\nPID: ", getpid(), "SIGINT recibida. Interrumpiendo proceso.")
        pid = readPidlog()
        kill(pid, SIGTERM)
        print("Proceso hijo PID: ", pid, "terminado.")
        exit(0)
    if sid == 10:
        print("PID: ", getpid(), "SIGUSR1 recibida")

def main():
    signal(SIGUSR1, handler)
    pid = fork()
    if pid:
        signal(SIGINT, handler)
        print("Padre PID: ", getpid(), "| hijo PID: ", pid, "\n")
        logPid(pid)
        for _ in range(10):
            kill(pid, SIGUSR1)
            sleep(5)
        print("10 señales SIGUSR1 enviadas")
        kill(pid, SIGTERM)
        print("Proceso hijo PID:", pid, "terminado")
        print("Proceso padre, PID: ", getpid(), "terminando.")
        exit(0)
    else:
        signal(SIGINT, SIG_IGN)
        while True:
            pause()


if __name__ == "__main__":
    main()
