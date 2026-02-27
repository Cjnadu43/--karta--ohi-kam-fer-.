# # Create a greeting for your program.
# # Ask the user for the city that they grew up in and store it in a variable.
# # Ask the user for the name of a pet and store it in a variable.
# # Combine the name of their city and pet and show them their band name.
# print("Hello fello Madristas")
# better = input("Who do you think clears?\n")
# print("Bro MADRID CLEARS")
# Bellingham = input("Bellingham or predri?\n")
# print("Whos pedri bru")
# Madrid = input("Who Has more ucl barca or madrid?\n")
# print("HALA....")
# grade = 89
# print(grade)
print("Welcome to the tip calculator")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tipPercent = tip / 100
tipAmount = bill * tipPercent
totalBill = bill + tipAmount
per_person = totalBill / people

print(f"Each person should pay: ${per_person:.2f}")



