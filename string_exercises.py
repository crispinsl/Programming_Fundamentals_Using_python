# QUESTION 1: Take an input string from the user and create a new string with the first, middle, and last characters of the input string

## STEPS ##
# ask the user to input a string
# get the first character using index 0
# get the last character using index -1
# to get the middle character
#  --get the number of characters the string has using len()
#  --get the index pf the middle character - len/2
#  --get the character at middle index using str[mid_index]
# concatenate a, b, c together

user_str = input("please input a string")
print(user_str)

first_char = user_str[0]
last_char = user_str[-1]

mid_index = int(len(user_str)/2)
mid_char = user_str[mid_index]
result_str = first_char + mid_char + last_char
print(result_str)

# QUESTION 2: