# pay
hours= input('Enter hours:')
rate= input ('Enter rate:')
hrs= float(hours)
rt= float(rate)

#Normal
if hours == 40:
    pay= hrs*rt
    print('pay:',pay)

else:
    #overtime
    pay=hrs*rt
    ot=(hrs-40)*(rt*0.5)
    tot= pay+ot
    return tot
