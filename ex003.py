from functools import partial
def decorator_time(func):
    
    def inner_function(*args, **kwargs):
        for arg in args:
            validation_time(arg)
        return func(*args, **kwargs)
    return inner_function

@decorator_time
def to_pretty(seconds):
    calculation_time = partial(lambda x, y: x / y, seconds)
    
    if seconds >= 604800:
        if int(calculation_time(604800)) == 1:
            return 'a week ago'
        return f'{int(calculation_time(604800))} weeks ago'
    
    elif 86400 <= seconds < 604800:
        if int(calculation_time(86400)) == 1:
            return 'a day ago'
        return f'{int(calculation_time(86400))} days ago'
    
    elif 3600 <= seconds < 86400:
        if int(calculation_time(3600)) == 1:
            return 'an hour ago'
        return f'{int(calculation_time(3600))} hours ago'
    
    elif 60 <= seconds < 3600:
        if int(calculation_time(60)) == 1:
            return 'a minute ago'
        return f'{int(calculation_time(60))} minutes ago'
    
    elif 0 < seconds < 60:
        if seconds == 1:
            return 'a second ago'
        else:
            return f'{int(seconds)} seconds ago'
        
    return "just now"
    
def validation_time(time):
    if time < 0:
        raise TypeError("Não existe valores negativos para o tempo")
    
time_seconds = 3600
print(to_pretty(time_seconds))
