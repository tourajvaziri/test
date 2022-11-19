class Animal:
    def makeSound(self):
        print('I am not sure how')


class Cow(Animal):
    def makeSound(self):
        print('Moow')


class Cat(Animal):
    def makeSound(self):
        print('meow')


class JellyFish(Animal):
    pass


cow = Cow()
cat = Cat()
jellyFish = JellyFish()

cow.makeSound()
cat.makeSound()
jellyFish.makeSound()



# class Student:
#     def __init__(self, name, grade):
#         # Attribute
#         self.__name = name
#         self.__grade = grade

#     def getName(self):
#         return self.__name

#     def getGrade(self):
#         return self.__grade

#     def setGrade(self, grade):
#         self.__grade = grade

# class MasterStudent(Student):
#     def __init__(self, name, grade, undergradGrade):
#         super().__init__(name, grade)
#         self.__undergradGrade = undergradGrade

#     def getUndergradGrade(self):
#         return self.__undergradGrade

# mStudent = MasterStudent('Karl', '80', '75')
# print('Student name:', mStudent.getName())
# print('Student grade:', mStudent.getGrade())
# print('Student undergrad grade:', mStudent.getUndergradGrade())

# class Course:
#     __STUDENTS_LIMIT = 20

#     def __init__(self, courseName, courseYear, instructor):
#         self.__name = courseName
#         self.__year = courseYear
#         self.__instructor = instructor
#         self.__studentsEnrolledList = []

#     def getCourseName(self):
#         return self.__name

#     def getCourseYear(self):
#         return self.__year

#     def getInstructor(self):
#         return self.__instructor

#     def setInstructor(self, newInstructor):
#         self.__instructor = newInstructor

#     def enrollStudent(self, studentName):
#         if (len(self.__studentsEnrolledList) < Course.__STUDENTS_LIMIT):
#             self.__studentsEnrolledList.append(studentName)
#         else:
#             raise ValueError('Course is full!')

# math101Course = Course('math101', '2022', 'John')
# for i in range(21):
#     studentName = 'student' + str(i + 1)
#     math101Course.enrollStudent(studentName)
#     print(studentName, 'enrolled')

# class Food:
#     def __init__(self, name):
#         self.__name = name

#     def isHealthy(self):
#         return True

# food = Food('Pasta')
# if food.isHealthy():
#     # More Code
#     print('asdasd')

# #math101Course.studentsEnrolledList.append('Dilnaz')
# print(math101Course.getCourseName())
# print(math101Course.getCourseYear())
# print(math101Course.getInstructor())
# math101Course.setInstructor('Dave')
# print(math101Course.getInstructor())
