# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

meal_price = float(input("Welcome to your own tip calculator! Let's get started.\nHow much was your meal? $"))
percent_tip = int(input("How much % tip would you like to give? 10, 12, or 15? "))
tip_decimal = percent_tip / 100
contributors = int(input("How many people are splitting the bill? "))
tip_amount = meal_price * tip_decimal
final_bill = meal_price + tip_amount
split_amount = final_bill / contributors

final_amount = round(split_amount, 2)

print(f"Everyone will have to pitch in {final_amount} for the meal.")
