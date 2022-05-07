with open('k_2206_input.txt') as file:
	lines = []
	for line in file:
		lines.append(line)

n = float(lines[0])

seq = [int(k) for k in lines[1].split()]

def result(seq):
	answer = []
	checked = set()
	for k in seq[::-1]:
		if k in checked:
			answer.append(k)
		else:
			checked.add(k)
	answer.reverse()
	print(" ".join([str(k) for k in answer]),'\n',len(answer))

result(seq)
