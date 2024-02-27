def camel_case(s):
    return string.title().replace(" ", "")
    #return  ''.join(i.capitalize() for i in s.split() if i != ' ')
string = "test case"
output = camel_case(string)
print(output)
