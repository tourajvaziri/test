def myFunction():
    userAge = input('Enter your age: ')
    if (userAge.isdigit() == False):
      raise Exception('Bad input')
    if (int(userAge) < 19):
        return False

myFunction()

