# input ==> Function that allows to take users input and the data type 
            # of the input is string.
            
# age = input("What is your age? ")
# name = input("What is your name? ")

# print("Your age is: " + age)
# print("Your name is: " + name)

# Finding the date of birth

print("This programm will find your birth year.")
print("-"*30)
age=int(input("What is your age? "))

print(f"Your birth year is {2026 - age}")

product=input("What you want to buy? ")
price=float(input("What is the price of" + product +"?"))
quantity=int(input("How many want to buy? "))
total=price*quantity
print(f"The total price for {quantity} {product}(s) is: ${total}")
