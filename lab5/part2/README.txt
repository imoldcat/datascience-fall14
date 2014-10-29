ner.py			the script for part 2.1
ner_output.txt		the output by running 'python ner.py news1.html', news1.html is provided in lab5 
data/Chang_wiki.txt	a extracted news article from wikipedia updates, http://en.wikipedia.org/wiki/Chang%27e_5-T1
ner_output2.txt		the output for the data/Chang_wiki.txt. other documents are similar.

rel.py			the script for part 2.2
			if run with parameter, 
			it explores three patterns for relationships between Person and Organization
				1. executive at
				2. worked
				3. any possible words between the two type of named entities
			one can also run with a pattern, python rel.py worked

rel_output.txt		the output of rel.py when matching 'executive\ at'

