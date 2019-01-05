#!/usr/bin/python
# -*- coding=utf-8 -*-
from ar_ctype import *
import sys,re,string
import sys, getopt, os
def treat_root(root):
	return re.sub('[\[\]\ \"]',"",root)

def main():  
#	filename,all,future,past,passive,imperative= grabargs()
	try:
		fl=open("ar_verb.dict");
	except: 
		print " Error :No such file or directory: %s" % filename 
		sys.exit(0)
	line=fl.readline().decode("utf");
	text=u""
	verb_table=[];
	nb_field=3;
	count_teh=0;
	while line :
		if not line.startswith("#"):
#		print "line ", line 
			text=text+" "+chomp(line)
			liste=line.split("\t\t");
			if len(liste)>=nb_field:
				verb_table.append(liste);
				word=liste[0];
				root=liste[1];
				root=treat_root(root);
				vtype=liste[2];
				thl=u"ثلا";
				if    vtype.find(thl)>-1 and (root.find(WAW)>-1 or root.find(YEH)>-1 or root.find(ALEF_MAKSURA)>-1):
					print "':'".join([word,root, vtype]).encode("utf8");
					count_teh+=1;
#		print " ****",text
		line=fl.readline().decode("utf");
	print count_teh;

#	print "-------------------";
#	print tehteh.encode("utf8");
if __name__ == "__main__":
  main()







