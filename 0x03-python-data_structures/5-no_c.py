#!/usr/bin/python3

def no_c(my_string):
    """Replaces c and C in a string"""
    string_copy = ''
    c, C = ord('c'), ord('C')
    for i in range(0, len(my_string)):
        char = my_string[i]
        if not (char == chr(c) or char == chr(C)):
            string_copy += char
    return string_copy
