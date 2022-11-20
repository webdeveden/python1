#no traceback

x= input('Enter a number:')
try:
    y= int(x)
except:
    y= -1

if y >= 0:
    print('done',x)
else:
    print('not a number')
