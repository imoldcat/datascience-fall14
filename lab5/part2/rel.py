import nltk
import re
import sys

def find_per_org(pred_pattern):
	print "finding for pattern: ", pred_pattern
	IN = re.compile(r'.*\b%s\b'%pred_pattern)
	for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    		for rel in nltk.sem.extract_rels('PERSON', 'ORGANIZATION', doc, corpus='ieer', pattern = IN):
        		print(nltk.sem.rtuple(rel))
	print

if len(sys.argv) < 2:
	find_per_org("executive\ at")
	find_per_org("worked")
	find_per_org("[a-zA-Z]*")
else:
	find_per_org(sys.argv[1])
