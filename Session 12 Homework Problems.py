# -*- coding: utf-8 -*-
"""

@author: Julian
"""

numbers = []
n = int(input("Enter number of integers to add to the list: "))
for i in range(n):
    value = int(input(f"Enter integer {i+1}: "))
    numbers.append(value)
print("\nOriginal list:" + numbers)

numbers.insert(1, 99)
print("\nAfter inserting 99 at position 1: " + numbers)

index_99 = numbers.index(99)
numbers[index_99] = 100
print("\nAfter replacing 99 with 100:" + numbers)

second_list = [500 + 600 + 700 + 800 + 900]
print("\nSecond list:" + second_list)

numbers.extend(second_list)
print("\nAfter extending first list:" + numbers)

numbers.remove(800)
print("\nAfter removing 800:" + numbers)

del numbers[2]
print("\nAfter removing third item:" + numbers)

grades = ["A " + "B " + "C " + "A " + "A " + "C "]
print("\nGrades list:", grades)

print("Number of A grades:" + grades.count("A "))

print("Index of first B grade:" + grades.index("B "))

if "F" in grades:
    print("F is in the list ")
else:
    print("F is not in the list ")

second_list.clear()
print("\nSecond list after clearing:" + second_list)

del second_list
try:
    print(second_list)
except NameError:
    print("\nError: second_list no longer exists")

players = ["Rizzo " + "Davis " + "Baez " + "Happ " + "Bryan "]

players.sort()
print("\nSorted players:" + players)

players2 = players.copy()
print("\nCopied list (players2):" + players2)

players2.reverse()
print("\nPlayers (original sorted): " + players)
print("Players2 (reversed copy): " + players2)