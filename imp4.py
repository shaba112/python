
class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        total = (self.__hour * 3600 + self.__minute * 60 + self.__second +
                 other.__hour * 3600 + other.__minute * 60 + other.__second)

        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60

        return Time(h, m, s)

    def display(self):
        print(self.__hour, "hours", self.__minute,
              "minutes", self.__second, "seconds")


# Get input from user
h1 = int(input("Enter hour 1: "))
m1 = int(input("Enter minute 1: "))
s1 = int(input("Enter second 1: "))

h2 = int(input("Enter hour 2: "))
m2 = int(input("Enter minute 2: "))
s2 = int(input("Enter second 2: "))

# Create objects
t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)

# Add two time objects
t3 = t1 + t2

print("Sum of two times:")
t3.display()

