def collinearity(x1:float, y1:float, x2: float, y2: float) -> bool:
    try:
        if (x1, y1) == (0, 0) or (x2, y2) == (0, 0):
            return True
        if y1 == 0 and y2 == 0 or x1 == 0 and x2 == 0:
            return True
        if  x1 / x2 == y1 / y2:
            return True
        return False
    except ZeroDivisionError:
        return False
    
print(collinearity(*[0, 425, 0, -261]))