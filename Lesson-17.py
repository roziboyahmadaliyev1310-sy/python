# Concession stand program

# menu={
#     'apple':3.45,
#     'orange':4.23,
#     'banana':2.50,
#     'pineapple':5.40,
#     'lemon':3.40
# }

# count=[]
# total=0
# print('-----Menu-----')
# for key,value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
    
# while True:
#     food=input("Select a fruit (q to quit)")
#     if food.lower()=='q':
#         break
#     elif menu.get(food) is not None:
#         count.append(food)
        
# for food in count:
#     total+=menu.get(food)
#     print(food, end=' ')

# print()
# print(f'Total is: ${total:.2f}')





groceries={
    'apple':3.50,
    'soda':5.30,
    'book':1.50,
    'banana':4.30,
    'pen':1.00,
    'notebook':4.50,
    'pineapple':3.40,
    'carrot':5.40
}


shoping=[]
total=0

print('-----MENU-----')

for key,value in groceries.items():
    print(f'{key}: ${value}')

while True:
    shop=input("Enter shopping items (q to quit): ")
    if shop.lower()=='q':
        break
    elif groceries.get(shop) is not None:
        shoping.append(shop)
        
for item in shoping:
    total+=groceries.get(item)
    print(item,end=' ')
    
print()
print(f"The total is ${total}")