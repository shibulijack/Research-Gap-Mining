#!/usr/bin/python

import nltk
import string
import os
import re
from nltk.stem.lancaster import LancasterStemmer

import Chunker
import SWRemover

def preprocessText(str):
	t3 = [];
	L = [];
	td = {};
	t5 = [];

	t1 = Chunker.chunk(str);
	st = LancasterStemmer();
	t2 = SWRemover.removeStopWords(t1);
	for i in range(len(t2)):
		t2[i] = re.sub("[0-9]","",t2[i]);
	t2 = filter(None, t2);
	for i in range(len(t2)):
		t = t2[i].split();
		if len(t) == 1:
			L.append(st.stem(t2[i]));
		else:
			t3.append(t2[i]);
	for i in range(len(t3)):
		if td.has_key(t3[i]) == False:
			td[t3[i]] = 1;
			for j in range(i+1,len(t3)):
				if t3[i] == t3[j]:
					td[t3[i]] += 1;
	t4 = td.keys();
	for i in range(len(t4)):
		if(td[t4[i]] > 1):
			for k in range(td[t4[i]]):
				L.append(t4[i]);
		else:
			t = t4[i].split();
			t5 = t + t5;
	t5 = SWRemover.removeStopWords(t5);
	for i in range(len(t5)):
		t5[i] = st.stem(t5[i]);
	L = L + t5;
	for i in range(len(L)):
		L[i] = L[i].replace(' ','');
	return L;