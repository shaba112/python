def compare(s1,s2,n):
    return s1[:n]==s2[:n]
a=input("string 1:")
b=input("string 2:")
n=int(input("n:"))
print(compare(a,b,n))
