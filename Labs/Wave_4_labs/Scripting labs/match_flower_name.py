#For the following practice question you will need to write code in Python in the workspace below. This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files. You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

#Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower

# Write your code here

# HINT: create a dictionary from flowers.txt
def flowers_dict(filename):
    """
    This function opens the flowers.txt, reads every line in it, and saves it as a dictionary.
    
    """
    flowers = {} #initialize the flowers' dictionary
    with open(filename) as f: # open the text file as f.
        for line in f: # reads every line in text file.
            letter = line.split(": ")[0].lower() # splits the line by ":" and takes the first index i.e letter in lower case
            flower = line.split(": ")[1] # splits the line by ":" and takes the second index i.e flower
            #print(flower)
            flowers[letter] = flower # enters the letter and flower as value pairs in the flowers' dictionary.
    return flowers

# HINT: create a function
    
def main():
    """
    The main function as described in the instructions.
    
    """
    flowers = flowers_dict('flowers.txt') # creates the dictionary
    full_name = input("Enter your First [space] Last name only: ") # user input
    first_name = full_name[0].lower() # takes the first index of the full_name i.e first name.
    first_letter = first_name[0] # takes the first letter (index) of the first name.

    print("Unique flower name with the first letter: {}".format(flowers[first_letter])) # prints the flower name that matches the first letter

main() # call the main function