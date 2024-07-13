# Deve conter um par de olhos sorridentes, podem ser -> : ou ;
# Pode ter um nariz, podem ser -> - ou ~ 
# Deve ter uma boca sorridente -> ) ou D
# :) :D ;-D :~)
HAPPYS = [':)', ':D', ';-D', ':~)', ':~D', ';D', ':-D']

def count_smileys(arr):
    return len(list(filter(lambda a: a in HAPPYS, arr))) if len(arr) > 0 else 0

print(count_smileys([
    ';(', ':D', ':-D', ';-D', ':(', ';D', ';D', 
    ':D', ':o(', ';(', ':o(', ';(', ':o(', ';oD', 
    ';-(']
))