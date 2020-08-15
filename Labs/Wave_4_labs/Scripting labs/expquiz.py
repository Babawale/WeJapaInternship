#It's your turn to import and use the math module. Use the math module to calculate e to the power of 3. print the answer.
# print e to the power of 3 using the math module



import math # import the math module
print(math.exp(3)) # print e to the power of 3

import math as m # import the math module with an alias
print(m.exp(3)) # print e to the power of 3

from math import exp # import the exp function from the math module
print(exp(3)) # print e to the power of 3

from math import exp as e # import the exp function from the math module with an alias
print(e(3)) # print e to the power of 3

# returns nothing; asserting that all 4 approaches give the same values
assert math.exp(3) == m.exp(3)
assert math.exp(3) == exp(3)
assert math.exp(3) == e(3)