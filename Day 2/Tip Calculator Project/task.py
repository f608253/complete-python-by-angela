# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 ?"))
people = int(input("How many people to split the bill? "))
each_person_bill = (bill / people) + (((tip / 100) * bill)/ people)

print(f"Each person should pay: ${each_person_bill:.2f}")

# Retake2
# Prints a welcome message
print("Welcome to the tip calculator.")

# Asks for the total bill; float() is used because the bill can have decimals (e.g. 150.50)
bill = float(input("What was the total bill? $"))

# Asks for the tip percentage; int() is used because tips are whole numbers (10, 12, 15)
tip = int(input("What percentage tip would you like to give? 10 12 15 ? "))

# Asks how many people are splitting the bill; int() because people are whole numbers
people = int(input("How many people to split the bill? "))

# Each person's share of the bill, plus each person's share of the tip
# (tip / 100) converts the percentage to a decimal, e.g. 12 becomes 0.12
each_person_bill = (bill / people) + (((tip / 100) * bill) / people)

# Prints the result rounded to 2 decimal places using an f-string
print(f"Each person should pay: {each_person_bill:.2f}")


