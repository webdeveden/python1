# largest number

largest_so_far= -1
print('Before',largest_so_far)
for num in [0,9,41,12,3,74,15,80,100,-1]:
    if num > largest_so_far:
        largest_so_far=num
    print(largest_so_far,num)
print('after',largest_so_far)
