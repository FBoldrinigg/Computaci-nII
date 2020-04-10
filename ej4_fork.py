#!/usr/bin/python


from os import fork, getpid, wait, _exit


def main():
    pid_chld = fork()
    if pid_chld:
        [print("Soy el padre, PID ", getpid(), ", mi hijo es", pid_chld) for _ in range(2)]
        pid, returnCode = wait()
        print("Mi proceso hijo, PID", pid, "terminó. Exit status: ", returnCode)
    else:
        [print("Soy el hijo, PID: ", getpid()) for _ in range(5)]
        print("PID: ", getpid(), "Terminando.")
        _exit(0)


main()
