def solution(number):
    if number < 0:
        return 0
    multiple = (n for n in range(3, number) if n % 3 == 0 or n % 5 == 0)
    
    return sum(multiple)

