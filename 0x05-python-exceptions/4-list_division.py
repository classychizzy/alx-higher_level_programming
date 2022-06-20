#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    tempResult = 0
    for i in range(0, list_length):
        try:
            tempResult = my_list_1[i]/my_list_2[i]
        except TypeError:
            tempResult = 0
            print("wrong type")
        except ZeroDivisionError:
            my_list_2[i] = 0
            print("division by 0")
        except IndexError:
            if len(my_list_1) < list_length or len(my_list_2) < list_length:
                print("out of range")
        finally:
            pass
        length.append(tempResult)
    return length
