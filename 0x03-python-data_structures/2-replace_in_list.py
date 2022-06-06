#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    for i in range(len(my_list)):
        if idx < 0 or idx > (len(my_list) - 1):
            new_element = None
            return my_list
        elif idx == my_list[i]:
            my_list[i] = new_element
            new_list = my_list
            return my_list
