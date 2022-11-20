#prompting a user to insert a comment that exceed 100 caractersfh -

while True:
    fh= input('Comment:')
    if len(fh) < 100:
        print('Try again , 100 caracters at minimum')
    else:
        continue
