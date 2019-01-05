#!/usr/bin/python
# -*- coding=utf-8 -*-
from ar_ctype import *
import sys,re,string
import sys, getopt, os
def treat_root(root):
	return re.sub('[\[\]\ \"]',"",root)
wazn_init=(
u"تَفاعَلَ",
u"تَفَاعَلَ",
u"تَفَعَّلَ",
u"تَفَعْلَلَ",
u"تَفَاعّ",
u"تَفَاعَى",
u"تَفَعَّ",
u"تَفَعَّى",
u"تَفَعْلَى",
)
wazn=[];
for w in wazn_init :
	w=re.sub(u"[فعل]","-",w);
	print w.encode("utf8");
	wazn.append(w);
#-------------------------------------------------------------------------------
def teh_zaida(verb):
# التاء الزائدة		
	if not verb.startswith(TEH) :return False;
#	global wazn;
	verb=TEH+re.sub("[^%s%s%s%s%s]"%(FATHA,SUKUN,SHADDA,ALEF,ALEF_MAKSURA),"-",verb[1:]);
#	print verb.encode("utf8");
#	print wazn;
	if verb in wazn:
			 return True;
	for w in wazn :
		if vocalizedlike(w,verb): return True;
	else: return False;

#-------------------------------------------------------------------------------
def teh_zaida_root(verb,root):
# التاء الزائدة
	verb=ar_strip_marks(verb);
	if (verb.startswith(u"%s%s"%(TEH,TEH)) and root[0]==TEH)or (verb.startswith(TEH) and root[0]!=TEH):
			 return True;
	else: return False;
#-------------------------------------------------------------------------------
def main():  
#	filename,all,future,past,passive,imperative= grabargs()
	try:
		fl=open("teh_verb.dict");
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
	count_withrootonly=0
	count_withoutrootonly=0
	count_both=0

	print u"عدد الأفعال ذات التاء المزيدة التي يعرفها البرنامج بواسطة جذر".encode("utf8"),len(verb_table);
	table_word_without_root=[];
	for tuple_verb in verb_table:
		word=tuple_verb[0];
		root=tuple_verb[1];
		root=treat_root(root);
		vtype=tuple_verb[2];
#		if root.startswith(u"تت"):
#			tehteh+=u" "+root;
		withoutroot= teh_zaida(word)
		withroot=teh_zaida_root(word,root)

		if  withroot and withoutroot: count_both+=1;
		if  not withroot and withoutroot:	
			count_withoutrootonly+=1
			table_word_without_root.append("':'".join([word,root, vtype]));
		if  withroot and not withoutroot:
			print "':'".join([word,root, vtype]).encode("utf8");
			count_withrootonly+=1;
	print u"عدد الأفعال ذات التاء المزيدة الإجمالي".encode("utf8"),len(verb_table);
	print u"تعرف عليها  بالوزن فقط ".encode("utf8"),count_withoutrootonly;
	print "---------------------";
	for i in table_word_without_root: print i.encode("utf8");
	print "---------------------";
	print u"تعرف عليها بالجذر فقط".encode("utf8"),count_withrootonly;
	print u"تعرف عليها بالجذر والوزن".encode("utf8"),count_both;


if __name__ == "__main__":
  main()







