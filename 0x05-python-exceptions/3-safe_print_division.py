#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        return result
