# DIctioary => A collection of (key:value) pairs
#               ordered and changeable. No duplicates

capitals={'USA':'Washington DC',
         'Russia':"Moscow",
         'India':"NewDehli",
         'China':'Beijing'}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get('japan'))

# if capitals.get('Russia'):
#     print('The capital does exist')
# else:
#     print('The capital does not exist')

# capitals.update({'Germany':"berlin"})
# capitals.update({'USA':"Texas"})
# capitals.popitem()
# capitals.clear()
# keys=capitals.keys()
# for key in capitals.keys():
#     print(key,end=' ')
# value=capitals.values()

# for value in capitals.values():
#     print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")