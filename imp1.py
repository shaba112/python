
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Get input from user
l1 = int(input("Enter length of rectangle 1: "))
b1 = int(input("Enter breadth of rectangle 1: "))

l2 = int(input("Enter length of rectangle 2: "))
b2 = int(input("Enter breadth of rectangle 2: "))

# Create objects
r1 = Rectangle(l1, b1)
r2 = Rectangle(l2, b2)

print("Area of Rectangle 1:", r1.area())
print("Perimeter of Rectangle 1:", r1.perimeter())

print("Area of Rectangle 2:", r2.area())
print("Perimeter of Rectangle 2:", r2.perimeter())

# Compare areas
if r1.area() > r2.area():
    print("Rectangle 1 has greater area")
elif r1.area() < r2.area():
    print("Rectangle 2 has greater area")
else:
    print("Both rectangles have equal area")

