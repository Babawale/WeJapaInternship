#Coding Quiz: Check for Prime Numbers
#Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

#For instance, 6 has four factors: 1, 2, 3, 6.
#1 X 6 = 6
#2 X 3 = 6
#So we know 6 is not a prime number.

#In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.


## Your code should check if each number in the list is a prime number

# the numbers are prime, the code should print "[number] is a prime number."
#If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".
#Example output:

#7 IS a prime number
#26 is NOT a prime number, because 2 is a factor of 26

check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for num in check_prime: # loops through each number in check_prime list.
    for factor in range(2, num): # loop checks for factors of num i.e from [2,3,4,..., num-1]
        if (num % factor) == 0: # checks if it is a factor, i.e num is not a prime number
            print("{} is NOT a prime number, because {} is a factor of {}.".format(num, factor, num))
            break # break the if loop once a factor is found
        
        if factor == num - 1:    # i.e if no factor is found, then num is a prime number.
            print("{} IS a prime number.".format(num))

