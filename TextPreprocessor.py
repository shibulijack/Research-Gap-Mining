#!/usr/bin/python

import nltk
import string
import re

import Chunker
import PorterStemmer
import SWRemover

def preprocessText(str):
	td = {};
	ts = '';
	t1 = Chunker.chunk(str);
	t2 = SWRemover.removeStopWords(t1);
	for i in range(len(t2)):
		if len(t2[i].split()) == 1:				#Checks for NP Chunks
			t2[i] = re.sub("[0-9]","",t2[i]);
			p = PorterStemmer.PorterStemmer();
			t2[i] = p.stem(t2[i],0,len(t2[i])-1);
		else:		
			if td.has_key(t2[i]) == False:
				td[t2[i]] = 1;
				for j in range(i+1,len(t2)):
					if t2[i] == t2[j]:
						td[t2[i]] += 1;
			t3 = t2[i].split();
			t4 = SWRemover.removeStopWords(t3);
			t4 = filter(None, t4);
			if td[t2[i]] != 1:					#Removes stop words in chunks - Chunk Precision
				if len(t3) != len(t4):
					for k in range(len(t4)):
						ts += t4[k];
						t2[i] = ts;
						ts = '';
			else:								#A chunk is considered valid only if it occurs more than once in a doc, otherwise it is split and stemmed
				t2.remove(t2[i]);
				for k in range(len(t4)):
					t4[k] = p.stem(t4[k],0,len(t4[k])-1);
				t2 = t2 + t4;
	t2 = filter(None, t2);				#Removes empty strings
	for i in range(len(t2)):
		t2[i] = t2[i].replace(' ','');
	return t2;