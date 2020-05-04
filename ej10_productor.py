#!/usr/bin/python


from os import mkfifo, path


def main():
    fifoPath = "/tmp/ej10_fifo"
    if not path.exists(fifoPath):
        mkfifo(fifoPath)
    pipeout = open(fifoPath, "w")
    pipeout.write(input("Ingresar mensaje: ") + "\n")
    pipeout.close()


main()
