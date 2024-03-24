# solution with two for loops

'''for i in range(1, 6):
    print('*' * i)
for i in range(4, 0, -1):
    print('*' * i)'''

# solution using one for loop
for i in range(1, 10):
    if i <= 5:
        print('*' * i)
    else:
        print('*' * (10 - i)) # once the loop reaches 6 it will print (10-6=) 4 *s and so on until it reaches (10-9=) 1 *