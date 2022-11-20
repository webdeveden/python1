# converting second into hours, minutes and second

def convert_seconds(seconds):
    hours= seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remain_seconds = seconds - hours * 3600 - minutes *60
    return hours, minutes, remain_seconds
hours,minutes,seconds = convert_seconds(5000) # because the function returns 3 values, we assigned the result of the function to 3 different value
print(hours, minutes, seconds)