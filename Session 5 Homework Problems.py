# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:02:53 2026

@author: Julian
"""

quantity = int(input("How many widgets do you have? "))
if quantity >= 10 and quantity <= 10000:
    price = 20
else:
    price = 30
extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax
print("Extended Price " + str(extended_price))
print("Tax " + str(tax))
print("Total cost " + str(total)) 

part = input("What is the part number? ")
quantity = int(input("How many parts do you have? "))
if part == "10" or part == "55":
    cost = 1.00
elif part == "20" or part == "65":
    cost = 2.00
elif part == "30" or part == "70":
    cost = 3.00
else:
    cost = 5.00
total = quantity * cost
print("Part number " + str(part))
print("Cost Per Part " + str(cost))
print("Total Cost " + str(total))
      
principle = float(input("Enter principle amount: "))
years = int(input("Enter years to maturity: "))
if principle > 100000 and years == 5:
    rate = 0.06
elif principle >= 50000 and principle <= 100000 and years == 10:
    rate = 0.05
elif principle >= 50000 and principle <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02
interest = principle * rate
print("Principle " + str(principle))
print("The interest rate is " + str(rate))
print("Your first year interest rate is " + str(interest))

tickets = int(input("How many tickets do you have? "))
if tickets >= 25:
    price = 50
elif tickets >= 10:
    price = 60
elif tickets >= 5:
    price = 70
else:
    price = 75
total = tickets * price
print("Number of tickets " + str(tickets))
print("Cost of each ticket " + str(price))
print("Total cost " + str(total))

name = input("What is your employee last name? ")
salary = float(input("What's your salary? "))
level = int(input("What is your job level? "))
if level >= 10:
    rate = 0.25
elif level >= 5:
    rate = 0.20
else:
    rate = 0.10
bonus = salary * rate
print("Employee " + name)
print("Bonus you made" + str(bonus))