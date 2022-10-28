#!/usr/bin/python3
"""The module contains the main function"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

json_file = "add_item.json"
items = sys.argv[1:]

try:
    items = load_from_json_file(json_file) + items
except FileNotFoundError:
    pass
save_to_json_file(items, json_file)
