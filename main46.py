

import armstrong46

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Armstrong numbers are:")

for i in range(lower, upper + 1):
    if armstrong46.is_armstrong(i):
        print(i)

