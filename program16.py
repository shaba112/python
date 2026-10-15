color_list1=input("Enter colours for list1:").split()
color_list2=input("Enter colours for list2:").split()
for color in color_list1:
  if color not in color_list2:
    print(color)
