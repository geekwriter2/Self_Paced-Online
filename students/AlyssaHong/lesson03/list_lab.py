"""
Author: Alyssa Hong
Date: 10/22/2018
Lesson3 Assignments > List Lab Exercise
"""


#!/usr/bin/env python3
#
#
#Series 1
#
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ["Apples","Pears", "Oranges","Peaches"]
print(fruits)

# Ask the user for another fruit and add it to the end of the list.
response = input("What would you like to add a fruit? ")
fruits.append(response)
print(fruits)

# Ask the user for a number
response = input("What number of fruit would you like to see(the number is 1~5 and you can choose just one)? ")
print(fruits[int(response)-1])

# Add another fruit -- using "+"
print(["Mangos"] + fruits)

# Add another fruit -- using "insert()"
fruits.insert(0, 'Blueberries')
print(fruits)

# Display all the fruits that begin with “P”
for x in fruits:
    if x.startswith('P'):
         print("the fruit that begin with “P” is ", x)


#Series 2
#
print(fruits)

# Remove the last fruit from the list
del fruits[-1:]
print(fruits)

# Ask the user for a fruit to delete, find it and delete it
response = input("What would you like to delete any fruit in the list? ")
fruits.remove(response)

# ??? (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
print(fruits)


#Series 3
#
fruits = ["Apples","Pears", "Oranges","Peaches"]
yes_choice = ['yes']
no_choice = ['no']
fruit_cnt=0

# Ask the user for input
# For each “no”, delete that fruit from the list
while fruit_cnt<len(fruits):
    response = input("Do you like " + fruits[fruit_cnt].lower() + "? yes/no > ")
    if response in yes_choice:
        fruit_cnt+=1
        continue
    elif response in no_choice:
        fruits.remove(fruits[fruit_cnt])
        continue
    else:
        print("Please input yes/no")
        continue

print(fruits)

#Series 4
#
# Make a copy of the list and reverse the letters in each fruit in the copy
fruits = ["Apples","Pears", "Oranges","Peaches"]
original_fruits = fruits
copy_fruits = []
for fruit in original_fruits:
    # copy_fruits = ''.join(reversed(fruit))
    # print(copy_fruits)
    # copy_fruits.append(copy_fruits)
    copy_fruits.append(''.join(reversed(fruit)))
## print(','.join(copy_fruits))

# Delete the last item of the original list
del fruits[-1:]
fruits = fruits + copy_fruits
print(fruits)
