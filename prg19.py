a='ABC123DEF456'

def answer(string):
    alphabets=''
    result=0
    for char in string:
        if char.isdigit():
            result+=int(char)
        else:
            alphabets += char
    return(alphabets,result)
print(answer(a))