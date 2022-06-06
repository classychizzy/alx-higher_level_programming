#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list) + 1):
        if idx < 0 or idx > (len(my_list) - 1):
            return my_list
        elif idx == my_list[i]:
            my_list[i] = element
            new_list = my_list
            return my_list

