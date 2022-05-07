import datetime

with open('j.txt') as file:
	lines=file.readlines()

n = int(lines[0].split()[0])
L = int(lines[0].split()[1])
R = int(lines[0].split()[2])

data = []
for line in lines[1:]:
	d = line.split('-')
	d = d[::-1]
	d = list(map(int,d))
	data.append(d)

datum = []
for dat in data:
	year = dat[0]
	month = dat[1]
	day = dat[2]
	datum.append(datetime.date(year,month,day))

datum.sort()
max_length = 1
max_new = 1
for i in range(1,len(datum)):
	delta = datum[i] - datum[i-1]
	if delta == datetime.timedelta(days=1):
		max_new+=1
		if max_new > max_length:
			max_length = max_new
	else:
		max_new = 1

print(max_length)