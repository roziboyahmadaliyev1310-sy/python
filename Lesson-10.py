# while loops give same code while some conditions remain true




# while True:
#     name=input("Enter your name: ")
#     if name=="":
#         print("Please pay attention. give info!")
#     else:
#         print(f"Welcome {name.capitalize()}")


while True:
    age=input("Enter your age to find your birth year: ")
    if age=="" or age<='0':
        print("Please fill your name!")
    else:
        print(f"Your birth year is {2026-int(age)}")
        
        
        

