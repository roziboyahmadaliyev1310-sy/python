# String Methods

# name=input("Enter your full name: ")
# phone_number=input("Enter your phone number: ")

# length=len(name)
# finder=name.find(" ")
# rfinder=name.rfind('s')
# copitalize=name.capitalize()
# upperr=name.upper()
# lower=name.lower()
# title=name.title()
# digit=name.isdigit()
# alpa=name.isalpha()
# counting=phone_number.count("-")
# replacing=phone_number.replace("-"," ")

# print(replacing)



username=input("Enter username:")
finder=username.find(" ")


if len(username)>=10:
    print('username must not be more than 12 characters' )
elif not username.find(" ")==-1:
    print('Your name can not contain space')
else:
    print('Welcome', username)


