numbers=list(map(int,input("Enter integer:").split()))
positive=[n for n in numbers if n>0]
print("positive numbers:",positive)

n=int(input("Enter N:"))
squares=[i*i for i in range(1,n+1)]
print("squares:",squares)

word=input("Enter a word:")
vowels=[ch for ch in word if ch in 'aeiouAEIOU']
print("vowels:",vowels)

word=input("Enter a word:")
values=[ord(ch) for ch in word]
print("values:",values)
