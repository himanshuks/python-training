# PERFORM BELOW OPERATION

"""
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""

# Jan, Feb, Mar, Apr, May
expense = [2200, 2350, 2600, 2130, 2190]

extra = expense[1] - expense[0]
print("Extra spend in Feb", extra)

print(f"Total expense in 1st quater is {expense[0]+expense[1]+expense[2]}")

for i in expense:
    if i == 2000:
        print("Exactly spend 2000 dollars")

# Return TRUE/FALSE if item is present in list
print("Did I spend 2000 dollars ?", 2000 in expense)

# APPEND - add element at the end of the list
expense.append(1980)
print("New expense structure is", expense)

expense[3] = expense[3] - 200
print("After adjusting refund ", expense)
