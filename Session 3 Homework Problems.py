# -*- coding: utf-8 -*-


radius = float(input("What is the radius of the circle? " ))
area = 3.174 * radius * radius
perimeter = 2 * 3.174 * radius
print("The perimeter is " + str(perimeter)) 
print("The area is " + str(area)) 

stock_ticker = str(input("What is the stock ticker? "))
shares = int(input("Number of shares held? "))
cost = float(input("What is the cost per share? "))
amount_invested = shares * cost
print(amount_invested)

last_name = str(input("What is yout last name? "))
midterm = float(input("What was your midterm score? "))
final_exam = float(input("What was your final exam score? "))
total = midterm + final_exam
print(last_name + " Your score was " + str(total))

jobs_earnings = float(input("How much money did you recieve? "))
split = jobs_earnings / 3
print("The amount you earned " + str(split))

car_make = str(input("What kind of car make are you interested in? "))
car_model = str(input("What kind of car model are you interested in? "))
msrp = int(input("How much does the car cost? "))
discount = float(input("What is your discount? "))
amount_discounted = msrp * discount
discounted_price = msrp - amount_discounted
print("Car Make " + car_make)
print("Car Model " + car_model)
print("The Original Price " + str(msrp))
print("Discount " + str(discount))
print("Amount Discounted " + str(amount_discounted))
print ("Final Price " + str(discounted_price))
