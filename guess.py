import random

r = random.randint(1, 100)
while True:
    num = input('please guess number: ')
    if r == int(num):
        print('nice')
        break
    else:
        if int(num) > r:
            print('guess samller number')
        else:
            print('guess bigger number')