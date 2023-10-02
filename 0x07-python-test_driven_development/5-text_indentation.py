#!/usr/bin/python3
"""This module contains a function that indents a string paragraph.

The function will be tested using the similarly named
text file in the tests folder.
You can run the test using this command
    python3 -m doctest -v ./tests/5-text_indentation.txt
"""


def text_indentation(text):
    """Indent text by splitting it at ".", "?", and ":".

    The function splits a text at the characters ".", "?" and ":"
    and printing with double line breaks.
    Args:
        text (str): The input text to be indented.
    Raises:
        TypeError: If the 'text' parameter is not a string.
    """
    last_printed_index = 0
    joined_text = []
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i, char in enumerate(text, start=1):
        if char in ".?:":
            joined_text.append(text[last_printed_index:i].strip())
            last_printed_index = i
    joined_text.append(text[last_printed_index:].strip())
    print("\n\n".join(joined_text), end="")
