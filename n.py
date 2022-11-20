# this code will run without stoping on command line interferce even if you click ctrl+c
n= input()
try:
    m= float(n)
except:
    print('Numeric input only')

while True:
    m= float(n)
    if m== 1:
        print('ON')
    elif m== 0:
        print('OFF')
    else:
        print('Not a binary')
        break
