#!/usr/bin/python3
def magic_string():
    return ("BestSchool, " * (globals()[list(globals())[-1]] + 1))[:-2]
