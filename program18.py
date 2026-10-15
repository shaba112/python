numbers=list(map(int,input("Enter integers separated by spaces:").split()))
odd_numbers=[]
for num in numbers:
    if num %2!=0:
       odd_numbers.append(num)
       print("List after removing even numbers:",odd_numbers)
