#Extract First Names
#Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# write your list comprehension here
first_names = [name.split()[0].lower() for name in names] #splits every name in list of names, and returns the first name i.e index = 0 in lowercase
print(first_names)

#last_names = [name.split()[1].lower() for name in names] #splits every name in list of names, and returns the last name i.e index = 1 in lowercase
#print(last_names)
