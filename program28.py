start=int(input("Enter the starting range:"))
end=int(input("Enter the ending range:"))
result=[]
for num in range(start,end+1):
  if 1000<=num<=9999:
     digits=str(num)
     if all(int(digit)%2==0 for digit in digits):
        root=int(num**0.5)
        if root * root == num:
           result.append(num)
print("Result=",result)
