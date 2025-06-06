"""
Topic: Python If_Else
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""
a = 42
b = 2077
if b > a:
  print("b is greater than a")
"""
Python relies on indentation (whitespace at the beginning of a line)
to define scope in the code. Other programming languages often use curly-brackets for this purpose.
"""

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition":
a = 42
b = 42
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#The else keyword catches anything which isn't caught by the preceding conditions:
a = 2077
b = 42
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement:
if a > b: print("a is greater than b")

#Short Hand If_Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 42
b = 2077
print("A") if a > b else print("B")
#This technique is known as Ternary Operators, or Conditional Expressions.

#One line if else statement, with 3 conditions:
a = 2077
b = 2077
print("A") if a > b else print("=") if a == b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#The "and" keyword is a logical operator, and is used to combine conditional statements:
a = 2077
b = 42
c = 6800
if a > b and c > a:
  print("Both conditions are True")

#The "or" keyword is a logical operator, and is used to combine conditional statements:
a = 2077
b = 42
c = 6800
if a > b or a > c:
  print("At least one of the conditions is True")

#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 42
b = 6800
if not a > b:
  print("a is NOT greater than b")

#You can have if statements inside if statements, this is called nested if statements.
x = 42
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the "pass" statement to avoid getting an error:
a = 42
b = 2077
if b > a:
  pass
