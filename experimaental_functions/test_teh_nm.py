#!/usr/bin/python
# -*- coding=utf-8 -*-
from ar_ctype import *
import sys,re,string
import sys, getopt, os
def treat_root(root):
	return re.sub('[\[\]\ \"]',"",root)
wazn_init=(
u"تَفاعَلَ",
#"تَفَاعَلَ",
u"تَفَعَّلَ",
u"تَفَعْلَلَ",
u"تَفَاعّ",
#u"تَفَاعَى",
u"تَفَعَّ",
#u"تَفَعَّى",
u"تَفَعَّا",
#"تَفَعْلَى",
)
wazn=[];
for w in wazn_init :
	w=re.sub(u"[فعل]",".",w);
# إغفال الحركات ما عدا الشدة
	w=re.sub(u"[%s%s%s%s]"%(FATHA,DAMMA,KASRA,SUKUN),"",w);
	print w.encode("utf8");
	wazn.append(w);
def teh_zaida(verb):
	if not verb.startswith(TEH):return False;
# التاء الزائدة
#	global wazn;
	verb=re.sub(u"[%s%s%s%s%s]"%(FATHA,DAMMA,KASRA,SUKUN,TATWEEL),"",verb);
	verb=re.sub(u"[%s]"%(ALEF_MADDA),"%s%s"%(HAMZA,ALEF),verb);
	verb=TEH+re.sub("[^%s%s]"%(SHADDA,ALEF),".",verb[1:]);
#	verb=re.sub("^[^%s%s%s]"%(TEH,SHADDA,ALEF),".",verb);
#	print verb.encode("utf8");
#	print wazn;
	if verb in wazn:
			 return True;
	else: return False;
def teh_zaida_root(verb,root):
	if not verb.startswith(TEH):return False;
# التاء الزائدة
	verb=ar_strip_marks(verb);
	if (verb.startswith(u"%s%s"%(TEH,TEH)) and root[0]==TEH)or (verb.startswith(TEH) and root[0]!=TEH):
			 return True;
	else: return False;
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
	while line :
		if not line.startswith("#"):
#		print "line ", line 
			text=text+" "+chomp(line)
			liste=line.split("\t\t");
			if len(liste)>=nb_field:
				verb_table.append(liste);
#		print " ****",text
		line=fl.readline().decode("utf");
#	print verb_table;
#	sys.exit();
#	tehteh=u"";
	count_teh=0;
	for tuple_verb in verb_table:
		word=tuple_verb[0];
		root=tuple_verb[1];
		root=treat_root(root);
		vtype=tuple_verb[2];
#		if root.startswith(u"تت"):
#			tehteh+=u" "+root;
		withoutroot= teh_zaida(word)
		withroot=teh_zaida_root(word,root)
		if   withroot and  not withoutroot:
			print "':'".join([word,root, vtype]).encode("utf8");
			count_teh+=1;
	print count_teh;

#	print "-------------------";
#	print tehteh.encode("utf8");
if __name__ == "__main__":
  main()







