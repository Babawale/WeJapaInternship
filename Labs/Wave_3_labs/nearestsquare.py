#Nearest Square
#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

#For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

# write your while loop here
start_num = 1       # initializes 1 as the least/start number
while (start_num)**2 < limit:
    nearest_square = start_num**2 # computes the square of the number at each time through the loop
    start_num += 1 # increments(changes) the number by 1

print(nearest_square)
