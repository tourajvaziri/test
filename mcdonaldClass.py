class McdonaldItem:
    '''
     Assuming ingredientList is a list of string
    '''
    def __init__(self, itemName, price, calorieCount, ingredientList):
        '''
     Assuming ingredientList is a list of string
    '''
        self.__name = itemName
        self.__price = price
        self.__calorieCount = calorieCount
        self.__ingredientList = ingredientList

    def getPrice(self):
        return self.__price

    def getIngredients(self):
        return self.__ingredientList

    def hasAlergen(self, ingredientName):
        return ingredientName in self.__ingredientList


item1 = McdonaldItem('southern style chicken buscuit', 5, 410,
                     ['flour', 'egg', 'chicken'])

item2 = McdonaldItem('double quarter ponder with cheese', 6, 750,
                     ['meat', 'cheese', 'bun', 'pickles'])

print(type(item1))
print('the price of this is ', item1.getPrice())
print('The item has flour: ', item1.hasAlergen('flour'))
