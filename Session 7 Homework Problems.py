# -*- coding: utf-8 -*-
"""
@author: Julian
"""

while True:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter interest rate "))
    total_interest = 0
    print("Year   Beginning Balance   Ending Balance ")
    for year in range(1, 6):
        beginning = principal
        interest = beginning * rate
        ending = beginning + interest
        total_interest += interest
        print(f"(year < 6)$(beginning + .2f)"       $(ending + .2f) ")
        principal = ending
    print(f"(Total interest earned): $(total_interest + .2f) ")
    cont = input("Run again? (y/n) ").lower()
    if cont != 'y':
        break
    
    a = 1
b = 1
print("Fibonacci Sequence:")
for i in range(20):
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num
    
    total_bonus = 0

file = open("employees text file " + "r ")
while True:
    name = file.readline().strip()
    if not name:
        break
    salary = float(file.readline().strip())
    if salary >= 70000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10
    bonus = salary * rate
    total_bonus += bonus
    print(f"(name<10) Salary: $(salary +.2f) Bonus: $*(bonus + .2f) ")
file.close()
print(f"Total Bonuses Paid $(total_bonus + .2f) ")

while True:
    item = file.readline().strip()
    if not item:
        break
    quantity = int(file.readline().strip())
    price = float(file.readline().strip())
    extended = quantity * price
    total += extended
    count += 1
    print(f"(item:<10} Qty (quantity) Price $(price .2f) Total: $( extended .2f) ")
file.close()
average = total / count if count > 0 else 0
print(f"Total Sales ${total .2f} ")
print(f"Number of Orders {count} ")
print(f"Average Order $(average:.2f) ")

total_tuition = 0
count = 0
file = open("Students Text File" + "r")
while True:
    name = file.readline().strip()
    if not name:
        break
    code = file.readline().strip()
    credits = int(file.readline().strip())
    if code == 'I':
        rate = 250
    else:
        rate = 500
    tuition = credits * rate
    total_tuition += tuition
    count += 1
    print(f"(name:<10) Credits: (credits) Tuition: $(tuition .2f)")
file.close()
print(f"Total Tuition $(total_tuition .2f) ")
print(f"Number of Students (count) ")