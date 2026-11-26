def area(l, b):
    return l * b

def perimeter(l, b):
    return 2 * (l + b)

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

print("Area =", area(l, b))
print("Perimeter =", perimeter(l, b))
