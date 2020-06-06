def recursive_multiply(x, y):
    if (x < y):
        return recursive_multiply(y, x)
    elif (y != 0):
        return (x + recursive_multiply(x, y-1))
    else:
        return 0
x = int(input("Enter x"))
y = int(input("Enter y"))
print(recursive_multiply(x, y))