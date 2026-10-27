# Question 1
# Start with some base values
a = 5
b = 10
c = 7
import math
# TODO: Add 3 to a using +=
a += 3
# TODO: Multiply b by 2 using *=
b *= 2
# TODO: Modulo c by 4 using %=
c %= 4

# TODO: Calculate the square root of (a^2 + b^2 + c^2)
result = math.sqrt(a**2 + b**2 + c**3)

# TODO: Print the final result rounded to 2 decimal places
print(f"The answer is {result:.2f}")

#Question 2
# 1. Ask the user to input three integers
x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))
z = int(input("Enter the third integer (z): "))

# creating conditions:
# x is even
is_even = x % 2 == 0
# y is postive
is_positive = y > 0
# z is in range between 10 and 50
is_in_range = 10 <= z <= 50 

# Creating final condition
final_condition = (is_even) and (is_positive) and (is_in_range)

# Print the result
print(f"Final condition: {final_condition}")

# Question 3
# input the score
score = int(input("Enter your base score: "))

# adding bonus
has_bonus = input("Did you receive bonus points? (yes/no): ")
if has_bonus == "yes":
  score += 5

# applying late penalty
is_late = input("Do you have a late penalty? (yes/no): ")
if is_late == "yes":
  score -= 10 

# Clamp score between 0 and 100
score = max(0,min(100, score))

# Determining the grade
if score >= 90:
  grade ="A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"

# Print the resutls
print(f"Final score: {score}, Grade: {grade}")

# Question 4
# Asking user to input numbers 
num1 = int(input("Enter the 1stnumber: "))
num2 = int(input("Enter the 2ndnumber: "))

# inputing the operation
operation = input("Enter the operation (+, -, *, /, % , **,): ")
# Matching the operation
try:
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  elif operation == "%":
    result = num1 % num2
  elif operation == "**":
    result = num1 ** num2
  else:
   print("Invalid operation")
   result = None
except ZeroDivisionError:
  print("error : cannot divide or modulo by zero!")

# Print the result 
if result is not None:
  print(f"Result: {result}")
  



