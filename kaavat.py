#!/usr/bin/env python
from sympy import *
import sys
x = Symbol('x')

"""
parses the commandline arguments
returns a tupple of mult, exp and symbol flag of the argument
"""
def argument_parser(argument):
    #the variables that are to be returned
    #symb_flag is used to differiantite between variables and constants
    mult = ""
    exp = ""
    symb_flag = False

    i = 0
    #loop through the argument until a letter is found
    #the part until that point is the multiplier
    while(len(argument) > i):
        if(str.isalpha(argument[i])):
            break
        mult += argument[i]
        i += 1
    
    #loop through the part after the letter
    #that part is the exponent
    if(len(argument) > i and str.isalpha(argument[i])):
        symb_flag = True
        print('the symbol of variable ' + argument + ' is ' + argument[i])

        while(len(argument) > i):
            if(str.isdigit(argument[i])):
                exp += argument[i]
            i += 1


    if(argument[0] == '-' and len(mult) == 1):
        mult += "1"
    if(len(exp) == 0):
        exp = "1"
    if(len(mult) == 0):
        mult = "1"
    print('the multiplier of variable ' + argument + ' is ' + mult)
    print('the exponent of variable ' + argument + ' is ' + exp)
    print('the symbol flag of variable ' + argument + ' is ' + str(symb_flag))
    return (int(mult), int(exp), symb_flag)

"""
builds a sympy compatable expression
from command line arguments
"""
def expr_builder():
    argc = len(sys.argv)
    expr = 0

    for i in range(2, argc):
        mult, exp, symb_flag = argument_parser(sys.argv[i])
        if(symb_flag):
            expr += (+mult*x**exp)
        else:
            expr += (+mult**exp)

    print("Input: " + str(expr))
    return expr

def usage():
        print("Usage:")
        print("kaavat [-s solve -d diff -i integrate] [expression]")
        print("Expression example: 3x2 -2x 17")
        exit(1)
 

def main():

    if(len(sys.argv) < 2):
        usage()

    if(sys.argv[1] == '-s'):
        result = solveset(expr_builder(), x)
    elif(sys.argv[1] == '-d'):
        result = diff(expr_builder(), x)
    elif(sys.argv[1] == '-i'):
        result = integrate(expr_builder(), x)
    else:
        usage()
    print("Output: " + str(result))

if __name__ == "__main__":
    main()