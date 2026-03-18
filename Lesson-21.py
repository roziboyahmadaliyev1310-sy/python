# Keywrod arguments => An arguments proceded by an indentifier 
#                      helps with readability order of arguments does not matter
#                      1.positional 2.default 3.KEYWORD 4.arbitrary
def hello(greeting, title, first,last):
    print(f'{greeting} {title} {first} {last}')
    
hello("Hello", title='Mr', last='akhmadaliev', first='roziboy')

print('1','2','3','4','5','6','7',sep='-')

def phone_num(country,area,first,last):
    print(country,area,first,last, sep='-')
    # return f'{country}-{area}-{first}-{last}'
    
phone_num(country='82',area='10',first='1234',last='5678')
# print(num)