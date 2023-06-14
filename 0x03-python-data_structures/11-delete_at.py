#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if not my_list:  # Check if the list is empty
        return my_list

    if idx < 0 or idx >= len(my_list): 
        #Check if idx is negative or out of range
        return my_list

    del my_list[idx]  # Delete the item at the specified index

    return my_list
