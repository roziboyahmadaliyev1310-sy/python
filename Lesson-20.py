# Default argumens => A default value for certain parameters
#                      default is used when that argument is omitted
#                       make your function more felxible, reduce the number of arguments
#                      1.positional, 2. DEFAULT, 3.keyword, 4.arbitrary

def new_price(list_price,dicount=0,tax=0.05):
    return list_price*(1-dicount)*(1+tax)

print(new_price(50,0.1,0))


import time

def count(end,start=0,):
    for x in range(start,end+1):
        print(f"\r{x:02}",end=' ',flush=True)
        time.sleep(1)
    print("DONE!")
    
count(10)