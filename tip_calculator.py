print("Welcome to the tip calculator!")
bill = float(input("Enter the bill amount: "))
tip = int(input("What tip percentage would you like to leave ?: "))
number_of_people = int(input("How many people spliting the bill ?: "))

payment_per_person = (bill + (bill * (tip/100)))/number_of_people

print(f"R{payment_per_person}")