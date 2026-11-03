def simple_interest(p,t,senior):
  rate=12 if senior else 10
  return p*rate*t/100
p=float(input("principal:"))
t=float(input("Time(years):"))
s=input("senior citizen?(yes/no):")
print("simple interest=",simple_interest(p,t,s=="yes"))
