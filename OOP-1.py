class Point:
    """Represents a point in 2-D space."""

my_point = Point()
# print(type(my_point))

my_point.x = 3
my_point.y = 4

# print(my_point.x)
class Time:
    def print_time(self):
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second))

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return '{:02d}:{:02d}:{:02d}'.format(time.hour, time.minute, time.second)

time = Time()
time.print_time()
time = Time (9)
time.print_time()
time = Time(9, 45)
time.print_time()

time = Time(9, 45)
print(time)
# start = Time()
# start.hour = 9
# start.minute = 45
# start.second = 0

class Student:
    def __init__(self, classes=[], GPA = 0, year='', name=""):
        self.classes = classes
        self.GPA = GPA
        self.year = year
        self.name = name
    def __str__(self):
        k = ', '.join(self.classes)
        return "The student, {}, is a {} wth a {:.2f} GPA and takes {}.".format(self.name, self.year, self.GPA, k)
    def __add__(self, other):
        """Adds one course to the existing list of classes"""
        self.classes.extend(other)
        k = ', '.join(self.classes)
        return "The student, {}, is a {} wth a {:.2f} GPA and takes {}.".format(self.name, self.year, self.GPA, k)
    def drop(self, other):
        """Drops a class from Student.classes"""
        i = self.classes.index(other)
        self.classes.pop(i)

sam = Student()
sam.classes = ['Python', 'Webtech', 'Stats']
sam.year = 'Senior'
sam.GPA = 3.5
sam.name = "Sam"
(sam + ['Excel', 'Global Pop'])
print(sam)
sam.drop('Excel')
print(sam)

rob = Student()
rob.classes = ['QTM', 'Rhetoric', 'Blaw']
rob.year = 'Freshmen'
rob.GPA = 3
rob.name = 'Rob'
rob + sam.classes
print(rob)
rob.drop('QTM')
print(rob)
