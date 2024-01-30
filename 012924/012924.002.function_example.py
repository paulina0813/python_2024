'''
def sum_two(num1, num2):
    result = int(num1) + int(num2)
    return result
sum_two(5,1)
'''

def team(team_name):
    return f"The team name is {team_name}"
print(team("Oracle Red Bull Racing"))

def drivers(team, driver_one, driver_twoe):
    return f"{team}. The drivers are {driver_one} and {driver_twoe}"
print(drivers(team("Oracle Red Bull Racing"), "Max Verstappen", "Sergio Pérez"))

input_team = team("Oracle Red Bull Racing")
print(drivers(team, "Max Verstappen", "Sergio Pérez"))

user_team = input("Enter the name of a team: ")
input_team = team(user_team)
user_driver_one = input("Enter the name of the first driver: ")
user_driver_two = input("Enter the name of the second driver: ")
print(drivers(input_team, user_driver_one, user_driver_two))