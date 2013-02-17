#!/usr/bin/python

import os
import math
import string
import json

import tfCalculator

def main():
	dict = {};
	idf = {};
	st = "";
	ntdocs = 1.0;
	docs = os.listdir('papers');
	ndocs = len(docs);
	n = 0
	
	for i in range(ndocs):
		n = n + 1
		print docs[i]
		print n
		f = 'papers' + '/' + docs[i];
		statinfo = os.stat(f);
		if statinfo.st_size <= 152576:
			fp = open(f,"r");
			st = fp.read();
			dict = tfCalculator.findtf(st);
		s = docs[i].strip('.txt');
		s = 'pre/' + s + '.json'
		f = open(s,"w");
		f.write(json.dumps(dict));
		f.close();
		dict = {};
		fp.close();
		
if __name__ == "__main__":
	main();
		