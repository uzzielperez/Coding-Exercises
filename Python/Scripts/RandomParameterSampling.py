import random
from random import random
from random import seed
from random import randrange
import decimal

"""
 DEFAULT PARAMETER VALUES 
 learning rate	0.1
 n_estimators 	50 
 subsample	0.3
 random state	13
 min samples leaf 100
 max depth 3
"""

for i in range(0,10):
	print (random()/100, randrange(50,70), random(), randrange(1, 15), random(), randrange(1,3))
print "\n"

for i in range(0,10):
	print (random()/10, randrange(50, 70), random(), randrange(1,15), random(), randrange(1,3))

