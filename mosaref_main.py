from verb_const import *
from ar_ctype import *
from classverb import *
import sys,re,string
import sys, getopt, os

def do_sarf(word,root,future_type,all=True,past=False,future=False,passive=False,transitive=False):
	valid=is_valid_word(word)
	if valid:
		if future_type==u"فتحة":future_type=FATHA;
		elif future_type==u"ضمة":future_type=DAMMA;
		elif future_type==u"كسرة":future_type=KASRA;
		elif future_type==u"سكون":future_type=SUKUN;
		else:future_type=u"فتحة";
		transitive=False;
		if transitive==u"متعدي":	transitive=True;
		bab_sarf=0;
		vb=verbclass(word,root,transitive,future_type,bab_sarf);
		vb.verb_class();
	#test the uniformate function
		if all : return vb.conjugate_all_tenses();
		else :
			listetenses=[];
			if past : listetenses.append(TensePast);
			if (past and passive and transitive) : listetenses.append(TensePassivePast)
			if future : listetenses.append(TenseFuture);
			if (future and passive ) : listetenses.append(TensePassiveFuture)
			if (future and passive and transitive) : listetenses.append(TensePassiveFuture)
			if imperative : listetenses.append(TenseImperative)
			return vb.conjugate_all_tenses(listetenses);
			
			

#do_sarf("قال".decode("utf"),"قول".decode("utf"),"ضمة".decode("utf"))
	
