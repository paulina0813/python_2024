'''
Exercise 9
Write a program that manages a company's pending invoices. The invoices will be stored in a dictionary where the key of each invoice will be the invoice number and the value 
will be the cost of the invoice. The program should ask the user if they want to add a new invoice, pay an existing one, or terminate. If you want to add a new invoice, it 
will ask for the invoice number and its cost and it will be added to the dictionary. If you want to pay an invoice, you will be asked for the invoice number and it will be 
removed from the dictionary. After each operation, the program must display on the screen the amount collected so far and the amount pending collection
'''
print("Welcome to the invoice manager!")
invoices = {}
proceed = True
pending = 0
collected = 0

while proceed:
    action  = int(input("What do you want to do?\n\t1. Add invoice\n\t2. Pay invoice\n\t3. Finish\nPlease enter 1, 2, or 3: "))
    if action == 1:
        number = input("Enter the invioice number: ")
        amount = float(input("Enter the invoice cost: "))
        invoices[number] = amount
        pending += amount
    elif action == 2:
        if len(invoices) == 0:
            print("You don't have any invoices, please add an invoice!\n")
        else:
            num_check = input("Please enter the invoice number you want to pay: ")
            if num_check in invoices.keys():
                pending -= invoices[num_check]
                collected += invoices[num_check]
                del invoices[num_check]
            else:
                print("That's not a valid invoice number!\n")
    elif action == 3:
        print("You have terminated your session!")
        proceed = False
    else:
        print("That's not a valid option, please select a valid option!\n")
    print("Collected: $" + str(collected) + "\n" + "Pending: $" + str(pending))