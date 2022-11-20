# Traceback code

y= input('Enter number:')
try:
    x= float(y)
    if x > -1:
        print('Well done!')
    else:
        print('Less')
except:
    print('Error! Numeric input only')
