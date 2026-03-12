# Conditional expression = A one-line shortcut code for if and else
#                           X if condition else Y

# num=3

# result="Even" if num&2==0 else "ODD"
# print(result)

# age=input("Enter your age: ")

# ages="Adult" if age>='18' else "children"
# print(ages)


# weather=float(input("Enter the weather of your city: "))

# temperature="HOT" if weather>=20 else "COLD"

# print(temperature)

access_level=input("Enter your status(Admin or Guest): ")

authority="Full Access" if access_level.lower()=="admin" else "Limited Access"

print(authority)