#!/usr/bin/python

import os
import string

def main():
	
	""" Read the cluster output
	get the document IDs """
	
	fp = open ("assets/input/sample_cluster.txt","r")
	con = fp.read()
	clusters=con.split('\n')
	#print clusters;
	first=clusters[0]
	docs=first.split('\t')
	docs.pop(0)
	docs=[item.rstrip('tx.') for item in docs]
	#print docs
	fp.close()
	
	""" Get the cited papers' IDs
	for each of the documents """
	
	final={}
	citations=[]
	cit_fp=open("assets/input/citation.txt","r")
	for searchterms in docs:
		for line in cit_fp.readlines():
			n=line.find(searchterms)
			if n==0:
				t=line.partition('==>')
				citations.append(t[2])
		citations=[item.strip() for item in citations]
		#print citations
		final[searchterms]=citations
	cit_fp.close()
	print final

if __name__=="__main__":
	main()
