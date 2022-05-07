import random

exp = 100000
br = 1

p=0
correct = 0
# for i in range(exp):
# 	n=1
# 	while br > 0 and n <1000:
# 		new_br=False
# 		if random.randint(1,10) <= 4:
# 			new_br = True
# 		if new_br:
# 			br += 1
# 		else:
# 			p+=1
# 			br -=1
# 		n+=1
# 	if p >= 30:
# 		correct +=1

# print(correct/exp * 100000000000000)
n=0
while br > 0 and n <20:
		new_br=False
		if random.randint(1,10) <= 4:
			new_br = True
		if new_br:
			br += 1
		else:
			p+=1
			br -=1
		n+=1
		print(br, p, n)
