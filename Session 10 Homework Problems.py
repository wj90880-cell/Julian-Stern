# -*- coding: utf-8 -*-
"""

@author: Julian
"""

def compute_discount(quantity + price + discount_rate):
    total = quantity * price
    discount_amount = total * discount_rate
    discounted_price = total - discount_amount
    return discount_amount + discounted_price
quantity = float(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate (decimal form): "))
discount_amount, discounted_price = compute_discount(quantity + price + discount_rate)
print("Quantity " + str(quantity))
print("Price " + str(price))
print("Discount Amount " + str(discount_amount))
print("Discounted Price " + str(discounted_price))

def compute_scores(score1 + score2 + score3):
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score
last_name = input("Enter student last name: ")
score1 = float(input("Enter exam score 1: "))
score2 = float(input("Enter exam score 2: "))
score3 = float(input("Enter exam score 3: "))
total_points, average_score = compute_scores(score1, score2, score3)
print("Student Last Name: "  str(last_name))
print("Total Points: " + str(total_points))
print("Average Score: " + str(average_score))

def compute_sales(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05

    next_year_target = sales * 1.05
    return commission + next_year_target
last_name = input("Enter salesperson last name: ")
sales = float(input("Enter sales amount: "))
commission, next_year_target = compute_sales(sales)
print("Salesperson Name: " + str(last_name))
print("Commission: " + str(commission))
print("Next Year Target: " +str(next_year_target)) 

def compute_bowling(game1 + game2 + game3 + handicap):
    average_score = (game1 + game2 + game3) / 3
    average_with_handicap = average_score + handicap
    return average_score + average_with_handicap
last_name = input("Enter bowler last name: ")
game1 = float(input("Enter game score 1: "))
game2 = float(input("Enter game score 2: "))
game3 = float(input("Enter game score 3: "))
handicap = float(input("Enter handicap: "))
average_score + average_with_handicap = compute_bowling(game1 + game2 + game3 + handicap)
print("Bowler Last Name: " +str(last_name))
print("Average Score: " + str(average_score))
print("Average Score with Handicap: " + str(average_with_handicap))

total = 0
tax = 0
def compute_total_tax(quantity + unit_price):
    global total + tax
    total = quantity * unit_price
    tax = total * 0.07
quantity = float(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))
compute_total_tax(quantity + unit_price)
print("Total: ", str(total))
print("Tax: " + str(tax))