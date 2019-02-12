'''
CPSC 329
Assignment #2 - Random Calculations
Kenneth Sharman
Feb 11, 2019
'''

import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from math import ceil

# 100 possible passfaces, user assigned random 5
# C(100,5)
num_pass_set = factorial(100) / ( factorial(100-5)*factorial(5) )
print('Number of possible passface sets', num_pass_set)

# Enropy = ceil(log_2(x))
entropy = ceil( np.log(num_pass_set)/np.log(2) )
print('Entropy of 5 passface set', entropy)

# probability of guessing correctly 5/5
probability_5of5 = (1.0/9)**5
percent_5of5 = probability_5of5 * 100
print('Probability of Correctly Guessing each verification Step =', probability_5of5)
print('%.3e' % percent_5of5, '%')

# probability of guessing exactly 4/5
p = (1.0/9)
q = 1-p
comb_5_4 = factorial(5) / ( factorial(5-4)*factorial(4) )
probability_4of5 = comb_5_4 * (p)**4 * q**1
percent_4of5 = probability_4of5*100
print('Probability of Correctly Guessing 4/5 = %.3e' % probability_4of5)
print('%.3e' % percent_4of5, '%')
probability_4_or_5of5 = probability_4of5 + probability_5of5
percent_4_or_5of5 = probability_4_or_5of5 * 100
print('Probability of Correctly Guessing when 1 mistake is allowed = %.3e' % probability_4_or_5of5)
print('%.3e' % percent_4_or_5of5, '%')