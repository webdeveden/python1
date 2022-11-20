# pound to kilos= lb with 3 digits and kg with 2 digits
x= input('Enter quantity:')
y= str(x)
print(y,'=')
#making a condition statement
if y[3:5]== 'lb':
    kg= float(y[0:3])
    pound= kg* 0.45359237
    #finding [.]then dislay 2 number after
    ad= str(pound)
    pos= ad.find('.')
    rt= ad[:pos+3]
    print(rt,'kg')
elif y[2:4]=='kg':
    pound= float(y[0:2])
    kg= pound / 0.45359237
    #looking for [.] position
    ed= str(kg)
    pos= ed.find('.')
    rt= ed[:pos+3]
    print(rt,'lb')
