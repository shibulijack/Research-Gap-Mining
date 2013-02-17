#!/usr/bin/python

import os
import math
import string

import tfCalculator

def main():
	#Enter the path of the directory
	ntf = tl1 = [];
	dict = idf = {};
	st = "";
	ntdocs = 1;
	docs = os.listdir("C:\\Python27\\sampleset");
	ndocs = len(docs);
	
	for i in range(ndocs):
		f = 'C:\\Python27\\sampleset\\' + docs[i];
		fp = open(f,"r");
		st = fp.read();
		dict = tfCalculator.findtf(st);
		
		#Normalising term frequency
		m = max(dict.values()) + 0.0;
		for j,v in dict.items():
			dict[j] = v/m;
		ntf.append(dict);	#ntf = [{'word':ntf}]
		fp.close();
		
		#Calculating Inverse Document Frequency idf
	for i in range(ndocs):
		tl1 = ntf[i].keys();
		for j in range(len(tl1)):
			if idf.has_key(tl1[j]) == False:
				for k in range(i+1,ndocs):
					if ntf[k].has_key(tl1[j]) == True:
						ntdocs = ntdocs + 1;
				idf[tl1[j]] = math.log10(1.0 * (ndocs / ntdocs));
				ntdocs = 1;
	
	#Input File for Bayon Clustering Tool
	fp = open("input.txt","w");
	for i in range(ndocs):
		fp.write(docs[i]);
		fp.write('\t');
		tl1 = ntf[i].keys();
		for j in range(len(tl1)):
			fp.write(tl1[j]);
			fp.write('\t');
			tfidf = ntf[i].get(tl1[j]) * idf.get(tl1[j]);
			st = str(tfidf);
			fp.write(st);
			fp.write('\t');
		fp.write('\n');
	fp.close();
		
if __name__ == "__main__":
	main();
	
	