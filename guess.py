import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('please guess number: ')
    if r == int(num):
        print('nice, you got it')
        print('--------this is ', count, 'times you guess--------')
        break
    else:
        if int(num) > r:
            print('guess samller number')
        else:
            print('guess bigger number')
        print('--------this is ', count, 'times you guess--------')