#!/usr/bin/python
# -*- coding=utf-8 -*-
from ar_ctype import *
import sys,re,string
import sys, getopt, os
def treat_root(root):
	return re.sub('[\[\]\ \"]',"",root)
wazn_init=(
u"أَفْعَلَ",
u"أفال",
u"أفعا",
u"أفعى",
u"أَفَعّ",
)
wazn=[];
for w in wazn_init :
	w=re.sub(u"[فعل]",".",w);
	w=re.sub(u"[%s]"%ALEF_HAMZA_ABOVE,HAMZA,w);
# إغفال الحركات ما عدا الشدة
	w=re.sub(u"[%s%s%s%s]"%(FATHA,DAMMA,KASRA,SUKUN),"",w);
	print w.encode("utf8");
	wazn.append(w);

def unify_hamza(verb):
	verb=re.sub(u"[%s]"%(ALEF_MADDA),"%s%s"%(HAMZA,ALEF),verb);
	return re.sub(u"[%s]"%(HAMZAT),"%s"%HAMZA,verb);


def hamza_zaida(verb):
#	return False;
	verb=unify_hamza(verb);
	if not verb.startswith(HAMZA):return False;
# الهمزة الزائدة
	verb=re.sub(u"[%s%s%s%s%s]"%(FATHA,DAMMA,KASRA,SUKUN,TATWEEL),"",verb);
	verb=HAMZA+re.sub("[^%s%s]"%(SHADDA,ALEF),".",verb[1:]);
	if verb in wazn:
			 return True;
	else: return False;



def hamza_zaida_root(verb,root):
	verb=unify_hamza(verb);
	root=unify_hamza(root);
	if not verb.startswith(HAMZA):return False;
# الهمزة الزائدة
	verb=ar_strip_marks(verb);
	if (verb.startswith(u"%s%s"%(HAMZA,HAMZA)) and root[0]==HAMZA)or (verb.startswith(HAMZA) and root[0]!=HAMZA):
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
		withoutroot= hamza_zaida(word)
		withroot=hamza_zaida_root(word,root)
	
		if   not withroot and  withoutroot:
			print "':'".join([word,root, vtype]).encode("utf8");
			count_teh+=1;
	print count_teh;

#	print "-------------------";
#	print tehteh.encode("utf8");
if __name__ == "__main__":
  main()







