# celcius to fahnrenite
def temperature_conversion():
    x= input('Enter temperature:')
    print(x,'=')
    y= str(x)
    #Making a condition statement with some specif criteria
    if y[3] =='F':
        a=float(y[0:3])
        cel= (a-32)*5.0/9.0
        print(cel,'C')
    elif y[3] == 'C':
        a= float(y[0:3])
        fahrn=(a*9/5)+32
        print(fahrn,'F')
# cm to feet
def cm_to_feet():
    x= input('Enter measure:')
    y= str(x)
    print(y,'=')
    #making a condition statement
    if y[4:6]== 'ft':
        ft= float(y[0])*30.48
        inc= float(y[2:4])* 2.50
        print(ft+inc,'cm')
    elif y[3:5]=='cm':
        cm= float(y[0:3])
        length= cm/2.54
        feet= length / 12
        inc= length -12 * feet
        feets= str(feet)
        print(feets[0],'ft',feets[2],'inch')
temperature_conversion()
print('This is how to you can simply convert\ntemperature with simple python code.\nBut there is also another sophesticated way of doing other measurement\njust by using python simple code.\nFor example:\na.cm to feet and inch')
cm_to_feet()
