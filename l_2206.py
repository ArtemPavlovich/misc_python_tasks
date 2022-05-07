with open('l_2206_input.txt') as file:
	lines = []
	for line in file:
		lines.append(line)

space = [int(k) for k in lines[0].split()[:2]]
W = space[0]
H = space[1]

size = [int(k) for k in lines[0].split()[2:]]
a = size[0]
b = size[1]

n = int(lines[1])

coords = []
for line in lines[2:]:
	line = [int(k) for k in line.split()]
	coords.append(line)

x_coords = [[i[0], i[2]] for i in coords]
y_coords = [i[j] for i in coords for j in [1,3]]
y_labels = list(map(lambda i: 'b' if i%2==0 else 'u', range(2*n)))
y_number = [i for i in range(len(coords)) for j in range(2)]

y_all = list(zip(y_coords,y_labels,y_number))
y_all = sorted(y_all, key = lambda point: point[0]) #N*log(N)


# do intervals intersect
def is_intersect(interval1, interval2):
	return not (interval1[0] >= interval2[1] or interval2[0] >= interval1[1])

# make interference list between [x,x+a] and all x_coords of rectangles
def interference(x_coords,x,a):
	interval_target = [x,x+a]
	result = set()
	for i in range(len(x_coords)):
		if is_intersect(interval_target, x_coords[i]):
			result.add(i)
	return result

# interference_list = interference_list(x_coords,2,2)
# print(interference_list)
# The main process. Start from some x. We go through the y_all. Every step we check, if the rectangle is in the interference list. If so, bot or up_counter+=1. bot_counter = 1 shows the upper border of 
# the collision free region. We write down this region. Continue to count bot and up coords. When up_counter equals bot_counter, the bottom border of the next free region begins and counters are reset.
# In the end we will have a max free region. Shift x by 1 to the right and repeat. 

def max_collision_free_region(interference_list, y_all, H):
	b_target = 0
	u_target = 0
	max_h = 0
	max_h_next = 0
	b_target_next = 0
	u_target_next = 0
	b_count = 0
	u_count = 0
	for entry in y_all:
		y, label, num = entry
		if num not in interference_list:
			continue
		
		if label == 'b':
			b_count += 1
		else:
			u_count += 1
		# print(b_count,u_count)

		if u_count == b_count:
			b_target_next = y
			continue

		if b_count == 1:
			u_target_next = y
			max_h_next = u_target_next - b_target_next
			if max_h_next > max_h:
				b_target, u_target, max_h = b_target_next, u_target_next, max_h_next
			# print(b_target,u_target,max_h)

	print(b_target_next,u_target_next)
	u_target_next = H
	max_h_next = u_target_next - b_target_next
	if max_h_next > max_h:
		b_target, u_target, max_h = b_target_next, u_target_next, max_h_next

	return [b_target, u_target], max_h

# Loop through x

collision_free_region = [[0,0],[0,0]]
max_h = 0
for x in range(W - a + 1):
	interference_list = interference(x_coords, x, a)
	# print(interference_list)
	collision_free_region_x, max_h_x = max_collision_free_region(interference_list, y_all, H)
	# print(collision_free_region_x)
	if max_h_x > max_h:
		collision_free_region = [[x,collision_free_region_x[0]],[x+a, collision_free_region_x[1]]]



# print(x_coords)
# print(y_all)
# print(interference_list)
# print(max_collision_free_region(interference_list, y_all, 8))
print(collision_free_region)
