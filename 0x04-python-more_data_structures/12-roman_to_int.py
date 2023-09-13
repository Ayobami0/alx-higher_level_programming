#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if type(roman_string) is not str or roman_string is None:
        return 0
    res = 0
    roman_string = roman_string.upper()
    roman_rep = {"I": 1, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in roman_string:
        res += roman_rep[i]
