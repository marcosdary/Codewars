# You are given a list of unique integers arr,
# and two integers a and b. Your task is to find 
# out whether or not a and b appear consecutively 
# in arr, and return a boolean value (True if a and b are consecutive, False otherwise).
#It is guaranteed that a and b are both present in arr.

def consecutive(arr, a, b):
    exit_consecutive = True if arr.index(a) + 1 == arr.index(b) or arr.index(b) + 1 == arr.index(a) else False
    return exit_consecutive
a, b = 3, 1
sequence = [1, 3, 5, 7]
output = consecutive(sequence, a, b) # consecutive([1, 3, 5, 7], 3, 1), True
