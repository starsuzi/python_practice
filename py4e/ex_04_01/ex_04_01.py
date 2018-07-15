
hours = input("Enter Hours: ")
try:
    hours = float(hours)
except:
    print('Error, please enter the numeric value')
    quit()

rate = input("Enter Rate: ")
try:
    rate = float(rate)
except:
    print('Error, please enter the numeric value')
    quit()

def compute(hours, rate):
    if float(hours) > 40:
        print('overtime')
        pay = 40*float(rate) + ((float(hours)-40)*float(rate))*1.5
    else :
        print('Regular')
        pay = (float(hours)*float(rate))
        print("Pay:", pay)

compute(hours,rate)
