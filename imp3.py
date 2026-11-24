
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


# Get input from user
l1 = int(input("Enter length of rectangle 1: "))
w1 = int(input("Enter width of rectangle 1: "))

l2 = int(input("Enter length of rectangle 2: "))
w2 = int(input("Enter width of rectangle 2: "))

# Create objects
r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)

# Compare rectangles
if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 1 does not have smaller area")

