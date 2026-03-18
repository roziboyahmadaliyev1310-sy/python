# making Random numbers

import random
first="2006"
number=random.randrange(1000000,9999999)

print(first+str(number))

options=['rock','scissors','paper']
cart=['1','2','3','4','5','6','7','8','9','g','u','p']

option=random.choice(options)
random.shuffle(cart)
print(cart)
print(option)