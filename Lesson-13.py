# Nested loop => A loop with another inner side loop(outer, inner)
#                   outer loop:
#                       inner loop:

rows=int(input("Enter the # of rows: "))
columns=int(input("Enter the # of columns: "))
symbol=input("Enter the symbol to use: ")
for x in range(rows):
    for y in range(columns):
        if x==0 or x==rows-1 or y==0 or y==columns-1:
            print(symbol,end='')
        else:
            print(" ",end='')
    print()


rows=int(input("Enter the # of rows: "))
symbol=input("Enter the symbol to use: ")
for x in range(rows,0,-1):
    space=' '*(rows-x)
    symbols=symbol*(2*x-1)
    print(space+symbols)   


rows=int(input("Enter the # of rows: "))
symbol=input("Enter the symbol to use: ")
for x in range(1,rows+1):
    print(symbol*x)
    
rows=int(input("Enter the # of rows: "))
symbol=input("Enter the symbol to use: ")
for x in range(rows,0,-1):
    print(symbol*x)