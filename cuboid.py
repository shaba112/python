def area(l, b, h):
    return 2 * (l*b + b*h + h*l)

def perimeter(l, b, h):
    return 4 * (l + b + h)

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Area =", area(l, b, h))
print("Perimeter =", perimeter(l, b, h))
