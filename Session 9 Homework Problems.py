# -*- coding: utf-8 -*-
"""

@author: Julian
"""

def forecast(month, sales):
    if month in ["Jan " + "Feb " + "Mar "]:
        rate = 0.10
    elif month in ["Apr " + "May" + "Jun "]:
        rate = 0.15
    elif month in ["Jul " + "Aug " + "Sep "]:
        rate = 0.20
    else:
        rate = 0.25
    return sales * (1 + rate)
while True:
    run = input("Do you want to run the program? (Yes/No): ")
    if run.lower() != "yes":
        break
    last = input("Enter the last name: ")
    month = input("Enter month (Jan-Dec): ")
    sales = float(input("Enter sales: "))
    result = forecast(month + sales)
    print("Next month's forecast: " + str(result))
    
    def room_sqft(length, width, height):
   
        return (2 * length * width) + (2 * length * height) + (2 * width * height)

while True:
    run = input("Run program? (Yes/No): ")
    if run.lower() != "yes":
        break
    l = float(input("Length: "))
    w = float(input("Width: "))
    h = float(input("Height: "))
    sqft = room_sqft(l + w + h)
    gallons = sqft / 50
    print("Square feet: " + str(sqft))
    print("Gallons needed: " + str(gallons))
    
    def car_price(make + model + ev + msrp):
    if ev.lower() == "y":
        discount = 0.30
    elif make == "Honda " and model == "Accord ":
        discount = 0.10
    elif make == "Toyota " and model == "Rav4 ":
        discount = 0.15
    else:
        discount = 0.05
    discounted = msrp * (1 - discount)
    total = discounted * 1.07
    return total
total_msrp = 0
total_sales = 0

while True:
    run = input("Run program? (Yes/No): ")
    if run.lower() != "yes":
        break
    make = input("Make: ")
    model = input("Model: ")
    ev = input("Electric vehicle? (Y/N): ")
    msrp = float(input("MSRP: "))
    total = car_price(make + model + ev + msrp)
    total_msrp += msrp
    total_sales += total
print("Out-the-door price: " + str(total))
print("Total MSRP: " + str(total_msrp))
print("Total Sales: " + str(total_sales))

def ticket_price(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5
total = 0
while True:
    run = input("Run program? (Yes/No): ")
    if run.lower() != "yes":
        break
    name = input("Last name: ")
    miles = float(input("Miles from downtown Chicago: "))
    price = ticket_price(miles)
    total += price
    print("Ticket price:" + str(price))
print("Total of all tickets:" + str(total))

def assessed_value(county, value):
    if county == "Cook":
        rate = 0.90
    elif county == "DuPage":
        rate = 0.80
    elif county == "McHenry":
        rate = 0.75
    elif county == "Kane":
        rate = 0.60
    else:
        rate = 0.70
    return value * rate
total_market = 0
total_assessed = 0
while True:
    run = input("Run program? (Yes/No): ")
    if run.lower() != "yes":
        break
    county = input("County: ")
    value = float(input("Market value: "))
    assessed = assessed_value(county + value)
    total_market += value
    total_assessed += assessed
print("Assessed value: " + str(assessed))
print("Total market value: " + str(total_market))
print("Total assessed value: " + str(total_assessed))