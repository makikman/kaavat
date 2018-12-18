#!/usr/bin/env python
from sympy import *
import sys

#x is universally used for the symbol
x = Symbol('x')

#parses the commandline arguments
#returns a tupple of mult, exp and symbol flag of the argument
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
    
    if(len(exp) == 0):
        exp = "1"
    if(len(mult) == 0):
        mult = "1"
    print('the multiplier of variable ' + argument + ' is ' + mult)
    print('the exponent of variable ' + argument + ' is ' + exp)
    print('the symbol flag of variable ' + argument + ' is ' + str(symb_flag))
    return (int(mult), int(exp), symb_flag)

#builds a sympy compatable expression
#from mult, exp and symbol flag
def expr_builder(mult, exp, symb_flag):
    expr = 0

    if(symb_flag):
        expr += (+mult*x**exp)
    else:
        expr += (+mult**exp)

    return expr

def main():
    argc = len(sys.argv)
    expr = 0

    for i in range(1, argc):
        mult, exp, symb_flag = argument_parser(sys.argv[i])
        expr += expr_builder(mult, exp, symb_flag)

    print(str(expr))
    result = solveset(expr, x)
    print(result)

main()
