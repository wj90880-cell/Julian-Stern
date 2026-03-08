# -*- coding: utf-8 -*-

Created on Sat Mar  7 14:32:21 2026

@author: Julian


item_quantity = int(input("How much do you have ?" ))
if item_quantity >= 1000:
    price = 3.00
else:
    price = 5.00
extended_price= item_quantity * price
tax = extended_price * .07
total = extended_price + tax
print("You have " + str(item_quantity))
print("The price is " + str(price) )
print("The extended price is " + str(extended_price))
print("The tax percentage is " + str(tax))
print("The total is " + str(total))


item = str(input("What item do you have? A or B "))
quantity = int(input("How much do you have ?" ))
if item == "A":
    unit_price = 10.00
else: 
    unit_price = 20.00
extended_price = unit_price * quantity
print("Item " + str(item))
print("The unit price is " + str(unit_price))
print("The extended price is " + str(extended_price))


number_books = int(input("How many books do you need to order? "))
cost = float(input("Cost per book "))
order_total = cost * number_books
if order_total > 50.00 :
    order_total = order_total
else:
    order_total = order_total + 25
print("The order total is " + str(order_total))
print("The shipping charge is " + str(0))


appliance_name = str(input("What is the name of the appliance? "))
cost = int(input("What is the cost of the appliance? " ))
if cost > 1000:
    warranty = cost * 0.10
else:
    cost * 0.05 
total = cost + warranty
print("Appliance name " + appliance_name)
print("The appliance costs " + str(cost))
print("The cost of the warranty is " + str(warranty))
print("The total cost is " + str(cost))


last_name = str(input("What is your last name? "))
number_dependents = int(input("What is the number of dependents? "))
gross_income = float(input("How much do you make? "))
adjusted = gross_income - number_dependents * 12000
if adjusted > 50000:
    tax_rate = .20
else:
    tax_rate = .10
income_tax = tax_rate * adjusted
if income_tax < 0:
    income_tax + 100
print("Last Name " + last_name)
print("Your gross income is " + str(gross_income))
print("Number of dependents " + str(number_dependents))
print("Your adjusted gross income is " + str(adjusted))
print("Your income tax is " + str(income_tax)) 


















