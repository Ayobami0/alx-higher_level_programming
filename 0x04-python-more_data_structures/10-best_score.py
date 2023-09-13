#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    return list(a_dictionary.keys())[list(
        a_dictionary.values()).index(max(a_dictionary.values()))]
# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))
#
# best_key = best_score(None)
# print("Best score: {}".format(best_key))
