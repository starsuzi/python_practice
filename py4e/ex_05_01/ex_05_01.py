sum=0
cnt=0
while True:
    i = input('Enter a number: ')
    if i == 'done':
        print('sum:', sum)
        print('count:', cnt)
        print('average:', sum/cnt)
        break
    else:
        try:
            sum = sum+int(i)
            cnt = cnt+1
        except:
            print('Invalid data')

        continue
