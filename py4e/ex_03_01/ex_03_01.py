hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = (float(hours)*float(rate))

if float(hours) > 40:
    print('overtime')
    pay = 40*float(rate) + ((float(hours)-40)*float(rate))*1.5
else :
    print('Regular')
    pay = (float(hours)*float(rate))
print("Pay:", pay)
