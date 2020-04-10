#!/usr/bin/python


import sys
from getopt import getopt, GetoptError
from os import fork, getpid, getppid, _exit


def readArgs():
    try:
        opts, args = getopt(sys.argv[1:], 'n:', [])
    except GetoptError as error:
        print(error)
        sys.exit(0)
    if len(opts) > 1:
        x = 1
        print("\nEntered more options than 1:\n")
        for opt, arg in opts:
            print(str(x)+ ':', "opt:", opt, "arg:", arg, "\n")
            x += 1
        sys.exit(0)
    elif len(opts) < 1:
        x = 1
        print("\nDidn't enter an option\n")
        sys.exit(0)
    return opts[0][1]

def main():
    try:
        N = int(readArgs())
    except  ValueError:
        print("Entered argument is not an integer")
        sys.exit(0)
    for _ in range(N):
        if not fork():
            print("Soy el proceso: ", getpid(), ". Mi padre es el proceso: ", getppid())
            _exit(0)


main()
