try:
    a=int(input('~'))
except Exception as error:
    print('User Error','erro :'+str(error))


try:
    a=int(input('~'))
except Exception:
    print('User Error')

try:
    print('opened')
    a=int(input('~'))
    print('Closed')
except ValueError:
    print('Invalid user input')
except TypeError:
    print('type error')
except KeyboardInterrupt:
    print('Keybord Interrupt')
finally:
    print('Closed')
