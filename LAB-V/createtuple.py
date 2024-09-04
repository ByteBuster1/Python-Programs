fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')
# I. Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff Tuple:", food_stuff_tp)
# II. Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)
# III. Slice out the middle item(s)
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index]
print("Middle Item(s):", middle_items)
# IV. Slice out the first three items and the last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First Three Items:", first_three)
print("Last Three Items:", last_three)
# V. Delete the food_stuff_tp tuple
del food_stuff_tp