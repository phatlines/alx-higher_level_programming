#!/usr/bin/python3
def no_c(my_string):
    string_2 = ""
    for stg2 in range(len(my_string)):
        if my_string[stg2] == 'c' or my_string[stg2] == 'C':
            continue
        string_2 += my_string[stg2]
    return string_2
