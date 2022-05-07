import math

with open('j_2206_input.txt', 'r') as file:
	lines = []
	for line in file:
		lines.append(line)

n = int(lines[0])
data = [float(i) for i in lines[1].split()]
# print(data)
n_q = int(lines[2])

q= []
for i in range(3, 3 + n_q):
	q.append([int(k) for k in lines[i].split()])\

def make_ln_sums(data):
	ln_sums=[0]
	for number in data:
		next_number = ln_sums[-1] + math.log(number)
		ln_sums.append(next_number)
	# del ln_sums[0]
	return ln_sums

# print(make_ln_sums(data))
def calc(ln_sums,querry):
	return math.exp((ln_sums[querry[1]+1] - ln_sums[querry[0]])/(querry[1] - querry[0] + 1))

# ln_sums = make_ln_sums(data)

# print(calc(ln_sums,[0,0]))
def print_output(data,q):
	ln_sums = make_ln_sums(data)
	for querry in q:
		result = calc(ln_sums,querry)
		print(round(result,6))

print_output(data, q)

