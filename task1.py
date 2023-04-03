# n = int(input('enter the number of coins'))
# a = input('enter the coins side')
# if len(a) != n:
#     print('the wrong number of sides')
# else:
#     tepmEagle = 0
#     tempTails = 0
#     for i in range(0,n):
#         if a[i] == '1':
#             tepmEagle += 1
#         else:
#             tempTails += 1
#     if tepmEagle < tempTails:
#         print(tepmEagle)
#     else:
#         print(tempTails)


n = int(input('enter the number of coins'))
eagle = 0
tails = 0
for i in range(0,n):
    coinSide = input(f'enter the side (eagle/tails) of coin {i+1}')
    if coinSide == 'eagle':
        eagle += 1
    else:
        tails += 1
if eagle > tails:
    print(tails)
else:
    print(eagle)