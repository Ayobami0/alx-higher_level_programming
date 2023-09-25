#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        __import__("sys").stderr.write("Exception: {}\n".format(e))
        return None
