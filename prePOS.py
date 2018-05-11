#!/usr/local/bin/python3
import os
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from string import punctuation

def procss_doc(directory,directory2):
	for fileid in os.listdir(directory):
		if not fileid.endswith(".txt"):
			continue
		print(fileid)
		fpath = os.path.join(directory,fileid)
		with open(fpath,'r') as f:
			text = f.read()
			f.close()
		table = str.maketrans('', '', punctuation)
		text = text.translate(table)
		tokens = word_tokenize(text)
		tagged_corpus = pos_tag(tokens)
		sentences = []
		for i, sent in enumerate(tagged_corpus):
			line = "".join(sent[0]+ "_" + sent[1])
			sentences.append(line)
		sentences= " ".join(sentences)
		path2 = os.path.join(directory2,fileid)
		with open(path2,'w') as f2:
			f2.write(sentences)
			f2.close()


if __name__ == "__main__":
	procss_doc('txt_sentoken/neg','txt_sentoken2/neg')
	procss_doc('txt_sentoken/pos','txt_sentoken2/pos')