#Modify Usernames with Range
#Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list

#usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

#should change to this:

#usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(len(usernames)): # iterates with indices 0 to (len(usernames) - 1) 
    usernames[i] = usernames[i].lower().replace(" ", "_") # converts the names to lowercase and replaces the space in each name to an underscore.

print(usernames)
