#!/usr/bin/python

import os
import string
import json

def main():
	id_list=[]
	title_list=[]
	year_list=[]
	cit_fp=open("assets/input/metadata.txt","r")
	for line in cit_fp.readlines():
		i=line.find("id")
		t=line.find("title")
		y=line.find("year")
		if i==0:
			tu=line.partition('=')
			id_list.append(tu[2])
		elif t==0:
			tu=line.partition('=')
			title_list.append(tu[2])
		elif y==0:
			tu=line.partition('=')
			year_list.append(tu[2])
	cit_fp.close()
	ids=[item.strip() for item in id_list]
	titles=[item.strip() for item in title_list]
	years=[item.strip() for item in year_list]

	#Strip the unwanted { }
	final_id=[]
	for it in ids:
		st=it
		st=st.strip('}{')
		final_id.append(st)
	final_title=[]
	for it in titles:
		st=it
		st=st.strip('}{')
		final_title.append(st)
	final_year=[]
	for it in years:
		st=it
		st=st.strip('}{')
		final_year.append(st)
	
	#Create a dictionary with the extracted metadata
	chronological_detail={}
	l=len(final_id)
	i=0
	while(i<l):
		tu=()
		tu=final_title[i],final_year[i]
		chronological_detail[final_id[i]]=tu
		i+=1
	f_out=open("assets/output/meta.json","w")
	f_out.write(json.dumps(chronological_detail))
	#print chronological_detail
	
if __name__=="__main__":
	main()
