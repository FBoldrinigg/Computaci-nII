#!/usr/bin/python


import sys
import  getopt


def readArgs():
	try:
		(opts,args) =  getopt.getopt(sys.argv[1:], 'i:o:', [])
	except getopt.GetoptError as error:
		print("\nError, ", str(error))
		return
	if len(opts) > 2:
		x = 1
		print("\nEntered more options than 2:\n")
		for opt, arg in opts:
			print(str(x)+ ':', "opt:", opt, "arg:", arg, "\n")
			x += 1
		return
	elif len(opts) < 2:
		x = 1
		print("\nEntered less options than 2:\n")
		for opt, arg in opts:
			print(str(x)+ ':', "opt:", opt, "arg:", arg, "\n")
			x += 1
		return
	return opts

def copyFile(args):
	if not args:
		return
	for opt, arg in args:
		if opt == '-i':
			origin = arg
		else:
			destination = arg
	try:
		originFile = open(origin, "r")
	except FileNotFoundError as error:
		print(error)
		return
	lines = originFile.readlines()
	originFile.close()
	destFile = open(destination, "w")
	destFile.writelines(lines)
	destFile.close()


copyFile(readArgs())