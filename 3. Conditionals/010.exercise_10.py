'''
Exercise 10 Conditionals

Bella Napoli pizzeria offers vegetarian and non-vegetarian pizzas to its customers. The ingredients for each type of pizza appear below.

- Vegetarian ingredients: Pepper and tofu.
- Non-vegetarian ingredients: Pepperoni, Ham and Salmon.

Write a program that asks the user if they want a vegetarian pizza or not, and based on their answer, shows them a menu with the ingredients available for them to choose from. 
You can only choose one ingredient besides the mozzarella and tomato that are on all pizzas. At the end it must be shown on the screen whether the chosen pizza is vegetarian 
or not and all the ingredients it contains.
'''


choice = input("Do you want a vegetarian pizza? (Y/N) ").upper()

if choice == "Y":
    print("""
          Since you have chosen a vegetarian pizza, you can select ONE of the following ingredients:
          - 1. Pepper
          - 2. Tofu""")
    ingredient = input("Select an ingredient (1 or 2): ")
    if ingredient == "1":
        ingredients = "The ingredients on this pizza are:\n\t- Mozzarella\n\t- Tomato\n\t- Pepper\n"
    elif ingredient == "2":
        ingredients = "The ingredients on this pizza are:\n\t- Mozzarella\n\t- Tomato\n\t- Tofu\n"
    else:
        ingredient = ""

    if ingredient == "":
        print("That's not a valid ingredient")
    else:
        print(f"\nThis is a vegetarian pizza\n{ingredients}")     
        
elif choice == "N":
    print("""
          Since you have chosen a not vegetarian pizza, you can select ONE of the following ingredients:
          - 1. Pepperoni
          - 2. Ham
          - 3. Salmon""")
    ingredient = input("Select an ingredient (1, 2, or 3): ")
    if ingredient == "1":
        ingredients = "The ingredients on this pizza are:\n\t- Mozzarella\n\t- Tomato\n\t- Pepperoni\n"
    elif ingredient == "2":
        ingredients = "The ingredients on this pizza are:\n\t- Mozzarella\n\t- Tomato\n\t- Ham\n"
    elif ingredient == "3":
        ingredients = "The ingredients on this pizza are:\n\t- Mozzarella\n\t- Tomato\n\t- Salmon\n"
    else:
        ingredient = ""

    if ingredient == "":
        print("That's not a valid ingredient")
    else:
        print(f"\nThis is a not vegetarian pizza\n{ingredients}")     
        
else:
    print("That's not a valid answer")