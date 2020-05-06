#!/usr/bin/python

from sys import argv
from os import mkfifo, path


def main():
    fifoPath = "/tmp/ej10_fifo"
    if not path.exists(fifoPath):
        mkfifo(fifoPath)
    pipeout = open(fifoPath, "w")
    pipeout.write(" ".join(argv[1:]) + "\n")
    pipeout.close()


main()
