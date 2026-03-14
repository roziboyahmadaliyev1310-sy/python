# countdown timer program

# import time

# time.sleep(3)

# print("Time`s up")

# my_time=int(input("Enter the time in second: "))

# for x in range(0,my_time):
#     time.sleep(1)
    
# print("TIME`S UP")

# my_time=int(input("Enter the time in second:"))
# # for x in reversed(range(0,my_time)):
# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)
# print("TIME`S UP")

# my_time=int(input("Enter the time in second:"))
# # for x in reversed(range(0,my_time)):
# for x in range(my_time, 0, -1):
#     seconds=x%60
#     minutes=int(x/60)%60
#     hours=x//3600
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("TIME`S UP")


import time
import sys

try:
    my_time=int(input("Enter the time in seconds: "))
    
    if my_time<=0:
        print("Please enter positive number!")
        sys.exit()
        
    for x in range(my_time,0,-1):
        hours=x//3600
        minutes=int(x%3600)//60
        seconds=x%60
        print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end='',flush=True)
        time.sleep(1)
        
    print("\n🧑‍💻TIME`S UP")
except ValueError:
    print("Invalid input! Please enter a number.")
except KeyboardInterrupt:
    print("\n\n⏸️  Timer stopped by user.")
        
