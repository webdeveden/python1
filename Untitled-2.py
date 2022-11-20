# this code will only do calculation of number in certain range
x=input('Enter score: ')
#avoiding traceback
try:
    y= float(x)
#specifying a range
    if y< 0.0 or y>1.0:
        print('Not in range')
    elif y== str():
        print('Wrong input')
    elif y>= 0.9:
        print('A')
    elif y>= 0.8:
        print('B')
    elif y>= 0.7:
        print('C')
    elif y>= 0.6:
        print('D')
    else:
        print('F')
except:
    print('wrong input')