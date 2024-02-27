def likes(names):
    if len(names) == 0:
        phrase = 'no one likes this'
        return phrase
    elif len(names) == 1:
        single_person_phrase = f'{names[0]} likes this'
        return single_person_phrase
    elif len(names) == 2:
        phrase_of_more_people = f'{names[0]} and {names[1]} like this'
        return phrase_of_more_people
    elif len(names) == 3:
        phrase_of_more_people = f'{names[0]}, {names[1]} and {names[2]} like this'
        return phrase_of_more_people
    else:
        name1, name2, *_ = names
        phrase_of_more_people = f'{name1}, {name2} and {len(_)} others like this'
        return phrase_of_more_people
list_names = ['Alex', 'Jacob', 'Mark', 'Max']
output = likes(list_names)
print(output)