# this program will pull over evry name that start with letter 'E' but if it has 3 names.
fname= input('Enter file name:')
a= open(fname)
#lst=list()
for nam in a:
    nams=nam.split()
    if len(nams) ==2:
        value= nams[1]
        nams.append(value)
        print(nams[0],nams[1],nams[2])
    else:
        print(nams[0],nams[1],nams[2])
