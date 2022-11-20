# this code will print out the score of all number inserted that are in range of 0 to 1
# and if not it will prompt an error message.
score=input('Enter score:')
def computergrade():
    try:
        scr= float(score)
        if scr > 1.0 or scr < 0.0:
            print('Bad score')
        elif scr >= 0.9:
            print('A')
        elif scr >= 0.8:
            print('B')
        elif scr >= 0.7:
            print('C')
        elif scr >= 0.6:
            print('D')
        elif scr < 0.6:
            print('F')
    except:
        print('Error,Numeric input only')
computergrade()
