#Zip Lists to a Dictionary
#Use zip to create a dictionary cast that uses names as keys and heights as values.

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

# replace with your code
cast = dict(zip(cast_names, cast_heights)) # zips both list together and converts to dictionary
print(cast)
