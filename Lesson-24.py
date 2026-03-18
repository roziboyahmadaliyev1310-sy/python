# Membership operator => used to test wether value or varibale is found in a sequence 
#                       (strig,list,tuple,set or dictionary)
#                       1: in
#                       2: not in


# fruit='apple'

# letter=input('Guess a letter in the secret word: ')

# if letter not in fruit:
#     print(f'{letter} has in {fruit}')
# else:
#     print(f'{letter} was not found')
    


students={'malik','golif','ali'}

give_name=input('Enter the student name: ')

if give_name not in students:
    print(f'{give_name} is not a student')
else:
    print(f'{give_name} is a student')
    
grades={'ali':'a',
              'vali':'a',
              'salim':'c',
              'galim':'b'}
name_give=input("Enter the name of student: ")

if name_give in grades:
    print(f"{name_give}`s garde is {grades[name_give]}")
else:
    print(f'{give_name} is a student')