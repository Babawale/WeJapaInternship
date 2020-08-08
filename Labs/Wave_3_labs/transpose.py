#Transpose with Zip
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this!.


data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

# replace with your code
data_transpose = tuple(zip(*data)) # steps: zip the items in unpacked data matrix ; convert the zip to a tuple.
print(data_transpose)
