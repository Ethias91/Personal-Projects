# You can use this program to calculate sales taxes on a purchase! Curse the US and their inability to include taxes on costs. 
cost = input("What is the subtotal of the product? $")
# Updated to ask what tax rate instead
Tax = input("What is the tax rate of your state? Enter in the format [0.00] ")
Tax_rate = float(Tax) / 100
tax_total = float(cost) * float(Tax_rate)
# I had to look this up
rounded_tax = round(tax_total, 2)
total = float(cost) + float(tax_total)
rounded_number = round(total, 2)
print("Taxes amount: ")
print(rounded_tax)
print("and your total comes out to")
print(rounded_number)