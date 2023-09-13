#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return
    a_dictionary[key] = value
    return a_dictionary
# a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
# new_dict = update_dictionary(a_dictionary, 'language', "Python")
# print(new_dict)
# print("--")
# print(a_dictionary)
#
# print("--")
# print("--")
#
# new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
# print(new_dict)
# print("--")
# print(a_dictionary)
