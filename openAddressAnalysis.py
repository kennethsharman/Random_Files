import math

"""
Function gives the upper bounds on the expected number of probes in a hash table search with load
factor alpha.
    Parameters:
        alpha: load factor
        probe: String representation of Probing strategy (Linear, Quadtratic, Double Hashing)
        suceess: Boolean representing the outcome of search (successful or unsuccessful)
    Returns the ceiling value of the number of probes required to perform search
"""
def openAddressingProbes( alpha, probe, success=True):
    if success == False:
        if probe == 'Linear':
            num_probes = 0.5 * ( 1.0 + ( 1.0 / ( 1.0-alpha )**2 ) )
        elif probe == 'Quadratic':
            num_probes = (1.0 / (1.0-alpha) ) - alpha - math.log( 1-alpha )
        elif probe == 'Double Hashing':
            num_probes = 1.0 / ( 1.0-alpha )
    else:
        if probe == 'Linear':
            num_probes = 0.5 * ( 1.0 + ( 1.0 / ( 1.0-alpha ) ) )
        elif probe == 'Quadratic':
            num_probes = 1 - math.log( 1-alpha ) - ( alpha/2.0 )
        elif probe == 'Double Hashing':
            num_probes = ( 1.0 / alpha ) * math.log( 1.0 / (1.0-alpha) )
    return math.ceil( num_probes )

alpha = 3.0/4.0
print( '\n** Load Factor: alpha = 3/4 **' )
print( 'Linear Successful: %11d' % openAddressingProbes(alpha, 'Linear') )
print( 'Linear Unsuccessful: %9d' % openAddressingProbes(alpha, 'Linear', False) )
print( 'Quadratic Successful: %8d' % openAddressingProbes(alpha, 'Quadratic') )
print( 'Quadratic Unsuccessful: %6d' % openAddressingProbes(alpha, 'Quadratic', False) )
print( 'Double Hashing Successful: %3d' % openAddressingProbes(alpha, 'Double Hashing') )
print( 'Double Hashing Unsuccessful: %0d' % openAddressingProbes(alpha, 'Double Hashing', False) )

alpha = 7.0/8.0
print( '\n** Load Factor: alpha = 7/8 **' )
print( 'Linear Successful: %11d' % openAddressingProbes(alpha, 'Linear') )
print( 'Linear Unsuccessful: %9d' % openAddressingProbes(alpha, 'Linear', False) )
print( 'Quadratic Successful: %8d' % openAddressingProbes(alpha, 'Quadratic') )
print( 'Quadratic Unsuccessful: %6d' % openAddressingProbes(alpha, 'Quadratic', False) )
print( 'Double Hashing Successful: %3d' % openAddressingProbes(alpha, 'Double Hashing') )
print( 'Double Hashing Unsuccessful: %0d' % openAddressingProbes(alpha, 'Double Hashing', False) )