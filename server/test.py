# preparing dataset

import random

for i in range(10000):
	min_t = random.uniform(25,30)
	max_t = min_t + random.uniform(1,8)
	mot = random.uniform(0,1)

	human = 0
	nHuman = 0
	if min_t >= 25 and max_t <= 30 and mot >=0.5:
		human = 1
	else :
		nHuman = 1

	print min_t, max_t, mot, human, nHuman