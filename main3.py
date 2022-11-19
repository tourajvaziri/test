

















userAge = input('Enter your Age: ')
try:
    userAgeInt = int(userAge)
except ValueError:
    print('Enter a valid age.')
else:
    if userAgeInt > 19:
        print('Allowed')
# other code


def kelvinToFahrenheit(temperature):
    assert (temperature > 0)
    return ((temperature - 273) * 1.8) + 32


print(kelvinToFahrenheit(273))
print(kelvinToFahrenheit(-5))



try:
    userAge = input('Enter your Age: ')
    userAgeInt = int(userAge)
    if userAgeInt > 19:
        print('Allowed')
except:
    print('Enter a valid age.')

try:
    print('here')
    # Following more code that might raise an exception
except:
    print('An exception occured')

sum = 10 / 0

variable1 = int('abcd')

list = [10, 7, 6]
list[3]

from replit import db

x = 'hello'
if type(x) != int:
    raise TypeError('Only integers are allowed')

x = -1
if (x < 0):
    raise Exception('x cannot be less than 0')

# def askForNewPassword(username):
#     newPassword = input('Enter a new password: ')
#     runNewPasswordRequirementCheck()
#     db[username] = newPassword
#     print('Welcome to system!')

# def runNewPasswordRequirementCheck(newPassword):
#     if not passwordLengthIsCorrect(newPassword):
#       raise Exception('MUST contain at least 8 characters')
#     if not passwordContainsOneUpperCaseChar(newPassword):

#   and passwordContainsOneUpperCaseChar(
#                 newPassword) and passwordContainsOneUpperCaseChar(
#                     newPassword) and passwordContainsAtLeastOneNumber(
#                         newPassword
#                     ) and passwordContainsAtLeastOneSepcialCharacter(
#                         newPassword):
#         return True

# def passwordLengthIsCorrect(newPassword):
#     if len(newPassword) >= 8:
#         return True
#     else:
#         return False

# def passwordContainsOneUpperCaseChar(newPassword):
#     for c in newPassword:
#         if (c.isupper()):
#             return True
#     print('MUST contain at least one uppercase letter')
#     return False

# def passwordContainsAtLeastOneNumber(newPassword):
#     for c in newPassword:
#         if (c.isdigit()):
#             return True
#     print('MUST contain at least one number')
#     return False

# def passwordContainsAtLeastOneSepcialCharacter(newPassword):
#     tupleSpecialChars = ('(', '!', '”', '#', '$', '%', '&', '(', ')', '*', '+',
#                          '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
#                          '\'', ']', '^', '_', '`', '{', '|', '}', '~', ')')
#     for c in newPassword:
#         if c in tupleSpecialChars:
#             return True
#     print(
#         "MUST contain at least one special character !”#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
#     )
#     return False


def getAge(string):
    '''Assumes string has format name,age
     Return a list '''


def countInString(string):
    ''' Assumes the string is onl with integers.
      Returns the sum of all the  '''
    sum = 0
    for c in string:
        sum = sum + int(c)
    return sum


countInString('asd')


def openFile(fileName):
    file = open(fileName, 'r')
    print(file.readlines())


openFile('fruits3')


def myFUnction(a):
    if (a == 2):
        b = 3
    return b


while (True):
    try:
        userAge = int(input('Enter your Age: '))
        break
    except ValueError:
        print('Enter a valid age.')

#geek = input()
#print(geek)

#list = [10,7,6]
#list[3]

#print('asdas ' + 2)
#myFUnction(4)
#variable1 = int('abcd')

sum = 10 / 0

string = 'hello world' + 2
