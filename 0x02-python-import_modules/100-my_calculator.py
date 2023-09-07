#!/usr/bin/python3
import sys
import calculator_1


def calculate(a, b, operator):
    if operator not in "+-/*":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = 0
    if operator == "+":
        result = calculator_1.add(a, b)
    elif operator == "-":
        result = calculator_1.sub(a, b)
    elif operator == "*":
        result = calculator_1.mul(a, b)
    elif operator == "/":
        result = calculator_1.div(a, b)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, result))


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    calculate(a, b, operator)
