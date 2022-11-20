x= input('Enter Hours:')
y= input('Enter rate:')
try:
    a= int(x)
    w=int(y)
except:
    print('Error, please enter numeric input')

i= a*w
print('Your monthly salary is ' + str(i), end='*****')
print('Your check will be available tommorow')