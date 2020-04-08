#!/usr/bin/python


import subprocess as sp 
import sys
import  getopt
import datetime


def readArgs():
    try:
        (opts, args) =  getopt.getopt(sys.argv[1:], 'c:f:l:', [])
    except getopt.GetoptError as error:
        print("\nError, ", str(error))
        return
    if len(opts) > 3:
        x = 1
        print("\nEntered more options than 3:\n")
        for opt, arg in opts:
            print(str(x)+ ':', "opt:", opt, "arg:", arg, "\n")
            x += 1
        return
    elif len(opts) < 3:
        x = 1
        print("\nEntered less options than 3:\n")
        for opt, arg in opts:
            print(str(x)+ ':', "opt:", opt, "arg:", arg, "\n")
            x += 1
        return
    return opts

def main():
    opts = readArgs()
    if not opts:
        return
    command = ""
    out_file = ""
    log_file = ""
    for opt, value in opts:
        if opt == '-c':
            command = value
        elif opt == '-f':
            out_file = open(value, "a")
        else:
            log_file = open(value, "a")
    process = sp.Popen([command], stdout = out_file, stderr = sp.PIPE, shell = True, universal_newlines = True)
    error = process.communicate()[1]
    if not error:
        log_file.write(str(datetime.datetime.now()) + " Comando " + command + " ejecutado correctamente.\n\n")
        out_file.write("\n"s)
    else:
        log_file.write(str(datetime.datetime.now()) + "  " + str(error) + "\n\n")
    out_file.close()
    log_file.close()


main()