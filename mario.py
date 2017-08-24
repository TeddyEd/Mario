length = int(input("Length: "))
print('\n' * 24)     
for i in range(1, length + 1):
    space = ' '
    n = length - i
    print(space * n, end = '')
    print('#' * i, end = '')
    print(space * 2, end = '')
    print('#' * i)
