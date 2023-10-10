#!/usr/bin/python3
"""A module module containing a function."""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"

try:
    item_list = load_from_json_file(file_name)
except Exception:
    item_list = []
for item in sys.argv[1:]:
    item_list.append(item)
save_to_json_file(item_list, file_name)
