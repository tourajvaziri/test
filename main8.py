class Person:
    def __init__(self, firstName, lastName, dateOfBirth, occupation):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__occupation = occupation

    def getName(self):
        return self.__firstName + ' ' + self.__lastName

    def getAge(self):
        return None

    def setOccupation(self, newOccupation):
        self.__occupation = newOccupation


p1 = Person('John', 'Smith', '12.01.1995', 'Musician')
p1.getName()

p1.setOccupation('Director')

string = 'hello'
print(type(string))

#print(string.upper())


class Student:
    def __init__(self, name, grade):
        # Attribute
        self.__name = name
        self.__grade = grade

    def getName(self):
        return self.__name

    def getGrade(self):
        return self.__grade

    def setGrade(self, grade):
        self.__grade = grade


class MasterStudent(Student):
    def __init__(self, name, grade, undergradGrade):
        super().__init__(name, grade)
        self.__undergradGrade = undergradGrade

    def getUndergradGrade(self):
        return self.__undergradGrade

mStudent = MasterStudent('Karl', '80', '75') 


class Course:
    __totalCourses = 0

    def __init__(self, name, max_students):
        self.__name = name
        self.__maxStudents = max_students
        self.__students = []
        Course.__totalCourses = 10

    def addStudent(self, student):
        if (len(self.__students) > self.__maxStudents):
            raise Exception('Course is full!')
        self.__students.append(student)

    def getStudents(self):
        return self.__students

    def getAverageGrade(self):
        sum = 0
        for s in self.__students:
            sum = sum + s.getGrade()
        return sum / len(self.__students)

    @classmethod
    def getTotalCourses(cls):
        return cls.__totalCourses


#dog = Student('Tom', 14)
#dog.bark()
#print(type(dog))
#print(dog.getName())

math = Course('math', 20)
for i in range(20):
    student = Student('student ' + str(i), 18 + i)
    math.addStudent(student)
    #print(student.getName(), 'successfully added')

#for s in math.getStudents():
#   print(s.getName())

#print(math.getAverageGrade())

masterStudent = MasterStudent('Ali', 20, 18)
#print('getgrade ', masterStudent.getUndergradGrade())
#print(masterStudent.getGrade())
#print(Course.getTotalCourses())


class Math:
    @staticmethod
    def sum(x, y):
        return x + y


#print(Math.sum(3, 4))
