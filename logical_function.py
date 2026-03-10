# Logical operations => or, and, not
# or => at least one condition must be true
# and => both conditions must be true
# not => inverts the conditions (Not false, not true)

# cridit card using age 
age=int(input("Enter your age: "))

is_adult=True
#     print("The cridit card validation is canceled")
# else:
#     print("The age is appropreate to use cridit card")
    
    
# if age<18 and is_adult:
#     print(f"{age} is not proper!")
# else:
#     print("poper using")


if age<0 and not is_adult:
    print("poper using") 
       
else:
    print(f"{age} is not proper!")
    
    
