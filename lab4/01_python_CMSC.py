import re

with open('cmsc.txt', 'rt') as f:
	course, section, teacher = "", "", ""
	seat, open, wait = "", "", ""
	date, time, blgd, room = "", "", "", ""
	for line in f:
		if re.match(r'^CMSC', line):
			course = line.strip()
		elif re.match(r'^[0-9]+', line):
			section = line.strip()
		elif re.match(r'^[a-zA-Z.:]+ [a-zA-Z.:]+', line):
			teacher = line.strip()
		elif re.match(r'^Seats', line):
			segs = re.split(r'[:,)]\s', line)
			seat = segs[1]
			open = segs[3]
			wait = segs[5].rstrip()
		elif re.match(r'[a-zA-Z]+ [0-9]+:[0-9]', line):
			segs = re.split(r'\s', line)
			date = segs[0]
			time = segs[1] + " - " + segs[3]
		elif re.match(r'^[A-Z]+  [0-9]+$', line):
			segs = re.split(r'[\s]+', line)
			blgd = segs[0]
			room = segs[1]
			print "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
				%(course, section, teacher, seat, open, \
				wait, date, time, blgd, room)