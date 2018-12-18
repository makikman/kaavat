#!/usr/bin/env python
from stings import *

x = Symbol('x')

def main():

    if(sys.argv[1] == '-s'):
        result = solveset(expr_builder(), x)
    elif(sys.argv[1] == '-d'):
        result = diff(expr_builder(), x)
    elif(sys.argv[1] == '-i'):
        result = integrate(expr_builder(), x)
    else:
        print("Usage:")
        print("kaavat [-s solve -d diff -i integrate] [expression]")
        exit(1)
    print("Output: " + str(result))

if __name__ == "__main__":
    main()