
def nested_range(start, stop):
    lst=[]
    for x in range(start,stop):
        for y in range(x):
            lst.append(y)
            result=  sum(lst)
            print(y)
    print()
    print(result)
            
nested_range(1,200)
        