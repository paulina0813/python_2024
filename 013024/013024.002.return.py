'''
002. Return
- All functions return something
- Not all functions print something
- A function should be able to do one thing right
- When you use a return, you exit the function
'''
consumption = float(input("Please enter the total amount: "))
desired_tip = float(input("Enter the tip amount (10, 12, 15, 20): "))

def percentage_conversion(desired_tip):
    result = desired_tip / 100
    return result

tip_percentage = percentage_conversion(desired_tip)

def calculate_tip_amount(consumption, tip_percentage):
    result = consumption * (1 + tip_percentage)
    return result

print(calculate_tip_amount(500, tip_percentage))

'''
calculated_tip = percentage_conversion()

def round_two_decimals(value, decimals = 2):
    return round(value, 2)

total = round_two_decimals(550.4567)
tip = round_two_decimals(calculated_tip)

def tip_calculator(total, tip_amount, people):
    tip = (total * tip_amount) / people
    return f'Ammount consumed ${round(total,2)}'

print(tip_calculator(7382.60, 0, 3))
'''