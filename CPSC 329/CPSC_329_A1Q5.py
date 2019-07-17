'''
CPSC 329
Assignment #1 - Question 5
Kenneth Sharman
Jan 27, 2018
'''
import numpy as np

'''Hash Function without Salting'''
def hash1(num):
    '''
    Function implements hash function defined in assignment
    Parameter, num: password to be hashed
    Returns hashed value of password
    '''
    a0 = num % 10
    a1 = int(num/10) % 10
    a2 = int(num/10**2) % 10
    a3 = int(num/10**3) % 10
    return (a3**4 + a2**3 + a1**2 + a0) % 100

accepted_hash = hash1(7819)
print('Software is looking for hash value =', accepted_hash )

password = 0 # Start iterartion from 0
# array to store passwords with matching hashes
working_pswd_list = np.array([], dtype=int)

while password < 10000: # iterate from 0-9999
    current_hash = hash1(password) # calculate hash value
    # integer comparison as hashed values are ints
    if current_hash == accepted_hash:
        # if a match, then add to array
        working_pswd_list = np.append(working_pswd_list, password)
        password += 1
    else: password += 1
# verify that all elements of array have correct hash val
for password in working_pswd_list:
    assert hash1(password) == 23

# display results
print('First password found with hash value equal to h(7819)', working_pswd_list[0])
print('Number of Passwords with hash value equal to h(7819) =', len(working_pswd_list))
print('Probability of Guessing =', 100*len(working_pswd_list)/10000.0, '%' )
print(working_pswd_list)

def hash2(salt, num):
    '''
    Function implements hash function (with salt) defined in assignment
    Parameters
        salt: hashing salt
        num: password to be hashed
    Returns hashed value of password
    '''
    s0, s1 = salt %10, int(salt/10) % 10
    a0 = num % 10
    a1 = int(num/10) % 10
    a2 = int(num/10**2) % 10
    a3 = int(num/10**3) % 10
    
    return (10*s1 + s0 + a3**4 + a2**3 + a1**2 + a0) % 100

user_password2 = 7819
salt = 39

accepted_hash2 = hash2(salt, user_password2)
print('Software is looking for hash value =', accepted_hash2)

password2 = 0 # start with password 0000
# array to store passwords with matching hashes
working_pswd_list2 = np.array([])

while password2 < 10000:
    current_hash2 = hash2(salt, password2)
    if current_hash2 == accepted_hash2:
        working_pswd_list2 = np.append(working_pswd_list2, password2)
        password2 += 1
    else: password2 += 1
    
print('Number of Possible Successful Hashes =', len(working_pswd_list2))
print('Probability of Guessing =', \
      100*len(working_pswd_list2)/((2**len(str(salt)))*10000.0), '%' )