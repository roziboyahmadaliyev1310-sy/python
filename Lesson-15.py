# 2-dimentional list

# fruits=['apple','banana','pineapple']
# bread=['french bread','uzbek bread','bread']
# meats=['chicken','fish','turkey']

# groceries=[fruits,bread,meats]
# # groceries[2][1]='carowa'
# print(groceries)

groceries=[('apple','banana','pineapple'),
           ('french bread','uzbek bread','bread'),
           ('chicken','fish','turkey')]

for collection in groceries:
    for food in collection:
        print(food, end=' ')
    print()
    
    
    
numbers=[(1,2,3),
        (4,5,6),
        (7,8,9),
        ('*',0,'#')]

for number in numbers:
    for num in number:
        print(num,end=' ')
    print()