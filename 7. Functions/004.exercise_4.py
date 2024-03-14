'''
Exercise 4
Write a function that calculates the total of an invoice after applying VAT. The function must receive the amount without VAT and the percentage of VAT to be applied, and 
return the total of the invoice. If the function is invoked without passing the VAT percentage, 21% must be applied.
'''

def invoice():
    amount = float(input("Enter amount: "))
    vat_entered = input("Do you wish to enter a VAT percentage? Y/N ").upper()
    
    if vat_entered == "Y":
        vat = float(input("Enter VAT percentage: "))
    else:
        vat = 21
    
    total = amount + amount * (vat / 100)
    
    return total

print(invoice())

'''
Solution 2
def invoice(amount, vat=21):
    return amount + amount*vat/100

print(invoice(1000,10))
print(invoice(1000))

'''