# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

#It would be nice to keep track of both the number of fruits and other items in the basket.

#Use this environment below to try out this second part

fruit_count, not_fruit_count = 0, 0 # initializes counts of fruits and not_fruits
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add to fruit_count.
for item, value in basket_items.items(): #Iterate through the dictionary
   if item in fruits: #checks if the key(i.e item) is in the list of fruits, 
       fruit_count += value # add the value (number of fruits) to fruit_count
#if the key is not in the list, then add to the not_fruit_count
   else:
        not_fruit_count +=value # if not adds it to not_fruit_count


print(fruit_count, not_fruit_count)
