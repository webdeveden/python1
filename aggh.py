while True:
    fh=input('Enter temperature:')
    y= str(fh)
    if fh=='done':
        break
    elif y[1]=='C':
        a= float(y[:1])
        fahrn= (a*9/5)+32
        print(fahrn,'F')
        #continue
    elif y[1]=='F':
        a=float(y[:1])
        cel= (a-32)*5.0/9.0
        print(cel,'C')
    elif y[2] == 'C':
        a= float(y[:2])
        fahrn= (a*9/5)+32
        print(fahrn,'F')
    elif y[2] == 'F':
        a=float(y[:2])
        cel= (a-32)*5.0/9.0
        print(cel,'C')
    elif y[3] == 'C':
        a= float(y[:3])
        fahrn= (a*9/5)+32
        print(fahrn,'F')
    elif y[3] == 'F':
        a=float(y[:3])
        cel= (a-32)*5.0/9.0
        print(cel,'C')
