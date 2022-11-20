import re

#Extracting Digits and Summing them
hand = open("regex_sum_1362862.txt")
numlist = []

for line in hand:
    line = line.rstrip()
    extract = re.findall("([0-9]+)", line)

    #if len(extract) < 1 : continue

    for i in extract:
        num = int(extract[1])
        numlist.append(num)

print(sum(numlist))
