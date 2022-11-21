import calendar

x= calendar.TextCalendar()
print(x.pryear(2022))

# GRADED ASSESSMENT(Google IT Automation)
# 1
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km * 2))

# 2

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

# 3
# if and else statement
def hint_username(username):
    if len(username)<6:
        print('Invalid username. Must contain at least 6 Characters')
    else:
        print(username)
hint_username('Eden')

#4
# The number_group function should return "Positive" if the number received is positive,
#  "Negative" if it's negative,
#  and "Zero" if it's 0
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

# 5
# The function receives a name, then returns a greeting based on whether or not that name is "Taylor".
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

# 6

# If a filesystem has a block size of 4096 bytes, 
# this means that a file comprised of only one byte will still use 4096 bytes of storage.
#  A file made up of 4097 bytes will use 4096*2=8192 bytes of storage

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size // filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * 2
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

# 7
#The longest_word function is used to compare 3 words. It should return the word with the most number of
#  characters (and the first in the list when they have the same length)

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word1)>= len(word2) or len(word2)>= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

# 8
# If both the last_name and the first_name parameters are supplied, string= last_name + first_name
# If only one name parameter is supplied (either the first name or the last name) ,string= first_name of last_name 
# if both names are blank, the function should return the empty string:
def format_name(first_name, last_name):
	# code goes here
	if first_name and last_name != "":
		string="Name: "+last_name+", "+first_name
	elif first_name !="" and last_name=="":
		string="Name: "+ first_name
	elif first_name==""and last_name!="":
		string="Name: "+last_name
	else:
		string=""
	return string
print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


# LOOPS

# 9
#  the current variable needs to be
# initialized to get the function to count down from the start
# number to zero.

def count_down(start_number):
  current=3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

# 10
#  make the print_prime_factors function print all the prime factors of a number. 
# A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

# 11
# The following code can lead to an infinite loop. 
# Fix the code so that it can finish successfully for all numbers

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n!= 0 and n % 2 == 0:
    n = n / 2
    return True
    break
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

# 12
# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it.
#  A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  dv = 1
  while dv < n:
    if n % dv == 0:
      sum += dv
      dv +=1
    else:
      dv+=1
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

# 13 (while loop)
#  multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. 
# An additional requirement is that the result is not to exceed 25, which is done with the break statement. 
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier+= 1
		

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

# 14 (for loop)
#  the factorial of a number is defined as the product of an integer and all the integers below it.
#  For example, the factorial of four (4!) is equal to 1*2*3*4=24.
#  Fill in the blanks to make the factorial function return the right number.
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result=i*result
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


# 15
# Adding a third parameter to the range funtion
# Three parameters will create a sequence starting with the first parameter and stopping before the second parameter,
#  but this time increasing each step by the third parameter.
def to_celcius(x):
  return (x-32)*5/9
for x in range(0,101,10):
  print(x,to_celcius(x))

# 16
# Fill in the blanks to make the factorial function return the factorial of n. 
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember that the factorial of a number is defined as the product of an integer and all integers before it.
#  For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. 
# Also recall that the factorial of zero (0!) is equal to 1.
def factorial(n):
    result = 1
    for x in range(1,n):
        result = result* x
    return result

for n in range(0,10):
    print(n, factorial(n+1))

# RECURSION
# The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1.
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. 

def factorial(n):
    print("Factorial called with "+ str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result= n* factorial(n-1)
    print("Returning "+ str(result)+ " for factorial of "+ str(n))
    return result
factorial(4)

# 14

#Fill in the blanks to make the is_power_of function return whether the number is a power of the given base.
#  Note: base is assumed to be a positive number. 
# Tip: for functions that return a boolean value, you can return the result of a comparison.
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

#15
# The count_users function recursively counts the amount of users that belong to a group in the company system,
#  by going through each of the members of a group and if one of them is a group,
#  recursively calling the function and counting the members.

def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += (count_users(member)-1)
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

#Implement the sum_positive_numbers function, 
# as a recursive function that returns the sum of all positive numbers between the number n received and 1. 
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

def sum_positive_numbers(n):
  if n < 1:
    return 0
  else:
    n+=sum_positive_numbers(n-1)
  return n

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

#16

# Question 3
# Complete the function digits(n) that returns how many digits the number has. 
# For example: 25 has 2 digits and 144 has 3 digits. 
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n>=1):
		count += 1
		n=n/10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

# 17

# Question 4
#This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:

#1 2 3 

#2 4 6 

#3 6 9

def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

# 18

# The counter function counts down from start to stop when start is bigger than stop, 
# and counts up from start to stop otherwise

def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x-=1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x<stop:
				return_string += ","
			x+=1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

# 19

# The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, 
# up to and including the maximum that's passed into the function. 
# For example, even_numbers(6) returns “2 4 6”.

def even_numbers(maximum):
	return_string = ""
	for x in range(2,maximum+1,2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


#STRING INDEXING

# 1

# Want to give it a go yourself? 
# Be my guest! Modify the first_and_last function so that it returns True 
# if the first letter of the string is the same as the last letter of the string, False if they’re different. 
# Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

def first_and_last(message):
    if len(message)==0 or message[0]==message[-1]:
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# Imagine that your company has recently moved to using a new domain,
#  but a lot of the company email addresses are still using the old one. 
# You want to write a program that replaces this old domain with the new one in any outdated email addresses.
#  The function to replace the domain would look like this. 

def  replace_domain(email,old_domain,new_domain):
  if "@"+old_domain in email:
    index= email.index("@"+old_domain)
    new_email= email[:index]+"@" + new_domain
    return new_domain
  return email

#2

#Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, 
# in upper case. 
# For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

#FORMATING STRINGS
# with the formatting expression :.2f , this script will print a float number with only 2 digit after the coma
price= 7.5
with_tax=price * 1.09
print("Base price: ${:.2f}. with Tax: ${:.2f}".format(price,with_tax))

#exemple 2
# In these two expressions we're using the greater than operator to align text to the right so that 
# the output is neatly aligned.
#  In the first expression we're saying we want the numbers to be aligned to the right 
# for a total of three spaces.
#  In the second expression we're saying we want the number to always have exactly two decimal 
# places and we want to align it to the right at six spaces. 

def to_celcius(x):
  return (x-32)*5/9
for x in range (0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x,to_celcius(x)))

#If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).
# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

#"""Outputs:
#apple carrot banana
#"""

#PRACTICE QUIZ : STRINGS
# Question 1
#The is_palindrome function checks if a string is a palindrome. 
#A palindrome is a string that can be equally read from left to right or right to left, 
#omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, 
#and phrases like "Never Odd or Even". 
#Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string.lower():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string.
		if letter.strip():
			new_string +=letter
			reverse_string +=letter
	# Compare the strings
	if new_string[::-1]==reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

# Question 2
#Using the format method, fill in the gaps in the convert_distance function so that it returns 
#the phrase "X miles equals Y km", with Y having only 1 decimal place. 
#For example, convert_distance(12) should return "12 miles equals 19.2 km".

def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

# Question 4
# Fill in the gaps in the nametag function so that it uses the format method 
# to return first_name and the first initial of last_name followed by a period. 
# For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

# Question 5
#The replace_ending function replaces the old string in a sentence with the new string,
# but only if the sentence ends with the old string. 
# If there is more than one occurrence of the old string in the sentence,
# only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") 
#should return abcxyz, not xyzxyz or xyzabc. 
#The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made). 

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = len(old)
		new_sentence = "{sentence}{new}".format(sentence=sentence[:-i],new=new)
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

# LIST

# Question

#Using the "split" string method from the preceding lesson, 
# complete the get_word function to return the {n}th word from a passed sentence.
# For example, get_word("This is a lesson about lists", 4) should return "lesson", 
# which is the 4th word in this sentence. 
# Hint: remember that list indexes start at 0, not 1. 

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


# The skip_elements function returns a list containing every other element from an input list, 
# starting with the first element. 
# Complete this function to do that, using the for loop to iterate through the input list.

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for x in elements:
		# Does this element belong in the resulting list?
		if i % 2 ==0:
			# Add this element to the resulting list
			new_list.append(x)
		# Increment i
		i+=1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# Let's use tuples to store information about a file: its name, its type and its size in bytes. 
# Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 

def file_size(file_info):
	name,type,size= file_info
	return("{:.2f}".format(size/ 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


#ENUMERATE FUNCTION(enumerate())

winners= ["Ashley","Eden","Dylan"]
for index,person in enumerate(winners):
  print("{} - {}".format(index + 1, person))

# 1 - Ashley
# 2 - Dylan
# 3 - Reese

# LIST OF TUPLEs

#  a list of tuples containing two strings each. 
# The first string is an email address and the second is the full name of the person with that email address.
#  You want to write a function that creates a new list containing one string per person including their name and
#  the email address between angled brackets.
#  the format usually used in emails like this (Terrance Ford <terrance@example.com>)
#people is a list of tuples where the first element is the email address and the second one is the full name

def full_emails(people):# defining a function that receives a list of people
  result=[] #  create the variable that we'll use as a return value which will be a list and we'll call it result.
  for email,name in people:# iterate over the list of people
    result.append("{} <{}>".format(name,email))
  return result
print(full_emails([("alex@example.com","Alex Diego"),("shay@example.com", "Shay Brandt")]))

#Complete the skip_elements function to return every other element from the list, 
# this time using the enumerate function to check if an element is in an even position or an odd position.

def skip_elements(elements):
	# code goes here
	list=[]
	i=0
	for i, letter in enumerate(elements):
		if i % 2 ==0:
			list.append(letter)
		i+=1
	return list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# LIST COMPREHENSION

multiples=[]
for x in range(1,11):
  multiples.append(x*7)
print(multiples)

# or

multiples= [x*7 for x in range(1,11)]
print(multiples)

# another example of list comprehension

languages= ["Python","Perl","Ruby","Go","Java","C"]
lenghts= [len(languages) for language in languages]
print(lenghts)

#
a= [x  for x in range (0,102) if x % 2 == 0]
print(a)

# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
# Fill in the blanks in the function, using list comprehension.
#  Hint: remember that list and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
	return [x for x in range(1,n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

# LIST QUIZ
# Q1
#we want to rename all the files with extension hpp to the extension h. 
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
for name in filenames:
    if name.endswith(".hpp"):
        name= name.replace(".hpp",".h")
    newfilenames.append(name)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# Q2
# Let's create a function that turns text into pig latin: 
# a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. 
# For example, python ends up as ythonpay.

def pig_latin(text):
  say = ""
  latin=[]
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    word= word[1:]+word[0]+"ay"
    latin.append(word)
    #return latin
    # Turn the list back into a phrase
    say=" ".join(latin)
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

#Q3

# The permissions of a file in a Linux system are split into three sets of three permissions:
#  read, write, and execute for the owner, group, and others. 
# Each of the three values can be expressed as an octal number summing each permission,
#  with 4 corresponding to read, 2 to write, and 1 to execute. 
# Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
# For example: 
# 640 is read/write for the owner, read for the group, and no permissions for the others; 
# converted to a string, it would be: "rw-r-----"
#755 is read/write/execute for the owner, and read/execute for group and others; 
# converted to a string, it would be: "rwxr-xr-x"

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i>= value:
                result += letter
                i-= value
            else:
                result+="-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

#Q4

# The group_list function accepts a group name and a list of members, 
# and returns a string with the format: group_name: member1, member2, … 
# For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

def group_list(group, users):
  members = ",".join(users)
  return "{}: {}".format(group,members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

#Q5

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, 
# and prints the sentence "Guest is X years old and works as __." for each one. 
# For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer"))
#  should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. 
# Amanda is 25 years old and works as Engineer.

def guest_list(guests):
	for name, age, prof in guests:
		print("{} is {} years old and works as {}".format(name, age, prof))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

# DICTIONARIES

# the followinf script counting how many times each letter appears in a piece of text.

def count_letters(text):
  result={}
  for letter in text:
    if not letter in result:
      result[letter]=0
    result[letter]+=1
  return result

print(count_letters("a long string with a lot of letters"))

#  analyzing logs in your server and you want to count how many times each type of error appears in the log file. 
# You could easily do this with a dictionary by using the type
#  of error as the key and then incrementing the associated value each time you come across that error type. 

def count_logs(types):
    result={}
    for log in types:
        if log == "warning":
            result[log]+=1
        result[log]=0
    return result

print(count_logs())

# our single value can be a list containing multiple values. Here we have a 
# dictionary called "wardrobe" with items of clothing and their colors. Fill in the 
# blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothing, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color,clothing))


# DICTIONARIES

#  generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+'@'+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
 "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#
# The groups_per_user function receives a dictionary, which contains group names with the list of users. 
# Users can belong to multiple groups.
#  Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				user_groups[user]=[]
			user_groups[user].append(groups)

			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


#
# The add_prices function returns the total price of all of the groceries in the  dictionary.
#  Fill in the blanks to complete this function.

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for product, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

# DICTIONARY, LIST AND TUPLE GRADED QUIZ

# Q1
#The format_address function separates out parts of the address string into new strings:
#  house_number and street_name, and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, followed by the street name which may contain numbers,
#  but never by themselves, and could be several words long. 
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".

def format_address(address_string):
  # Declare variables
  street_name= []
  # Separate the address string into parts
  address_parts= address_string.split()
  # Traverse through the address parts
  for address in address_parts:
    # Determine if the address part is the
    # house number or part of the street name
    if address.isnumeric():
      house_number=address
    else:
      street_name+=[address]
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number," ".join(street_name))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

# Q2

# The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day"

def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# Q3

# Complete the steps to combine them into one list as follows: 
# the contents of Drew's list, followed by Jamie's list in reverse order, 
# to get an accurate list of the students as they arrived

def combine_lists(list1, list2):

  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1.reverse()
  list2.extend(list1)
  return list2
  
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


# Q4

# Use a list comprehension to create a list of squared numbers (n*n). 
# The function receives the variables start and end, 
# and returns a list of squares of consecutive numbers between start and end inclusively.

def squares(start, end):
	return [n*n for n in range(start,end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Q5

# Complete the code to iterate through the keys and values of the car_prices dictionary,
#  printing out some information about each one.

def car_listing(car_prices):
  result = ""
  for kind, price in car_prices.items():
    result += "{} costs {} dollars".format(kind,price)+ "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Q6

# combine both dictionaries into one, with each friend listed only once, and the number of guests from
#  Rory's dictionary taking precedence, if a name is included in both dictionaries.
#  Then print the resulting dictionary.

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  guests2.update(guests1)
  return guests2


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Q7

# Use a dictionary to count the frequency of letters in the input string.
#  Only letters should be counted, not blank spaces, numbers, or punctuation.
#  Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") 
# should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
  result = {}
  letters= text.lower()
  # Go through each letter in the text
  for letter in letters:
    # Check if the letter needs to be counted or not
    if letter.isalpha() and not letter in result:
      result[letter]=letters.count(letter)
    # Add or increment the value in the dictionary
    
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


# OBJECT-ORIENTED PROGRAMMING (OOP)

# Defining a class

class Flower():
      color = 'unknown'

rose = Flower()
rose.color = 'red'

violet = Flower()
violet.color = 'blue'

this_pun_is_for_you = 'But no one of those are beautifull like you are, I love you!'

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

# PRACTICE QUIZ

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    you.apples,me.apples = me.apples,you.apples
    return you.apples, me.apples
    
def exchange_ideas(you, me):

    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
    you.ideas,me.ideas = you.ideas + me.ideas,me.ideas + you.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# Q2
#The City class has the following attributes: name, country (where the city is located), 
# elevation (measured in meters), and population (approximate, according to recent statistics). 
# Fill in the blanks of the max_elevation_city function to return the name of the city and its country 
# (separated by a comma), when comparing the 3 defined instances for a specified minimal population. 
# For example, calling the function for a minimum population of 1 million: 
# max_elevation_city(1000000) should return "Sofia, Bulgaria". 

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population and city1.elevation > return_city.elevation:
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3

	#Format the return string
	if return_city.name:
		return "{}, {}".format(return_city.name,return_city.country)
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

#Q3

#We have two pieces of furniture: a brown wood table and a red leather couch.
# Fill in the blanks following the creation of each Furniture class instance, 
# so that the describe_furniture function can format a sentence that describes these pieces as follows: 
# "This piece of furniture is made of {color} {material}"

class Furniture:
    	color = ""
      material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"

# CLASS AND METHODS

# In this code, there's a Person class that has an attribute name, which gets set when constructing the object.
# Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 
# 2) when the greeting() method is called, the greeting states the assigned name.

class Person:
    def __init__(self, name): # __init__ ( this is a special method )
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Eden")  
# Call the greeting method
print(some_person.greeting())

# we use the __str__ special method to tell python to print our desired string

class Apple:
      def __init__(self,color,flavor): # construtor method 
            self.color = color
            self.flavor = flavor
      def __str__(self): # conversion to string function
        # after calling the special method "str" define the way you want the string to be printed as shown below
            return "This Aplle is {} and {}".format(self.color, self.flavor)

jonagold = Apple()
print(jonagold) # printing Jonagold() without telling python that our output should be string , 
#pyhton could pring print random letter and number
      
  

