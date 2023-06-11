#!/use/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extend the tuples to have a length of at least 2
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)
    
    # Perform the addition of corresponding elements
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return result
