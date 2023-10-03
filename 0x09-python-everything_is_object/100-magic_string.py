#!/usr/bin/python3
def magic_string():
    print(("BestSchool, " * (globals()[list(globals())[-1]] + 1))[:-2])
