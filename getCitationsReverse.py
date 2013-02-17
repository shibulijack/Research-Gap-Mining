#!/usr/bin/python

import os
import string
import json

def main():
	
	""" Read the cluster output
	get the document IDs """
	
	docs=[]
	fp = open ("assets/input/papers_list.txt","r")
	con = fp.read()
	docs=con.split('\n')
	docs.pop(-1)
	docs=[item.rstrip('tx.') for item in docs]
	print docs
	fp.close()
	
	""" Get the cited papers' IDs
	for each of the documents """
	
	final={}
	citations=[]
	cit_fp=open("assets/input/citation.txt","r")
	for searchterms in docs:
		for line in cit_fp.readlines():
			n=line.find(searchterms)
			if n>0:
				t=line.partition('==>')
				citations.append(t[0])
		citations=[item.strip() for item in citations]
		print citations
		final[searchterms]=citations
	cit_fp.close()
	fp_out=open("citnw_lt.json","w")
	fp_out.write(json.dumps(final))
	print final

if __name__=="__main__":
	main()
