n=int(input("Enter the number of items:"))
lst=[]
for i in range(n):
    num=int(input("Enter a number:"))
    lst.append(num)
    total=0
    for i in lst:
        total=total+i
    print("list:",lst)
    print("sum of all items:",total)
