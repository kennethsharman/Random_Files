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

# Question 1

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

# Question 2
# method 1

# 100 possible passfaces, user selects 20
# C(100,20)
num_pass_set2 = factorial(100) / ( factorial(100-20)*factorial(20) )
print('Number of possible passface sets = %.3e' % num_pass_set2)

prob_guessing = 1.0/num_pass_set2
print('Probability of correctly guessing the set of 20 = %.3e' % prob_guessing )
percent_prob_guessing = 100.0 * prob_guessing
print('%.3e' % percent_prob_guessing, '%')

# Enropy = ceil(log_2(x))
entropy2 = ceil( np.log(num_pass_set2)/np.log(2) )
print('Entropy of 20 passface set', entropy2)

# method 2

# probability of correctly responding to 20 challenges
# each challenge has 2 pics: 1 right and 1 wrong

prob2 = (1.0/2)**20
print('Probability of correctly responding to all 20 challenges %.3e' % prob2)

percent_prob2 = prob2 * 100.0
print('%.3e' % percent_prob2, '%')

# Question 3

def hexxor(a, b):
    '''
    Function returns XOR operation done on 2 strings, assumed to be in hex format
    '''
    return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])

y = '3344ffac'
z = '1100dd0d'
s = hexxor(y,z)
print('secret key = ' + s)

# Challenge x
x = z
print('Challenge =', x)
transmitted = hexxor(x,s)
print('Transmitted Value =', transmitted)
response = hexxor(transmitted, s)
print('Response, z =', response)
#print('Challenge == Response:', x == response)