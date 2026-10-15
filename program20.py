text=input("Enter a string:")
if len(text)<3:
     print(text)
elif text.endswith("ing"):
     print(text+"ly")
else:
     print(text+"ing")
