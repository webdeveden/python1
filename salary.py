#my Daily salary at brady corporation

x= input('Monthly salary:')
ya=input('Days:')
hours=input('hrs:')
ye=float(ya)
hrs=float(hours)
#Hourly
w=float(x)/hrs/ye/4
print('/hr:',w)
#Daily
y=w*7.5
print('Daily:',y)
#Weekly
z=y*ye
print('weekly:',z)
#Annual
di=z*4*12
print('Annual:',di)
