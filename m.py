#these codes works very well
n= input('Enter number:')
try:
    m= float(n)
    #while True:
    if m== 1:
        print('ON')
    elif m== 0:
        print('OFF')
    else:
        print('Not a binary')
            #break
except:
    print('Error!numeric input only')
