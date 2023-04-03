s = int(input('enter the sum of X and Y: '))
p = int(input('enter the product of X and Y: '))
for x in range(1001):
    for y in range(1001):
        if (s == x + y) and (p == x * y):
            print(x, y)
            break

# s = int(input('enter the sum of X and Y: '))
# p = int(input('enter the product of X and Y: '))
# print('X = ', (s - (s ** 2 - 4 * p) ** (1/2)) / 2)
# print('Y = ', (s + (s ** 2 - 4 * p) ** (1/2)) / 2)