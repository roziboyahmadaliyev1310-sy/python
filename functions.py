# functions


# zip => combaine two varibales
numbers=[1,2,3]
vegitables=['carrot','potato','orange']

for vegistable, number in zip(vegitables,numbers):
    print(f'{number}: {vegistable}')  
    
    
    
# enumerate => gives index + value

fruits={'apple','orange','banana','pineapple'}
for index,fruit in enumerate(fruits):
    print(f'{index}:{fruit}')
    

# map() => applies function to each other

nums=[1,2,3,4,5,6,7,8,9]

squared=list(map(lambda x: x**2, nums))
print(squared)
    
    
    
# filtering() => filters items by conditions

number_list=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x: x % 2==0, number_list))
print(even)

# sorted() => sorts iterable

num_list=[1,2,3,52,2,4,6,4,3,54]

print(sorted(num_list)) 
print(sorted(num_list,reverse=True))