# PS3P1
ticker = input("Enter stock ticker symbol: ")
shares = int(input("Enter number of shares: "))
cost_per_share = float(input("Enter cost per share: "))

amount_invested = shares * cost_per_share

print(f"Amount invested in {ticker}: ${amount_invested:.2f}")

# PS3P2
last_name = input("Enter your last name: ")
midterm = float(input("Enter your midterm score: "))
final = float(input("Enter your final exam score: "))

total_points = midterm + final

print(f"{last_name}'s total exam points: {total_points}")

# PS3P3
total_amount = float(input("Enter the total amount received: "))
each_share = total_amount / 3

print(f"Each person receives: ${each_share:.2f}")

# PS3P4
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
msrp = float(input("Enter the MSRP amount: "))
discount_percent = float(input("Enter discount percent (as decimal, e.g., 0.1 for 10%): "))

amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

print(f"Make: {make}, Model: {model}")
print(f"MSRP: ${msrp:.2f}, Discount: {discount_percent*100:.1f}%")
print(f"Amount off: ${amount_off:.2f}, Discounted price: ${discounted_price:.2f}")

# PS3P5
radius = float(input("Enter the radius of the circle: "))
pi = 3.174

area = pi * radius * radius
perimeter = 2 * pi * radius

print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")