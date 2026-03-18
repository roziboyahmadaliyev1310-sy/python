# *args => allows you to pass multiple non-key arguments
#  **kwargs => allows you to pass multiple key-word arguments
#               *unpacking operator
#               1.positonal 2.default 3.keyword 4.ARBITRARY

def add(*nums):
    
    total=0
    for num in nums:
        total+=num
    return total
        
        
print(add(1,2,3,4,5,6,7,8,9))

def display(*args):
    
    for arg in args:
        print(arg, end=' ')
        
display('Dr','Ruziboy','ahmadaliev','abdugulomuvich')
print(display)


def number(**kwargs):
    for key,value in kwargs.items():
        print(key,':',value)

number(steet='tanlillo',city='kyonggido',sate='songnam',zip=324567)


# giving both *args and **kwargs

def intro(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    
    for value in kwargs.values():
        print(value, end=' ')
        
intro('Dr','Ruziboy','ahmadaliev','abdugulomuvich',
      street='123 cake',
      city='muna',
      state='maroit',
      zip='234432')