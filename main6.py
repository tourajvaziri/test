def addNumbers(x, y):
    ''' assuming x and y are integers 
      returns the sum of the two
      throws ValueError if x and y are not integers '''
    if (not type(x) is int or not type(y) is int):
        raise ValueError
    return x + y


number1 = 2
number2 = '3'
try:
    total = addNumbers(number1, number2)
except ValueError:
    print('only integers are allowed')
else:
    print('Total is', total)