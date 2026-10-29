# Print Type Checking

print(type(123))
print(type(233.56))
print(type(334548545483489238329327464.0))
print(type(0))
print(type("123"))

#print("Number of letters in your name: " + len (input("Enter your name"))) # This will give TypeError: can only concatenate str (not "int") to str

# Fix 1: Convert the number to a string with str()

# len() returns an int, so str() converts it to text before concatenating
print("Number of letters in your name: " + str(len(input("Enter your name "))))

# Fix 2: Use a comma instead of + (no conversion needed)
# The comma lets print() handle the string and the number separately
print("Number of letters in your name:", len(input("Enter your name ")))

# Fix 3: Use an f-string
# The f-string places the value inside the text, converting it automatically
print(f"Number of letters in your name: {len(input('Enter your name '))}")

# Fix 4 (most readable): Split into steps
# Store the input, calculate the length, then print
name = input("Enter your name ")
length = len(name)
print("Number of letters in your name:", length)

# Task - Write out 4 type checks to print all 4 data types in Python
# str , int , float , bool

print(type("Hello Manav"))
print(type(123))
print(type(233.56))
print(type(True))
print(type(False))

# Below will give 'ValueError'
print(int("abc") + int("456"))