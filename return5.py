#converting minutes into hours and seconds
def convert_minutes(minutes=int(input('Enter minutes:'))):
    hours= minutes//60
    minutes= minutes-(hours*60)

    return hours,minutes
hours,minutes= convert_minutes()
print(hours,'hr',minutes,'min')