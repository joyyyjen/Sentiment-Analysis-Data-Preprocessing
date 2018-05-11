#!/usr/local/bin/python3

from string import punctuation
import os 
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def procss_doc(directory):
	for fileid in os.listdir(directory):
		if not fileid.endswith(".txt"):
			continue
		print(fileid)
		fpath = os.path.join(directory,fileid)
		with open(fpath,'r') as f:
			text = f.read()
			f.close()
		tokens = word_tokenize(text)
		stop_words = set(stopwords.words('english'))
		tokens = [w for w in tokens if not w in stop_words]
		table = str.maketrans('', '', punctuation)
		tokens = [w.translate(table).strip() for w in tokens]
		line = ' '.join(tokens)
		with open(fpath,'w') as f2:
			f2.write(line)
			f2.close()
if __name__ == "__main__":
	procss_doc('txt_sentoken/neg')
	procss_doc('txt_sentoken/pos')
