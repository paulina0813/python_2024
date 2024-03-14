'''
Exercise 10
Write a program that allows you to manage a company's customer database. The customers will be saved in a dictionary in which the key of each customer will be their ID, and 
the value will be another dictionary with the customer's data (name, address, telephone, email, preferred), where preferred will have the value True if This is a preferred 
customer. The program must ask the user for an option from the following menu: (1) Add customer, (2) Delete customer, (3) Show customer, (4) List all customers, 
(5) List preferred customers, (6) End . Depending on the option chosen, the program will have to do the following:

1. Ask for the customer's data, create a dictionary with the data and add it to the database.
2. Ask for the customer's ID and delete their data from the database.
3. Ask for the customer's ID and show their data.
4. Show list of all customers in the database with their ID and name.
5. Show the list of preferred customers from the database with their ID and name.
6. Finish the program.
'''
ids = {}
info = {}
proceed = True

while proceed:
    option = int(input("""
        Please select one of the following options:
        \t1. Add customer
        \t2. Delete customer
        \t3. Show customer
        \t4. List all customers
        \t5. List preferred customers
        \t6. End
        Enter option number: """))
    if option == 1:
        ids = input("Enter the customer ID: ")
        
        info[ids] = {}
        
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        telephone = input("Enter your phone number: ")
        email = input("Enter your email: ")
        preferred = input("Is it a preferred customer? Y/N ").upper()
        if preferred == "Y":
            preferred = True
        elif preferred == "N":
            preferred = False
    
        info[ids]["Name"] = name
        info[ids]["Address"] = address
        info[ids]["Telephone"] = telephone
        info[ids]["Email"] = email
        info[ids]["Preferred"] = preferred
        print("You have added a customer, your customer dictionary is the following ", info)
        
    elif option == 2:
        print("You have selected: Delete customer")
        delete_id  = input("Enter the id that you wish to remove: ")
        info.pop(delete_id, "That's not a valid ID")
        print("Your new customer dictionary is ", info)
        
    elif option == 3:
        id_cust = input("Enter the ID of the customer to see their data: ")
        print(f"The data of the customer with ID {id_cust} is {info[id_cust]}")
        
    elif option == 4:
        print(f'The full list of customers including their IDs and their information is the following\n', info)
        
    elif option == 5:
        print("The list of preferred customers is: ")
        for entry in info:
            if info[entry]["Preferred"] == True:
                print(f'Customer ID: {entry} | Data: {info[entry]}')

    elif option == 6:
        print("Session terminated!")
        proceed = False
    
    else:
        print("That's not a valid selection, please enter a valid number!")