# collection = single 'varibale' used to store multiple values
# List=[] =>ordered and changeable. Duplicates OK
# Set={} => unordered and immuteable, but Add/Remove OK. NO Duplicates
# Tuple=() => ordered and unchangeable. Duplicates OK FASTER

# fruits=['apple','orange','banana','coconut']
# print(dir(fruits))
# print(fruits.pop())
# print(fruits.count())
# print(help(fruits))
# print(fruits[0])
# print(fruits[::-1])
# for x in fruits:
#     print(x)

# fruits=['apple','orange','banana','coconut']

# print(fruits)

# 'append', 'clear', 'copy', 
# 'count', 'extend', 'index', 
# 'insert', 'pop', 'remove', 'reverse', 'sort']
#  |      append(self, object, /)
#  |      Append object to the end of the list.
#  |  
#  |  clear(self, /)
#  |      Remove all items from list.
#  |  
#  |  copy(self, /)
#  |      Return a shallow copy of the list.
#  |  
#  |  count(self, value, /)
#  |      Return number of occurrences of value.
#  |      extend(self, iterable, /)
#  |      Extend list by appending elements from the iterable.
#  |  
#  |  index(self, value, start=0, stop=9223372036854775807, /)
#  |      Return first index of value.
#  |      
#  |      Raises ValueError if the value is not present.
#  |  
#  |  insert(self, index, object, /)
#  |      Insert object before index.
#  |  
#  |  pop(self, index=-1, /)
#  |      remove(self, value, /)
#  |      Remove first occurrence of value.
#  |      
#  |      Raises ValueError if the value is not present.
#  |  
#  |  reverse(self, /)
#  |      Reverse *IN PLACE*.
#  |  
#  |  sort(self, /, *, key=None, reverse=False)
#  |      Sort the list in ascending order and return None.


# fruits={'apple','orange','banana','coconut'}

# print(help(fruits))
# print(len(fruits))
# print('pineapple' in fruits)
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# print(fruits)

# fruits=('apple','coconut','orange','banana','coconut')

# print(fruits.index('apple'))
# print(fruits.count('coconut'))



def get_items(tuple):
    numbers=()
    words=()
    
    for x in tuple:
        numbers+=(x[0],)
        if x[1] not in words:
            words+=(x[1],)
            
    minimum=min(numbers)
    maximum=max(numbers)
    lenght=len(words)
    return minimum,maximum,lenght


test=((1,'a'),(2,'b'),(3,'c'))
(a,b,c)=get_items(test)
print(a,b,c)




def duplication(x,y):
    copy=x[:]
    for i in copy:
        if i in y:
           x.remove(i)
    return x,y
            
list=duplication([1,2,3,4,5],[1,2,3,6,7])
print(list)

