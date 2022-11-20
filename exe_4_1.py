
hrs = input("Enter Hours:")
rt= input("Enter rate:")
h=float(hrs)
r=float(rt)

def computepay():
    if h==40:
        pay=h*r

    else:
        #overtime
        ot=(h-40.0)*(r*0.5)
        pay=h*r
        p=pay+ot
        return p
#computepay()
print('Pay',computepay())
