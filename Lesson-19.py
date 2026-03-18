# Function = A block of reusable code 
#            place() after the function name invoke it


# def happy_birthday(name):
#     print(f"happy birthday {name}")
  
    
# happy_birthday("Ruziboy") 
# happy_birthday("sheri")  
# happy_birthday("ahmad")   

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f'Your bill of ${amount:.2f} is due: {due_date}')
    
display_invoice('Ruziboy',79.87,'20/03/2026')


# return function

def add(x,y):
    return x+y
def subtructe(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print(add(2,3))
print(subtructe(4,3))
print(multiply(3,8))
print(divide(9,3))
