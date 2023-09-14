#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if type(roman_string) is not str or roman_string is None:
        return 0
    res = 0
    roman_string = roman_string.upper()
    roman_rep = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
    for n, i in enumerate(roman_string, 0):
        if n < len(roman_string) - 1:
            roman_rep_k = list(roman_rep.keys())
            if roman_rep_k.index(i) < roman_rep_k.index(roman_string[n+1]):
                res -= roman_rep[i]
                continue
        res += roman_rep[i]
    return res
