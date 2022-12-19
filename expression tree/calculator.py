# assignment: programming assignment 4 (Expression Tree)
# author: Tanvi Herwadkar
# date: November 20, 2022
# file: calculator.py is a file that takes an infix expression and evaluates and
#       prints the answer
# input: infix expression
# output: value of input post evaluation

from stack import Stack
from tree import ExpTree

#method that recognizes numbers as potentially double digit and floats
def separate_decimals(string):
    list_ = []
    i = 0
    while i < len(string):
        if string[i].isdigit() or string[i] == ".":
            list_.append(string[i])
            i += 1
        else:
            break
    return "".join(list_), len(list_)

#takes an infix expression and converts it to its postfix form
def infix_to_postfix(infix):
    stack = []
    postfix = ""
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    # based off of psuedocode given by Michael Coe and Professor Munishkina
    jumpto = None
    for idx, i in enumerate(infix):
        # if number: add to postfix
        if jumpto != None:
            if idx < jumpto:
                continue
        if i.isdigit():
            s, jump = separate_decimals(infix[idx:])
            jumpto = jump + idx
            postfix += s + " "
        # if open parentheses: push to stack
        elif (i == "("):
            stack.append(i)
        # if close parentheses: pop stack and add to postfix until open parentheses is reached
        elif (i == ")"):
            while ( stack != [] and stack[-1] != "(" ):
                postfix += stack.pop() + " "
            stack.pop()
        else:
            while (stack != [] and stack[-1] != "(" and priority[i] <= priority[stack[-1]]):
                postfix += stack.pop() + " "
            stack.append(i)
    while stack != []:
        postfix += stack.pop() + " "
    out = postfix[:-1]
    return out

def calculate(infix):
    #print(infix)
    postfix = infix_to_postfix(infix)
    #print(postfix)
    tree = ExpTree.make_tree(postfix.split())
    return  ExpTree.evaluate(tree)

print("Welcome to Calculator Program!")
while True:
    x = input("Please enter your expression here. To quit enter 'quit' or 'q':\n").upper()
    if (x == "Q" or x =="QUIT"):
        print("Goodbye!")
        break
    else:
        print(calculate(x))

