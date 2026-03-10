# if stetment => do some thing if condition is true
                # else statement => do some thing if condition is false
                
                
# univer_age=int(input("Enter your age: "))

# if univer_age>=18 and univer_age<=25:
#     print("You are eligible to apply for university.")
    
# elif univer_age<=0:
#     print("Invalid age entered.")
# else:
#     print("You are not eligible to apply for university.")
       
# online=False

# if online:
#     print("You are online.")
# else:
#     print("You are offline.")

operator=input("Enter the operator (+, -, *, /): ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if operator=="+":
    print(f"The result of {num1} + {num2} is: {(num1+num2)}")
    
if operator=="-":
    print(f"The result of {num1} - {num2} is: {(num1-num2)}")
    
if operator=="*":
    print(f"The result of {num1} * {num2} is: {(num1*num2)}")
    
if operator=="/":
    print(f"The result of {num1} / {num2} is: {(num1/num2)}")
    
if operator=="**":
    print(f"The result of {num1} ** {num2} is: {(num1**num2)}")
