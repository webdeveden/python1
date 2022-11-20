# bulding a multiplication table

def multiplication():
    multiplier=0
    while multiplier <12:
        multiplier+=1
        for number in range(1,13):
            math= number * multiplier
            print(str(number)+" x "+str(multiplier)+" = "+str(math),end=" \n")
multiplication()
