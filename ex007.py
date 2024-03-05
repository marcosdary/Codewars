from functools import reduce
def decorator_find_summands(func):
    def inner_function(*args, **kwargs):
        if size_list(*args):
            return f'Incorrect length for n = {args}'
        return func(*args, **kwargs)
    return inner_function

@decorator_find_summands
def find_summands(n):
    s = reduce(lambda ac, i: ac + i, n, 0)
    p = len(n)**3
    if s == p:
        return p
    else:
        return f'Incorrect sum for n = {n}'
    
def size_list(sent_list):
    if len(sent_list) < 2:
        return True

example = [7, 9, 11]
output = find_summands(example)
print(output)