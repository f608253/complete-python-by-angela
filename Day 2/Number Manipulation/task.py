# Calculates BMI: ** runs first (1.65 squared = 2.7225), then 84 is divided by that
# ** has higher precedence than /, so no brackets are needed here
bmi = 84 / 1.65 ** 2

# int() cuts off the decimal part (truncates, does not round), so 30.85... becomes 30
print(int(bmi))

# int() truncates, so 3.76893 becomes 3 (not 4)
print(int(3.76893))

# float() converts to a decimal type; 3.0 is already a float, so it prints 3.0
print(float(3.0))

# round() rounds to the nearest whole number, so 3.76893 becomes 4
print(round(3.76893))

# Simple assignment: stores the value 10 in x
x = 10

# Add and assign: same as x = x + 5
x += 5
print(x)    # 15

# Subtract and assign: same as x = x - 3
x -= 3
print(x)    # 12

# Multiply and assign: same as x = x * 2
x *= 2
print(x)    # 24

# Divide and assign: same as x = x / 4 (result is always a float)
x /= 4
print(x)    # 6.0

# Floor divide and assign: same as x = x // 4
x //= 4
print(x)    # 1.0

# Reset x to an int for the next examples
x = 10

# Modulus and assign: same as x = x % 3 (remainder)
x %= 3
print(x)    # 1

# Exponent and assign: same as x = x ** 4
x **= 4
print(x)    # 1

# f strings
name = "Manav"
age = 25

# The f before the quotes turns on the feature; {name} and {age} are replaced by the variable values
print(f"My name is {name} and I am {age} years old")

# What it is used for:
#
# Putting variables inside text without + or str():
# python
print("Age: " + str(age))   # old way
print(f"Age: {age}")        # f-string way
# Running expressions inside the text:
# python
print(f"Next year: {age + 1}")        # Next year: 26
print(f"Length: {len(name)}")         # Length: 5
print(f"Upper: {name.upper()}")       # Upper: MANAV
# Formatting numbers neatly:
# python
bmi = 30.853211
print(f"BMI: {bmi:.2f}")        # BMI: 30.85  (2 decimal places)
print(f"Total: {1234567:,}")    # Total: 1,234,567  (comma separator)
# Aligning text (useful for tables):
# python
print(f"[{name:>10}]")   # [     Manav]  (right-aligned)
print(f"[{name:<10}]")   # [Manav     ]  (left-aligned)

# Why use f-strings instead of other methods:
#
# Method	Example	Drawback
# Concatenation	"Hi " + name + " " + str(age)	Needs str() for numbers, easy to miss spaces
# Comma in print()	print("Hi", name, age)	Only works inside print(), can’t build a string to store
# .format()	"Hi {} {}".format(name, age)	Longer, values are far from their position
# f-string	f"Hi {name} {age}"	None, it is the most readable and fastest
#
# Things worth noting:

# The f is required: Without it, "{name}" prints as plain text {name}.
# Fixes your earlier error: The TypeError from "..." + len(...) disappears with f"Number of letters: {len(name)}", since numbers are converted automatically.
# Quotes inside {}: Before Python 3.12, use a different quote type inside the braces than the one wrapping the string:

# f strings
score = 0
score += 1
print(score)

# f strings
print("Your score is", score)
# print("Your score is" + score)  # This will give error
print(f"Your score is:{score}")

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")