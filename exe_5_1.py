#finding the largest number and the smallest number
largest = -1
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        be= int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest=be
    elif be < smallest:
        smallest= be
    elif be > largest:
        largest= be
        continue
print('Maximum is',largest)
print('Minimum is',smallest)
