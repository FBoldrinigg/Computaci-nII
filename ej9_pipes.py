#!/usr/bin/python


from sys import exit
from os import fork, pipe, kill, close, fdopen, getpid, getppid, wait
from signal import pause, signal, SIGUSR1, SIGUSR2


def handler(sid, frame):
    if sid == 10:
        pass
    if sid == 12:
        pass

def main():
    r, w = pipe()
    pid1 = fork()
    if not pid1:
        fpid = getppid()
        signal(SIGUSR1, handler)
        close(r)
        pid2 = fork()
        if not pid2:
            pause()
            w = fdopen(w, "w")
            w.write("Mensaje 2: (PID = " + str(getpid()) + ")\n")
            w.close()
            kill(fpid, SIGUSR2)
        else:
            #letting father know  p1 is ready
            kill(fpid, SIGUSR2)
            pause()
            w = fdopen(w, "w")
            w.write("Mensaje 1: (PID = " + str(getpid()) + ")\n")
            w.close()
            kill(pid2, SIGUSR1)
    else:
        close(w)
        signal(SIGUSR2, handler)
        #waiting till p1 is ready
        pause()
        kill(pid1, SIGUSR1)
        pause()
        print("\nA (PID = ", getpid(), ") leyendo:\n")
        r = fdopen(r)
        for line in r:
            print(line)
        r.close()
        wait()
        exit(0)


main()
