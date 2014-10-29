import nltk
import sys
import sets 

if len(sys.argv) < 2:
	print "usage: python ner.py filename" 

with open(sys.argv[1], "r") as myfile:
    doc = myfile.read()   
tokens = nltk.word_tokenize(doc)
tagged = nltk.pos_tag(tokens)
parsed = nltk.ne_chunk(tagged)
for chunk in parsed:
    if hasattr(chunk, "leaves") and hasattr(chunk, "label"):
        print "%s, %s" % (chunk.label().rstrip(), chunk.leaves()[0][0])
