def decorator_numbers(func):
    def inner_function(*args, **kwargs):
        for arg in args:
            validation_number(arg)
        return func(*args, **kwargs)
    return inner_function

def validation_number(number):
    if number <= 0:
        raise ValueError("Numbers less than 0 or negative are not accepted")
    
@decorator_numbers   
def narcissistic(value):
    size_value = len(str(value))
    sum_value = 0
    
    for number in str(value):
        calculation_number = int(number)**size_value
        sum_value += calculation_number
  
    if sum_value == value:
        return True  
    return False 

narcissistic_number = 153
output = narcissistic(narcissistic_number)
print(output)
