# cm to feet
# for ft enter(x'xxft)
while True:
    x= input('Enter measure:')
    y= str(x)
    #print(y,'=')
    #making a condition statement
    if x=='done':
        break
    elif  y[3:5]== 'ft':
        ft= float(y[0])*30.48
        inc= float(y[2:3])* 2.50
        print(ft+inc,'cm')
    elif y[3:5]=='cm':
        cm= float(y[0:3])
        length= cm/2.54
        feet= length / 12
        inc= length -12 * feet
        feets= str(feet)
        print(feets[0],'ft',feets[2],'inch')
