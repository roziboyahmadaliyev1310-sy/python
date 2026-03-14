# Python compound interest calculator

principal = 0
rate = 0
time = 0

# First while loop for principal
while True:
        principal = float(input("Enter the principal amount: "))
        if principal <= 0 or principal == '':
            print("Please fill with a positive value!")
            break

while True:
        rate = float(input("Enter the principal amount: "))
        if rate <= 0 or rate == '':
            print("Please fill with a positive value!")
            break

while True:
        time = float(input("Enter the principal amount: "))
        if time <= 0 or time == '':
            print("Please fill with a positive value!")
            break
        
        
total=principal*pow((1+rate/100),time)
print(f"Blanace after {time} yesr/s: ${total:.2f}")