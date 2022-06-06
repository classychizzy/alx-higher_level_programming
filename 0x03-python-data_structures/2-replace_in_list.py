#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    for i in range(len(my_list)):
        if my_list[i] == idx:
            my_list[i] = new_element
            new_list = my_list
            return new_list
        elif idx < 0 or idx > (len(my_list) - 1):
            return my_list
