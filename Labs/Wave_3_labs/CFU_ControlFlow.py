#Question: What type of loop should we use?
#You need to write a loop that takes the numbers in a given list named num_list:
#num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

#Would you use a while or a for loop to write this code?
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

def sum_first_5_odd(num_list):
    """ The function returns the sum of odd numbers in a list upto the first 5 odd numbers.
    
    Args: the list of numbers
    """
    odd_list = [] #initialize an empty list for the odd numbers
    for num in num_list: #iterates through each number in the list
        if (num%2) != 0 and len(odd_list) <5: #checks for odd number and length of the list of odd numbers
            odd_list.append(num) # appends odd numbers to the list of odd numbers
    if len(odd_list)<2:  # print statement for if there's only one odd number in list.
        print("The only odd number in the list is {}.".format(sum(odd_list)))
    else:
        print("The sum of the first {} odd numbers of the list is {}.".format(len(odd_list),sum(odd_list)))
        
## Please use this space to test and run your code
sum_first_5_odd(num_list)
