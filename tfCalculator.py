#!/usr/bin/python

import nltk
import string
import os

import TextPreprocessor

def findtf(str):
	dict = {};
	tl1 = TextPreprocessor.preprocessText(str);
	for i in range(len(tl1)):						#Hash - Dictionary: (term,frequency) pairs
		if(dict.has_key(tl1[i])):
			dict[tl1[i]] = dict[tl1[i]] + 1;
		else:
			dict[tl1[i]] = 1;
	return dict;