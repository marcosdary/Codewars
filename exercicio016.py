from collections import Counter

def naughty_or_nice(data:dict[dict]):
    MONTHS = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 
        'November', 'December'
    ]
    nice = 0
    naughty = 0
    for month in MONTHS:
        data_ = [
            value for value in data[month].values()
        ]
        points = Counter(data_)
        nice += points['Nice']
        naughty += points['Naughty']

    return "Naughty!" if naughty > nice else 'Nice!'
data = {
    'January': {'1': 'Naughty', '2': 'Nice', '3': 'Nice', '4': 'Nice', '5': 'Naughty', '6': 'Nice', '7': 'Nice', '8': 'Naughty', '9': 'Naughty', '10': 'Nice', '11': 'Naughty', '12': 'Naughty', '13': 'Naughty', '14': 'Nice', '15': 'Nice', '16': 'Nice', '17': 'Naughty', '18': 'Nice', '19': 'Nice', '20': 'Nice', '21': 'Naughty', '22': 'Nice', '23': 'Nice', '24': 'Naughty', '25': 'Naughty', '26': 'Naughty', '27': 'Naughty', '28': 'Nice', '29': 'Nice', '30': 'Naughty', '31': 'Nice'}, 
    'February': {'1': 'Naughty', '2': 'Nice', '3': 'Nice', '4': 'Naughty', '5': 'Naughty', '6': 'Nice', '7': 'Naughty', '8': 'Naughty', '9': 'Nice', '10': 'Nice', '11': 'Naughty', '12': 'Nice', '13': 'Naughty', '14': 'Nice', '15': 'Nice', '16': 'Nice', '17': 'Nice', '18': 'Nice', '19': 'Nice', '20': 'Nice', '21': 'Naughty', '22': 'Nice', '23': 'Nice', '24': 'Naughty', '25': 'Nice', '26': 'Naughty', '27': 'Naughty', '28': 'Nice'}, 
    'March': {'1': 'Nice', '2': 'Naughty', '3': 'Nice', '4': 'Nice', '5': 'Naughty', '6': 'Naughty', '7': 'Naughty', '8': 'Naughty', '9': 'Nice', '10': 'Nice', '11': 'Nice', '12': 'Naughty', '13': 'Nice', '14': 'Nice', '15': 'Nice', '16': 'Nice', '17': 'Naughty', '18': 'Nice', '19': 'Naughty', '20': 'Naughty', '21': 'Nice', '22': 'Naughty', '23': 'Nice', '24': 'Naughty', '25': 'Naughty', '26': 'Nice', '27': 'Naughty', '28': 'Nice', '29': 'Naughty', '30': 'Naughty', '31': 'Naughty'}, 
    'April': {'1': 'Nice', '2': 'Naughty', '3': 'Naughty', '4': 'Naughty', '5': 'Naughty', '6': 'Naughty', '7': 'Naughty', '8': 'Naughty', '9': 'Nice', '10': 'Nice', '11': 'Naughty', '12': 'Nice', '13': 'Nice', '14': 'Naughty', '15': 'Nice', '16': 'Nice', '17': 'Naughty', '18': 'Naughty', '19': 'Naughty', '20': 'Nice', '21': 'Nice', '22': 'Naughty', '23': 'Nice', '24': 'Naughty', '25': 'Naughty', '26': 'Naughty', '27': 'Nice', '28': 'Nice', '29': 'Nice', '30': 'Nice'}, 
    'May': {'1': 'Nice', '2': 'Naughty', '3': 'Nice', '4': 'Naughty', '5': 'Naughty', '6': 'Nice', '7': 'Naughty', '8': 'Naughty', '9': 'Naughty', '10': 'Naughty', '11': 'Nice', '12': 'Nice', '13': 'Nice', '14': 'Naughty', '15': 'Naughty', '16': 'Nice', '17': 'Naughty', '18': 'Naughty', '19': 'Naughty', '20': 'Naughty', '21': 'Naughty', '22': 'Nice', '23': 'Naughty', '24': 'Nice', '25': 'Nice', '26': 'Nice', '27': 'Nice', '28': 'Naughty', '29': 'Nice', '30': 'Nice', '31': 'Nice'}, 
    'June': {'1': 'Nice', '2': 'Nice', '3': 'Nice', '4': 'Nice', '5': 'Naughty', '6': 'Naughty', '7': 'Naughty', '8': 'Naughty', '9': 'Nice', '10': 'Naughty', '11': 'Nice', '12': 'Nice', '13': 'Naughty', '14': 'Naughty', '15': 'Nice', '16': 'Naughty', '17': 'Nice', '18': 'Nice', '19': 'Nice', '20': 'Nice', '21': 'Nice', '22': 'Naughty', '23': 'Nice', '24': 'Nice', '25': 'Naughty', '26': 'Nice', '27': 'Naughty', '28': 'Naughty', '29': 'Nice', '30': 'Nice'}, 
    'July': {'1': 'Nice', '2': 'Nice', '3': 'Nice', '4': 'Naughty', '5': 'Naughty', '6': 'Naughty', '7': 'Naughty', '8': 'Naughty', '9': 'Nice', '10': 'Naughty', '11': 'Nice', '12': 'Naughty', '13': 'Nice', '14': 'Nice', '15': 'Nice', '16': 'Naughty', '17': 'Naughty', '18': 'Naughty', '19': 'Nice', '20': 'Naughty', '21': 'Nice', '22': 'Naughty', '23': 'Nice', '24': 'Nice', '25': 'Nice', '26': 'Nice', '27': 'Naughty', '28': 'Nice', '29': 'Nice', '30': 'Naughty', '31': 'Naughty'}, 
    'August': {'1': 'Nice', '2': 'Naughty', '3': 'Naughty', '4': 'Nice', '5': 'Naughty', '6': 'Naughty', '7': 'Naughty', '8': 'Naughty', '9': 'Nice', '10': 'Nice', '11': 'Nice', '12': 'Nice', '13': 'Nice', '14': 'Naughty', '15': 'Nice', '16': 'Naughty', '17': 'Naughty', '18': 'Nice', '19': 'Nice', '20': 'Naughty', '21': 'Naughty', '22': 'Naughty', '23': 'Naughty', '24': 'Naughty', '25': 'Naughty', '26': 'Nice', '27': 'Naughty', '28': 'Naughty', '29': 'Nice', '30': 'Naughty', '31': 'Naughty'}, 
    'September': {'1': 'Naughty', '2': 'Nice', '3': 'Nice', '4': 'Naughty', '5': 'Nice', '6': 'Naughty', '7': 'Naughty', '8': 'Nice', '9': 'Nice', '10': 'Naughty', '11': 'Nice', '12': 'Naughty', '13': 'Naughty', '14': 'Naughty', '15': 'Naughty', '16': 'Naughty', '17': 'Naughty', '18': 'Nice', '19': 'Naughty', '20': 'Nice', '21': 'Nice', '22': 'Nice', '23': 'Nice', '24': 'Naughty', '25': 'Nice', '26': 'Naughty', '27': 'Naughty', '28': 'Nice', '29': 'Naughty', '30': 'Naughty'}, 
    'October': {'1': 'Nice', '2': 'Naughty', '3': 'Nice', '4': 'Naughty', '5': 'Naughty', '6': 'Nice', '7': 'Nice', '8': 'Naughty', '9': 'Nice', '10': 'Naughty', '11': 'Nice', '12': 'Nice', '13': 'Naughty', '14': 'Naughty', '15': 'Naughty', '16': 'Naughty', '17': 'Nice', '18': 'Nice', '19': 'Nice', '20': 'Naughty', '21': 'Nice', '22': 'Naughty', '23': 'Naughty', '24': 'Nice', '25': 'Nice', '26': 'Naughty', '27': 'Nice', '28': 'Naughty', '29': 'Nice', '30': 'Naughty', '31': 'Naughty'}, 
    'November': {'1': 'Naughty', '2': 'Naughty', '3': 'Naughty', '4': 'Naughty', '5': 'Nice', '6': 'Naughty', '7': 'Naughty', '8': 'Naughty', '9': 'Naughty', '10': 'Naughty', '11': 'Naughty', '12': 'Nice', '13': 'Nice', '14': 'Naughty', '15': 'Nice', '16': 'Naughty', '17': 'Nice', '18': 'Naughty', '19': 'Nice', '20': 'Nice', '21': 'Nice', '22': 'Nice', '23': 'Naughty', '24': 'Nice', '25': 'Naughty', '26': 'Naughty', '27': 'Nice', '28': 'Naughty', '29': 'Nice', '30': 'Naughty'}, 
    'December': {'1': 'Nice', '2': 'Naughty', '3': 'Nice', '4': 'Nice', '5': 'Nice', '6': 'Naughty', '7': 'Naughty', '8': 'Nice', '9': 'Naughty', '10': 'Nice', '11': 'Naughty', '12': 'Nice', '13': 'Nice', '14': 'Nice', '15': 'Nice', '16': 'Naughty', '17': 'Nice', '18': 'Naughty', '19': 'Nice', '20': 'Nice', '21': 'Nice', '22': 'Naughty', '23': 'Naughty', '24': 'Nice', '25': 'Naughty', '26': 'Nice', '27': 'Nice', '28': 'Naughty', '29': 'Nice', '30': 'Nice', '31': 'Nice'}
}

naughty_or_nice(data)