
while True:
    x= input('Enter time:')
    a= str(x)
    #continue
    if len(a)<3 and a[1] == 'u':
        y= int(a[0])
        w= y+8
        print(w)
        continue
    elif len(a)>2 and a[2]=='u':
        j= int(a[:2])
        #print(j)
        h= j+8
        print(h,'in Tz')
        #continue
