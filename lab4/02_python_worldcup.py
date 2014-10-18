import re

with open('worldcup.txt', 'rt') as f:
	data = f.read()
	country, rank, year = "", -1, 0
	for lines in data.split('-'):
		for line in lines.split('\n'):
			#print line, ";"
			#if re.match(r'sup', line):
			if line.find("fb|") != -1:
				segs = re.split(r'[\|}]', line)
				country = segs[2]
				if country == "{{fb": country = segs[3] 
				rank = 0
			else:
				if rank != -1: rank = rank + 1
				if (rank < 5 and rank > 0):
					segs = re.split(r'[\|}]', line)
					for seg in line.split("]]"):
						if seg.find("World Cup") != -1:
							year = seg[-4:]
							print "%s, %s, %s" % (country,year,rank)