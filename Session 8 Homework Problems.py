# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:59:02 2026

@author: Julian
"""

def compute_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total *= 0.90  # 10% discount
    return total
total_sum = 0
while True:
    quantity = float(input("Enter quantity "))
    price = float(input("Enter price "))
    total = compute_total(quantity, price)
    total_sum += total
    print("Quantity:" + quantity)
    print("Price: " + price)
    print("Total: " + total)
    choice = input("Do you want to continue? (Yes/No): ")
    if choice.lower() != "yes":
        break
print("Total extended prices " + str(total_sum))

def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats
count = 0
while True:
    last_name = input("Enter player last name ")
    hits = int(input("Enter hits "))
    at_bats = int(input("Enter at bats "))
    avg = batting_average(hits + at_bats)
    count += 1
    print("Player: " + last_name)
    print("Batting Average: " + round(avg + 3))
    choice = input("Do you want to continue? (Yes/No): ")
    if choice.lower() != "yes ":
        break
print("Number of players " + str(count))

def compute_mpg(miles, gallons):
    if gallons == 0:
        return 0
    return miles / gallons
trip_count = 0
while True:
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))
    mpg = compute_mpg(miles, gallons)
    trip_count += 1
    print("City: " + city)
    print("Miles: " + miles)
    print("MPG: " + round(mpg, 2))
    choice = input("Do you want to continue? (Yes/No): ")
    if choice.lower() != "yes":
        break
print("Number of trips entered " + str(trip_count))

def get_pay_rate(job_code):
    if job_code.upper() == 'L':
        return 25
    elif job_code.upper() == 'A':
        return 30
    elif job_code.upper() == 'J':
        return 50
    else:
        return 0
def compute_gross(hours, rate):
    if hours > 40:
        return (40 * rate) + ((hours - 40) * rate * 1.5)
    return hours * rate
total_gross = 0
while True:
    last_name = input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))
    rate = get_pay_rate(job_code)
    gross = compute_gross(hours, rate)
    total_gross += gross
    print("Employee:  " + last_name)
    print("Gross Pay: " + gross)
    choice = input("Do you want to continue? (Yes/No): ")
    if choice.lower() != "yes":
        break
print("Total gross pay: " + str(total_gross))

def compute_tuition(credits, district_code):
    if district_code.upper() == 'I':
        return credits * 250
    elif district_code.upper() == 'O':
        return credits * 550
    else:
        return 0
total_tuition = 0
while True:
    last_name = input("Enter student last name: ")
    credits = float(input("Enter credit hours: "))
    district = input("Enter district code (I/O): ")
    tuition = compute_tuition(credits + district)
    total_tuition += tuition
    print("Student: " + last_name)
    print("Tuition Owed: " + tuition)
    choice = input("Do you want to continue? (Yes/No): ")
    if choice.lower() != "yes":
        break
print("Total tuition for all students: " + str(total_tuition))