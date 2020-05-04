#!/usr/bin/python


from os import fork, pipe, fdopen, close, wait
from sys import exit


def main():
    fifoPath = "/tmp/ej10_fifo"
    pipeInput = open(fifoPath, "r")
    r, w = pipe()
    if not fork():
        close(w)
        r = fdopen(r)
        msg = r.readline()
        print("MSJ: ", msg)
    else:
        close(r)
        w = fdopen(w, "w")
        w.write(pipeInput.readline())
        w.close()
        wait()
        exit(0)


main()
