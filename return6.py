# converting hours into minutes and seconds
def convert_minutes(hours=int(input('hours:'))):
    minutes= hours * 60
    seconds= minutes * 60

    return minutes,seconds
minutes,seconds= convert_minutes()
print(minutes,'min =',seconds,'sec')
