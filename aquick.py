
def is_palindrome(input_string):
	# We'll create two strings, to compare them
    string= input_string.strip()
    reverse_string= string[::-1]
    return reverse_string

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
