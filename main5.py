
ss = {'nov2':[set(),{1,2}]}
ss['nov2'].add(3)
print(ss)


def addNumbers(x, y):
    ''' assuming x and y are integers 
      returns the sum of the two
      throws AssertionError if x and y are not integers '''
    if (not type(x) is int and not type(y) is int):
      raise ValueError
    return int(x) + int(y)


def askUser():
    number1 = input('enter first number: ')
    number2 = input('enter second number: ')
    try:
        total = addNumbers(number1, number2)
    except ValueError:
        print('only integers are allowed')
        askUser()
    else:
        print(total)


askUser()
