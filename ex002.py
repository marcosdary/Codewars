from functools import reduce

def generate_hashtag(s:str):
    if validation_string(s):
        return False
    
    text = list(map(concatenate_capitalize, s.split(" ")))
    concatenate_formed_text = reduce(lambda ac, x: ac + x, text)
    text_hashtag = f"#{concatenate_formed_text}"
    
    if len(text_hashtag) <= 140 and text_hashtag != "":
        return text_hashtag
    else:
        return False
    
def validation_string(string):
    if string == '':
        return True
    
def concatenate_capitalize(word:str):
    return word.capitalize()
text_example = " Hello there thanks for trying my Kata"
text_example_output = generate_hashtag(text_example)

print(text_example_output)
