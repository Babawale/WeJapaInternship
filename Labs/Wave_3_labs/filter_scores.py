#Filter Names by Scores
#Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

# write your list comprehension here
passed = [name for name, score in scores.items() if score >= 65] # returns every key(name) where the value(score) >=65 in the dictionary

print(passed)
