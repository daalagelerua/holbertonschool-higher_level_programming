#!/usr/bin/python3
import sys

argv = sys.argv[1:]
argc = len(argv)

if argc == 0:
    print("{} arguments.".format(argc))
elif argc == 1:
    print("{} argument:".format(argc))
else:
    print("{} arguments:".format(argc))

for i in range(argc):
    print("{}: {}".format(i + 1, argv[i]))
