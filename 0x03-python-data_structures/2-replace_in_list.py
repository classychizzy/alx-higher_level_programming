#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx == my_list[len(my_list) - 1]:
        my_list[(len(my_list) - 1)] = element
    else:
        for i in range(len(my_list)):
            if idx < 0 or idx > (len(my_list) - 1):
                return my_list
            elif idx == my_list[i]:
                my_list[i + 1] = element
    return my_list
