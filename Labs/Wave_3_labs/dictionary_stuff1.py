# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0 # initializes the result
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for item, value in basket_items.items(): #Iterate through the dictionary
   if item in fruits: #checks if the key(i.e item) is in the list of fruits, 
       result += value #add the value (number of fruits) to result

print(result)
