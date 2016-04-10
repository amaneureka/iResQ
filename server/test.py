# preparing dataset

import random

for i in range(5000):
	min_t = random.randrange(25,34,_int=float)
	max_t = min_t + random.randrange(1,12,_int=float)
	mot = random.randrange(0,1,_int=float)

	human = 0
	nHuman = 0
	if min_t >= 27 and max_t <= 35 and float(mot) >=0.5:
		human = 1
	else :
		nHuman = 1
	if nHuman == 0:
		print min_t, max_t, mot, human, nHuman
 