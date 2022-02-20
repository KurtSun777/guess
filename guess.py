import random
start = input('please choose start number')
end= input('please choose end number')

start = int(start)
end = int(end)

r = random.randint(start, end)
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