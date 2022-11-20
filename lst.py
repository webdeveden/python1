# this program will pull over evry name that start with letter 'E'but if it has 3names.
fname= input('Enter file name:')
fh= open(fname)
count=0
letter= input('letter:')
for line in fh:
    line= line.split()
    for lines in line:
        #Atributing line in order to make it as a list
        length= line
        #making a condition or algorithm
        if lines.startswith(letter) and len(length) > 2:
            count= count+1
            print(length)
