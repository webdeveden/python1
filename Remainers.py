#Remainers
# this program will tell you if a number is odd or even
scr= input('Enter score:')
# No traceback
try:
    scr= int(scr)
except:
    print('oops, numeric or integer input only')
    quit()
# condition
if scr%2 == 0:
    print(scr,'is an Even number')
else:
    print(scr,'is an ODD number') 
