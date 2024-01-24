'''
print('Hello World')
# for variable names, do not used reserved keywords like "print"

print(help('keywords'))
# this command shows you some keywords recognized by python

# assign multiple variables with the same value simultaneously
a = b = c = 10
print(a, b, c)
# works ... but is not recommended

## Expression VS Statement ##
x = 47
# statement
y = 47 + 10
# expression
'''
'''
# triple quotes can comment out entire sections

# type conversion
# convert to int
print(int(10.24))
print(int(float("10.24")))

# convert to str
print(str(20))
print(type(str(20)))

print(list("hello"))
# prints array of characters - ['h', 'e', 'l', 'l', 'o']
'''
'''
## STRINGS ##
# strings can be created either by using single, double, or triple quotes
first_name = 'Jane'
print(first_name)

last_name = "Doe"
print(last_name)

job1 = "Physician's Assistant"
# since there's a single quote character in this string, double quotes must be used
'''
'''
## STRING FUNCTIONS ##
emp_name = "Jane Doe"
# len() --> returns the number of characters in a given string
print(len(emp_name))

# upper and lower --> these convert the string into corresponding cases
print(emp_name.upper())

# string concatenation
first_name = "Jane"
last_name = "Doe"
print(first_name +' ' + last_name)
# single quote space string is to introduce a space between the first and last names

age = 24
print(first_name + ' ' + last_name + ': ' + str(age))

# string multiplication
print('Hello'*3)
# can only add 2 strings; and can only multiply a string with an int
'''

#Accessing string characters
emp_name = "Jane Doe"
print(emp_name[3])
# print(emp_name[8])
# throws index out of bounds error because the last char is at idx 7

print(emp_name.index('n'))