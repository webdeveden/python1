# celcius to fahnrenite
x= input('Enter temperature:')
print(x,'=')
y= str(x)
#Making a condition statement with some specif criteria
if y[1]=='C':
    a= float(y[:1])
    fahrn= (a*9/5)+32
    print(fahrn,'F')
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
elif y[4] == 'C':
    a= float(y[:4])
    fahrn= (a*9/5)+32
    print(fahrn,'F')
elif y[5] == 'C':
    a= float(y[:5])
    fahrn= ((a)*9/5)+32
    print(fahrn,'F')
elif y[3] == 'F':
    a=float(y[:3])
    cel= (a-32)*5.0/9.0
    print(cel,'C')
elif y[4]== 'F':
    a=float(y[:4])
    cel= ((a)-32)*5.0/9.0
    print(cel,'C')
elif y[5] == 'F':
    a=float(y[:5])
    cel= (a-32)*5.0/9.0
    print(cel,'C')
