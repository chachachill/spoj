from collections import deque
from sys import stdin

file = stdin


def read_line():
    return file.readline().strip()


def read_int():
    return int(read_line())


def string_list_to_int_list(x):
    return [int(e) for e in x]

operand_hash_map = {'(': 0, '+': 1, '-': 2, '*': 3, '/': 4, '^': 5}
def is_operand(c):
    return c in operand_hash_map

def precedence(c):
    return operand_hash_map[c]
def is_higher_precedence(a, b):
    return precedence(a) > precedence(b)

def is_expression_start(c):
    return c == '('


def is_expression_end(c):
    return c == ')'


def find_expression(lst, start=0):
    operand_stack = []
    output_queue = []
    while len(lst) > start:
        char = lst[start]
        if is_expression_start(char):
            operand_stack.append(char)
        elif is_expression_end(char):
            opr = operand_stack.pop()
            while opr != '(':
                output_queue.append(opr)
                opr = operand_stack.pop()
        elif is_operand(char):
            while len(operand_stack) > 0 and is_higher_precedence(operand_stack[-1], char):
                output_queue.append(operand_stack.pop())
            operand_stack.append(char)
        else:
            output_queue.append(char)
        start += 1
    return output_queue
cases = read_int()

for case in range(cases):
    inp = list(read_line())
    print("".join(find_expression(inp)))