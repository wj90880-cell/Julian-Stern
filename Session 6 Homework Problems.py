# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:14:57 2026

@author: Julian
"""
num = 1
while num <= 25:
    print(num)
    num = num + 2

start = int(input("Enter start value "))
stop = int(input("Enter stop value "))
increment = int(input("Enter increment  "))
current = start
while current <= stop:
    print(current)
    current += increment
    
count = 0
response = input("Do you want to continue? (Yes / No): ")
while response == "Yes":
    last_name = input("Enter your last name ")
    score1 = float(input("Enter first exam score "))
    score2 = float(input("Enter second exam score "))
    avg = (score1 + score2) / 2
    print(last_name + "average " + avg)
    count += 1
    response = input("Do you want to continue? (Yes / No) ")
print("Total students " + str(count))

total_pay = 0
count = 0
response = input("Do you want to continue? (Yes / No) ")
while response == "Yes":
    last_name = input("Enter your last name ")
    hours = float(input("How many hours did you work? "))
    rate = float(input("Enter your pay rate "))
    if hours > 40:
        gross = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        gross = hours * rate
    print(last_name + "gross pay " + gross)
    total_pay += gross
    count += 1
    response = input("Do you want to continue? (Yes / No) ")
if count > 0:
    avg = total_pay / count
else:
    avg = 0
print("Total pay " + str(total_pay))
print("Number of employees " + str(count))
print("Average pay " + str(avg))

total_discount = 0
response = input("Do you want to continue? (Yes / No) ")
while response == "Yes":
    quantity = float(input("Enter quantity  "))
    price = float(input("Enter price  "))
    extended = quantity * price
    if extended > 10000:
        discount = extended * 0.25
    else:
        discount = extended * 0.10
    total = extended - discount
    print("Extended " + extended)
    print("Discount " + discount)
    print("Total " + total)
    total_discount += discount
    response = input("Do you want to continue? (Yes / No) ")
print("Total discounts " + str(total_discount))