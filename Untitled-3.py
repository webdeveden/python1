import re

x=input('Enter rate:')
fh= open(x)
lst=('a','e','i','o','u','y')
for x in fh:
    y= re.findall('^([0-9])+',x)
    if len(y)!= 1 and x.startswith(lst):
        continue
    print(x)
    #print('nom propre')
