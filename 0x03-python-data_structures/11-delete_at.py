def delete_at(my_list=[], idx=0):
    if not (idx < 0 or idx >= len(my_list)):
        del my_list[idx]
    return my_list