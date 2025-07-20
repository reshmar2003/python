try:
    a=int(input('ONE : '))
    b=int(input('TWO : ')) #Enter the value 'a' to see the error    
    print(a+b)  
except ValueError:
    print('Invalid Error')
except ZeroDivisionError:
    print('Nothing Can be divided by Zero')