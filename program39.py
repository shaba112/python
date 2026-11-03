def add(*nums):
    """returns the sum of any number of integers"""
    return sum(nums)
nums=list(map(int,input("Enter numbers separated by space:").split()))
print("sum=",add(*nums))
print(add.__doc__)
