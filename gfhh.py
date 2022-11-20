import random



lst=[]
while True:
    name= input('Enter name:')
    if len(name) < 1:break

    try:
        name1=name.lower()
        if True:
            lst.append(name1)
            code= random.randint(200000,1000000)
    except:
        print('lower case only')
print(lst)
print(code)

                
