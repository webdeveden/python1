import re

#Extracting Digits and Summing them
fname= input('File name:')
if len(fname)< 1:
    fname='regex_sum_1362862.txt'
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    flt = re.findall("([0-9]+)", line)
    #converting extrated strings to integer
    for x in flt:
        y= int(x)
        lst.append(y)


print(sum(lst))
 
