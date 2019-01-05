#!/usr/bin/python
# -*- coding=utf-8 -*-
from verb_const import *
from ar_ctype import *
from classverb import *
import sys,re,string
import sys, getopt, os
scriptname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
scriptversion = '0.1'
AuthorName="Taha Zerrouki"
def usage():
# "Display usage options"
	print "(C) CopyLeft 2007, %s"%AuthorName
	print "Usage: %s -f filename [OPTIONS]" % scriptname
#"Display usage options"
	print "\t[-h | --help]\t\toutputs this usage message"
	print "\t[-V | --version]\tprogram version"
	print "\t[-f | --file= filename]\tinput file to %s"%scriptname
	print "\t[-a | --all ]\t\tConjugate in all tenses"
	print "\t[-i | --imperative]\tConjugate in imperative"
	print "\t[-F | --future]\t\tconjugate in the present and the future"
	print "\t[-p | --past]\t\tconjugate in the past"
	print "\t[-v | --passive]\tpassive form";
	print "\r\nThis program is licensed under the GPL License\n"

def grabargs():
#  "Grab command-line arguments"
	all = False;
	future=False;
	past=False;
	passive=False;
	imperative=False;
	fname = ''

	if not sys.argv[1:]:
		usage()
		sys.exit(0)
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hVvnaiFpi:f:",
                               ["help", "version","imperative", "passive", "past","all",
                                "future",  "file="],)
	except getopt.GetoptError:
		usage()
		sys.exit(0)
	for o, val in opts:    
		if o in ("-h", "--help"):
			usage()
			sys.exit(0)
		if o in ("-V", "--version"):
			print scriptversion
			sys.exit(0)
		if o in ("-v", "--passive"):
			passive = True
		if o in ("-f", "--file"):
			fname = val
		if o in ("-F", "--future"):
			future = True
		if o in ("-a", "--all"):
			all=True;
		if o in ("-p", "--past"):
			past =True;
		if o in ("-i","-imperative"):
			imperative=True;			
	return (fname,all,future,past,passive,imperative)

def main():  
	filename,all,future,past,passive,imperative= grabargs()
	try:
		fl=open(filename);
	except: 
		print " Error :No such file or directory: %s" % filename 
		sys.exit(0)
	line=fl.readline().decode("utf");
	text=u""
	verb_table=[];
	nb_field=2;
	while line :
		if not line.startswith("#"):
#		print "line ", line 
			text=text+" "+chomp(line)
			liste=line.split("\t");
			if len(liste)>=nb_field:
				verb_table.append(liste);
#		print " ****",text
		line=fl.readline().decode("utf");
#	print verb_table;
#	sys.exit();
	for tuple_verb in verb_table:
		word=tuple_verb[0];
		root=tuple_verb[1];
		future_type=tuple_verb[2];
		if future_type==u"فتحة":future_type=FATHA;
		elif future_type==u"ضمة":future_type=DAMMA;
		elif future_type==u"كسرة":future_type=KASRA;				
		elif future_type==u"سكون":future_type=SUKUN;
		else:future_type=u"فتحة";
		transitive=False;
		if tuple_verb[3]==u"متعدي":	transitive=True;
		bab_sarf=0;
		if len(tuple_verb)>=5 :
				try:bs=int(tuple_verb[4]);
				except:bs=0;
				if bs!=0:	bab_sarf=bs;
		vb=verbclass(word,root,transitive,future_type,bab_sarf);
		vb.verb_class();
# test the uniformate function		
		if all : vb.conjugate_all_tenses();
		else :
			listetenses=[];
			if past : listetenses.append(TensePast);
			if (past and passive) : listetenses.append(TensePassivePast)
			if future : listetenses.append(TenseFuture);
			if (future and passive) : listetenses.append(TensePassiveFuture)
			if imperative : listetenses.append(TenseImperative)
			vb.conjugate_all_tenses(listetenses);


if __name__ == "__main__":
  main()







