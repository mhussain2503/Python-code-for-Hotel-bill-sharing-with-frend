print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_percentage = tip/100
percentage_amount = tip_percentage*bill
total_bill= bill+percentage_amount
per_person_amount = total_bill/people
final_amount= round(per_person_amount , 2)
print(f"Each person should pay: ${ final_amount}")


