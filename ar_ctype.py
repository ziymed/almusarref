#!/usr/bin/python
# -*- coding=utf-8 -*-

import re, string,sys
from arabic_const import *
from verb_const import *

#!/usr/bin/python
# -*- coding=utf-8 -*-
#---

#--------------------------------------
def replace_pos (word,rep, pos):
	return word[0:pos]+rep+word[pos+1:];
#--------------------------------------
def chomp(s):
  if (s.endswith('\n')):
    return s[:-1]
  else:
    return s
HARAKAT_pat =re.compile(ur"^[%s%s%s%s%s%s%s%s]$"%(FATHATAN,DAMMATAN,KASRATAN,FATHA,DAMMA,KASRA,SUKUN,SHADDA) )
HARAKAT_NO_SHADDA_pat =re.compile(ur"^[%s%s%s%s%s%s%s]$"%(FATHATAN,DAMMATAN,KASRATAN,FATHA,DAMMA,KASRA,SUKUN) )
#--------------------------------------
def ar_isvowel(w):
	" return True if the letter is an arabic vowel. SHADDA is  a vowel."
	res=HARAKAT_pat.match(w);
	if res:return True;
	else: return False;

# return True if the letter is a tatweel.
#--------------------------------------
def ar_istatweel(w):
	"return True if the letter is a tatweel."
	if w==TATWEEL :  return True;
	else :return False;

#--------------------------------------
def ar_strip_vowel(w):
	"strip vowel from a word and return a result word"
	return HARAKAT_pat .sub('', w)


#strip tatweel from a word and return a result word
#--------------------------------------
def ar_strip_tatweel(w):
	"strip tatweel from a word and return a result word"
	return re.sub(ur'[%s]' % TATWEEL,	'', w)
#strip tatweel and vowel from a word and return a result word but keep shadda
#--------------------------------------
def ar_strip_marks_keepshadda(w):
	return re.sub(ur'[%s%s%s%s%s%s%s%s]' % (FATHATAN, DAMMATAN, TATWEEL,
                                            KASRATAN, FATHA, DAMMA, KASRA, SUKUN),	'', w)


#strip tatweel and vowel from a word and return a result word
#--------------------------------------
def ar_strip_marks(w):
	"strip tatweel and vowel from a word and return a result word"
	return re.sub(ur'[%s%s%s%s%s%s%s%s%s]' % (FATHATAN, DAMMATAN, TATWEEL,
                                            KASRATAN, FATHA, DAMMA, KASRA, SUKUN,SHADDA),	'', w)


#strip tatweel and vowel from a word and return a result word
#--------------------------------------
def ar_strip_punct(w):
    return re.sub(r'[%s%s%s%s\\]' % (string.punctuation, string.digits,
                                     string.ascii_letters, string.whitespace),
                  ' ', s)
# return True if the given word have the same or the partial vocalisation like the pattern
#------------------------------------------------
def vocalizedlike( vocalized,word):
	vocalized=re.sub(u"[%s]"%FATHA,u"[%s]?"%FATHA,vocalized)
	vocalized=re.sub(u"[%s]"%KASRA,u"[%s]?"%KASRA,vocalized)
	vocalized=re.sub(u"[%s]"%DAMMA,u"[%s]?"%DAMMA,vocalized)
	vocalized=re.sub(u"[%s]"%SUKUN,u"[%s]?"%SUKUN,vocalized)
	vocalized=re.sub(u"[%s]"%SHADDA,u"[%s]?"%SHADDA,vocalized)
	vocalized="^"+vocalized+"$";
	pat=re.compile(vocalized);
	res=pat.match(word);
	if res : return True;
	else : return False;
# this function is to replace all letters non vowel to an unique symbole, to be used for test vowlization
#--------------------------------------
def replace_letters(word0):
	return re.sub(ur'[^%s%s%s%s%s%s%s%s]' % (FATHATAN, DAMMATAN, KASRATAN, FATHA, DAMMA, KASRA,
                                            SUKUN,SHADDA),	u'-', word0)
# للمقارنة بين كلمتين متساويتين في الطول إذا كانتا متشاكلتان: أي يتطابق تشكيلهما جزئيا أو كليا.
# لا يهم إن كانتا غير متساويتين في الحروف
# if verify_vowel_only is True: verify only the vowels
#else verify letters too,
#--------------------------------------
def equal_shakl(word0,wazn0,verify_vowel_only=False):
	if not verify_vowel_only :
		word=ar_strip_marks(word0);
		wazn=ar_strip_marks(wazn0);
		if word!=wazn : return False;
	else :
		if len(ar_strip_marks(word0))!=len(ar_strip_marks(wazn0)):
			return False;
		word=replace_letters(word0);
		wazn=replace_letters(wazn0);
	# j :word index
#	print 1;
	j=0;
	i=0;
	while i< len(wazn) and j<len(word):
#		print 2;
		wazn_i_isvowel=ar_isvowel(wazn[i]);
		word_j_isvowel=ar_isvowel(word[j]);
		if (wazn_i_isvowel) and (word_j_isvowel):
			if wazn[i]!=word[j]:
#				print 3;
				return False;
			else: j+=1;
		elif (wazn_i_isvowel) and (not word_j_isvowel):
#			print 4;
			pass;
		elif (not wazn_i_isvowel) and ( word_j_isvowel):
#			print 5;
			while (ar_isvowel(word[j])) :  j+=1;
			if  (wazn[i]!=word[j]): return False;
			else : j+=1;
		elif  (not wazn_i_isvowel) and (not word_j_isvowel):
			if wazn[i]!=word[j]:
#				print 7;
				return False;
			else: j+=1;
		i+=1;
		#strip last vowel
	while ( j<len(word) and ar_isvowel(word[j]) ):  j+=1;
	if(j<len(word)): return False;
	return True;
#--------------------------------------
#
#
#
#---------------------------------------
def is_valid_word(word):
# This function return True, if the word is valid, else, return False
# A word is not valid if :
# - minimal lenght : 3
# - starts with :
#    ALEF_MAKSURA, WAW_HAMZA,YEH_HAMZA,
#    HARAKAT
# - contains : TEH_MARBUTA
# - contains  ALEF_MAKSURA at the began or middle.
# - contains : double haraka : a warning
# - contains : ALEF
# - contains: tanween
	if len(word)<3: return False;
	elif word[0]in (WAW_HAMZA,YEH_HAMZA,FATHA,DAMMA,SUKUN,KASRA):
         print (word+" error began with un valid letter").encode("utf8");
         return False;
	elif word.find(TEH_MARBUTA)>0:
         print (word+ " error contains TEH_MARBUTA").encode("utf8");
         return False;
	elif word.find(FATHATAN)>0:
         print (word+ " error contains FATHATAN").encode("utf8");
         return False;
	elif word.find(DAMMATAN)>0:
         print (word+ " error contains DAMMATAN").encode("utf8");
         return False;
	elif word.find(KASRATAN)>0:
         print (word+ " error contains KASRATAN").encode("utf8");
         return False;
	else:
	   word_nm=ar_strip_marks(word);
	   if word_nm[:-1].find(ALEF_MAKSURA)>0:
	       print (word+" error contains invalid ALEF_MAKSURA").encode("utf8");
	       return False;
	return True;

# تحويل الكلمة إلى شكلها النظري.
# الشكل اللإملائي للكلمة هو طريقة كتابتها حسب قواعد الإملاء
# الشكل النظري هو الشكل المتخيل للكلمة دون تطبيق قواعد اللغة
# ويخص عادة الأشكال المتعددة للهمزة، و التي تكتب همزة على السطر
# أمثلة
# إملائي		نظري
#إِمْلَائِي		ءِمْلَاءِي
#سَاَلَ		سَءَلَ
# الهدف : تحويل الكلمة إلى شكل نظري، ومن ثم إمكانية تصريفها بعيدا عن قواعد الإملاء،
#وبعد التصريف يتم تطبيق قواعد الإملاء من جديد.
#الفرضية: الكلمات المدخلة مشكولة شكلا تاما.
#الطريقة:
# 1-تحويل جميع أنواع الهمزات إلى همزة على السطر
# 1-فك الإدغام
#--------------------------------------
#--------------------------------------

def uniformate(word):
##standardize the Hamzat into one form of hamza
## replace shadda by double letters
## replace Madda by hamza and alef.
## replace the LamAlefs by simplified letters.

	HAMZAT= u"إأءئؤ";
	i=0;

## تستبدل الألف الممدودة في ,ل الكلمة بهمزة قطع بعدها همزة أخرى
	if word.startswith(ALEF_MADDA):
## مشكلة في تحويل ألف المدة الأولى، فهي تنقلب إما إلى همزة بعدها أللف في مثل فاعل،
## وذلك في حال الفعل المضعف مهموز الأول
## أو همزتين متتاليتين على وزن أفعل
	   if len(word)>=3 and (word[1] not in HARAKAT) and (word[2]==SHADDA or len(word)==3):
            word=HAMZA+FATHA+ALEF+word[1:];
	   else:
            word=HAMZA+FATHA+HAMZA+SUKUN+word[1:];
## ignore harakat at the began of the word
	while word[i] in HARAKAT:
	   i+=1;
	word=word[i:]

	while i in range(len(word)):
## حالة غياب الفتحة قبل الألف
		if word[i] not in(SUKUN,FATHA,KASRA,DAMMA,ALEF) and i+1<len(word) and word[i+1]==ALEF:
		  word=replace_pos(word,word[i]+FATHA,i);
		if word[i] in HAMZAT:
			word=replace_pos(word,HAMZA,i);
		elif word[i]==SHADDA:
			word=replace_pos(word,SUKUN+word[i-1],i)
##  تستبدل المدة في وسط الكلمة بهمزة مفتوحة وألف
##أما في أول الكلمة فتستبدل بهمزة على اللف وهمزة ساكنة
##		elif word[i] ==ALEF :
#### ignore harakat after Alef
##		  while i+1<len(word) and word[i+1]in HARAKAT:
##		      word=replace_pos(word,"",i+1);
##		elif word[i] in (ALEF,ALEF_MAKSURA,SUKUN,DAMMA,KASRA,FATHA) :
#### ignore double haraka and Alef
##		  while i+1<len(word) and word[i+1]in HARAKAT:
##		      word=replace_pos(word,"",i+1);
		elif word[i]==ALEF_MADDA:
			word=word.replace(ALEF_MADDA,HAMZA+FATHA+ALEF);
		elif word[i]==LAM_ALEF:
			word=word.replace(LAM_ALEF,simple_LAM_ALEF);
		elif word[i]==LAM_ALEF_HAMZA_ABOVE:
			word=word.replace(LAM_ALEF_HAMZA_ABOVE,simple_LAM_ALEF_HAMZA_ABOVE);
		elif word[i]==LAM_ALEF_HAMZA_BELOW:
			word=word.replace(LAM_ALEF_HAMZA_BELOW,simple_LAM_ALEF_HAMZA_BELOW);
		elif word[i]==LAM_ALEF_MADDA_ABOVE:
			word=word.replace(LAM_ALEF_MADDA_ABOVE,simple_LAM_ALEF_MADDA_ABOVE);
		i+=1;
##	word=word.replace( u"%s%s"%(LAM,ALEF),LAM+FATHA+ALEF);
	return word;
#--------------------------------------
def uniformate_alef_origin(marks,word_nm,future_type=KASRA):
	if len(marks)!=2:return marks;
# الحرف الأخير علة
	if marks[-1:]==ALEF_HARAKA:
		if future_type==KASRA:
			marks=marks[:-1]+ALEF_YEH_HARAKA;
		elif future_type==DAMMA:
			marks=marks[:-1]+ALEF_WAW_HARAKA;
# الحرف ماقبل الأخير علة
	elif   marks[len(marks)-2]==ALEF_HARAKA:
		if future_type==KASRA:
			marks=marks[:-2]+ALEF_YEH_HARAKA+marks[-1:]
		elif future_type==DAMMA:
			marks=marks[:-2]+ALEF_WAW_HARAKA+marks[-1:]
# الحرف الأخير علة
	if len(word_nm)==3 and word_nm[-1:]==ALEF:
	    word_nm=word_nm[:-1]+WAW
	elif len(word_nm)>3 and word_nm[-1:]==ALEF:
	    word_nm=word_nm[:-1]+YEH
	elif word_nm[-1:]==ALEF_MAKSURA:
	    word_nm=word_nm[:-1]+YEH
	return marks;

###--------------------------------------
##def uniformate_last_alef(word_nm):
### الحرف الأخير علة
##	if len(word_nm)==3 and word_nm[-1:]==ALEF:
##	    word_nm=word_nm[:-1]+WAW
##	elif len(word_nm)>3 and word_nm[-1:]==ALEF:
##	    word_nm=word_nm[:-1]+YEH
##	elif word_nm[-1:]==ALEF_MAKSURA:
##	    word_nm=word_nm[:-1]+YEH
##
##	return word_nm;

#--------------------------------------
def uniformate2(word,type="affix"):
	""" separate the harakat and the letters of the given word, it return two strings ( the word without harakat and the harakat).
    If the weaked letters are reprsented as long harakat and striped from the word.
    """
    ## type : affix : uniformate affixes
    ## type: verb uniformate verb, then treat last alef
	word=uniformate(word);
	HARAKAT=(FATHA,DAMMA,KASRA,SUKUN);
	shakl=u"";
	word_nm=u""
	i=0;
#	print "len word",len(word);
	while i <len(word):
		if word[i] not in HARAKAT:
			word_nm+=word[i];
			if i+1 < len(word) and word[i+1] in HARAKAT:
				if word[i+1]==FATHA :
					if i+2<len(word) and word[i+2]==ALEF and i+3<len(word) :
						shakl+=ALEF_HARAKA;
#						shakl+=ALEF;
						i+=3;
					elif type=="verb" and  i+2<len(word) and word[i+2]==ALEF_MAKSURA :
#						shakl+=ALEF_HARAKA;
#						i+=3
						shakl+=FATHA+FATHA;
						word_nm+=YEH;
						i+=3;
##معالجة حرف العلة في أخر الكلمةفي الفعل الناقص
##غذا كان الألف في آحر الفغعل الثلاثي يعوض بواو
##في الفعل غير الثلاثي يصبح ياء
					elif type=="verb" and len(word_nm)==2 and i+2<len(word) and word[i+2]==ALEF and i+3>=len(word) :
#						shakl+=ALEF_HARAKA;
#						i+=3
##						print "len word_nm1 ",len(word_nm);
						shakl+=FATHA+FATHA;
##  حالة الفعل عيا، أعيا، عيّا والتي يتحول إلى ياء بدلا عن واو
						if word_nm[1]==YEH:
						  word_nm+=YEH;
						else :
						  word_nm+=WAW;
#						print "len word_nm ",len(word_nm)
						i+=3;
					elif type=="verb" and  len(word_nm)>=3 and i+2<len(word) and word[i+2]==ALEF and i+3>=len(word) :
#						shakl+=ALEF_HARAKA;
#						i+=3
##						print "len word_nm44 ",len(word_nm);
						shakl+=FATHA+FATHA;
						word_nm+=YEH;
						i+=3;
					else :
						shakl+=FATHA;
						i+=2;
				elif word[i+1]==DAMMA and i+2<len(word) and word[i+2]==WAW:
					if i+3>=len(word) or word[i+3] not in HARAKAT:
						shakl+=WAW_HARAKA;
						i+=3;
					else :
						shakl+=DAMMA;
						i+=2;
				elif word[i+1]==KASRA and i+2<len(word) and word[i+2]==YEH:
					if i+3>=len(word) or word[i+3] not in HARAKAT:
						shakl+=YEH_HARAKA;
						i+=3;
					else :
						shakl+=KASRA;
						i+=2;
##					shakl+=YEH_HARAKA;
##					i+=3;
				else :
					shakl+=word[i+1];
					i+=2;
##معالجة حالات الشدة، فك الإدغام
			elif i+1 < len(word) and word[i+1] ==SHADDA:
				shakl+=SUKUN;
				word_nm+=word[i];
				if i+2 < len(word) and word[i+2] in HARAKAT :
##					shakl+=word[i+2];
##					i+=3;
					if i+3<len(word) and word[i+2]==FATHA and word[i+3]==ALEF:
					    shakl+=ALEF_HARAKA;
					    i+=4;
					elif i+3<len(word) and word[i+2]==DAMMA and word[i+3]==WAW:
					    shakl+=WAW_HARAKA
					    i+=4;
					elif i+3<len(word) and word[i+2]==KASRA and word[i+3]==YEH:
					    shakl+=YEH_HARAKA
					    i+=4;
					else:
					   shakl+=word[i+2];
					   i+=3;
				else :
					shakl+=NOT_DEF_HARAKA;
					i+=2;
			elif  i+1 < len(word) and word[i+1] in HARAKAT :
				shakl+=word[i+1];
			else:
				shakl+=NOT_DEF_HARAKA;
				i+=1;
		else: i+=1;
	if len(word_nm)==len(shakl):
		return (word_nm,shakl)
	else: return (u"",u"");
#-----------------------------------------
#
#
#
#------------------------------------------
def standard_harakat(word):
    k=0;
    new_word=u"";
    while k<len(word):
## الحروف من دون العلة لا تؤخذ بيعين الاعتبار، كما لا تؤخذ إذا كانت في أول الكلمة
       if k==0 or word[k] not in (ALEF,YEH,WAW,ALEF_MAKSURA):
            new_word+=word[k];
       else:
##إذا كان الحرف علة ولم يكن في أول الكلمة
##إذا كان ما قبله ليس حركة، ومابعده ليس حركة، أو انتهت الكلمة
        if word[k-1] not in HARAKAT and (k+1>=len(word) or word[k+1] not in HARAKAT) :
            if word[k]==ALEF:
                new_word+=FATHA+ALEF;
            elif word[k]==WAW :
                new_word+=DAMMA+WAW;
            elif word[k]==YEH:
                new_word+=KASRA+YEH;
            else:new_word+=word[k];
        else:new_word+=word[k];
       k+=1;
    return new_word;
#--------------------------------------
def geminating(word_nm,harakat):
    """ treat geminating cases
    """
##    SUKUN_HARAKATE=(SUKUN,ALEF_HARAKA,YEH_HARAKA,WAW_HARAKA);
##    return word_nm,harakat;
    new_word=u"";
    new_harakat=u"";
    i=0;
    while i <len(word_nm):
# للإدغام يجب أن يكون الحرف الحالي مساويا للحرف التالي،
# كما يجب أن تكون حركة الحرف الحالي سكونا أو حركة قصيرة
        if i>0 and i+1<len(word_nm) and word_nm[i]==word_nm[i+1] and harakat[i] in (SUKUN,FATHA,KASRA,DAMMA):
            # treat geminating case
            if  harakat[i]!=SUKUN and harakat[i+1]==SUKUN:
                #no geminating
##the counter is incremented by one step only, to treat other possible geminating with the second letter
##                new_word+=word_nm[i]+word_nm[i+1];
##                new_harakat+=harakat[i]+harakat[i+1];
                new_word+=word_nm[i];
                new_harakat+=harakat[i];
                i+=1;
            elif  harakat[i]==SUKUN and harakat[i+1]==SUKUN:
                #no geminating
##                new_word+=word_nm[i]+word_nm[i+1];
##                new_harakat+=FATHA+harakat[i+1];
                new_word+=word_nm[i];
                new_harakat+=FATHA;
                i+=1;
            else:

## عندما يكون الحرف السابق ساكنا فإنه يستعيعيض عن حركته بحركة الحرف الأول
                if i-1>=0 and new_harakat[i-1]==SUKUN:
                    new_word+=word_nm[i]+SHADDA;
                    if harakat[i]!=SUKUN:
                        new_harakat=new_harakat[:-1]+harakat[i]+NOT_DEF_HARAKA+harakat[i+1];
                    else:
                        new_harakat=new_harakat[:-1]+FATHA+NOT_DEF_HARAKA+harakat[i+1];
##                    new_harakat=new_harakat[:-1]+"*"+NOT_DEF_HARAKA+harakat[i+1];
## يتم الإدغام إذا كان الحرف السابق ذا حركة طويلة
                elif i-1>=0 and new_harakat[i-1]in (ALEF_HARAKA,WAW_HARAKA,YEH_HARAKA):
                    new_word+=word_nm[i]+SHADDA;
                    new_harakat+=NOT_DEF_HARAKA+harakat[i+1];
                elif harakat[i]==SUKUN:
                    new_word+=word_nm[i]+SHADDA;
                    new_harakat+=NOT_DEF_HARAKA+harakat[i+1];
                else:
## مؤقت حتى يتم حل المشكلة
                    new_word+=word_nm[i]+SHADDA;
                    new_harakat+=NOT_DEF_HARAKA+harakat[i+1];
##TODO
## منع الإدغام في بعض الحالات التي لا يمكن فيها الإدغام
##مثل حالة سكتتا ، أي الحرفات متحركان وما قبلهاما متحرك
                    #no geminating
##                    new_word+=word_nm[i]+word_nm[i+1];
##                    new_harakat+=harakat[i]+harakat[i+1];
                i+=2;
        else :
            new_word+=word_nm[i];
            new_harakat+=harakat[i];
            i+=1;
    return (new_word,new_harakat);

#--------------------------------------
def standard2(word_nm,harakat):
    """ join the harakat and the letters to the give word in the standard script,
    it return one strings ( the word with harakat and the harakat).
    """
    if len(word_nm)!=len(harakat):
        return u"";
    else:
        word=u"";
        i=0;
        word_nm,harakat=geminating(word_nm,harakat);
        if len(word_nm)!=len(harakat):
            return u"";
## حالة عدم الابتداء بسكون
##إذا كان الحرف الثاني مضموما  تكون الحركة الأولى مضمومة، وإلا تكون مكسورة
        if len(harakat)!=0 and harakat[0]==SUKUN:
            word_nm=ALEF+word_nm
            if len(harakat)>=2 and harakat[1]in (DAMMA, WAW_HARAKA):
                harakat=DAMMA+harakat
            else:
                harakat=KASRA+harakat

        word_nm=tahmeez2(word_nm,harakat);
        if len(word_nm)!=len(harakat):
            return u"";
        word_nm,harakat=homogenize(word_nm,harakat);
        if len(word_nm)!=len(harakat):
            return u"";


#### حالة عدم الابتداء بسكون
####إذا كان الحرف الثاني مضموما  تكون الحركة الأولى مضمومة، وإلا تكون مكسورة
##        if len(harakat)!=0 and harakat[0]==SUKUN:
####            if word_nm.startswith(ALEF_HAMZA_ABOVE):
####                word_nm=ALEF+word_nm
####            else: word_nm=ALEF+word_nm;
##
##            if len(harakat)>=2 and harakat[1]in (DAMMA, WAW_HARAKA):
##                harakat=DAMMA+harakat
#### معالجة حالة البدء بساكن لا سيما إن كان همزة على الألف
##                if word_nm.startswith(ALEF_HAMZA_ABOVE):
##                    word_nm=ALEF+WAW_HAMZA+word_nm[1:]
##                else: word_nm=ALEF+word_nm;
##            else:
##                harakat=KASRA+harakat
##                if word_nm.startswith(ALEF_HAMZA_ABOVE):
##                    word_nm=ALEF+YEH_HAMZA+word_nm[1:]
##                else: word_nm=ALEF+word_nm;
        while i <len(word_nm):
            if harakat[i]==ALEF_HARAKA:
                word+=word_nm[i]+FATHA+ALEF;
                i+=1;
            elif harakat[i]==ALEF_WAW_HARAKA:
                word+=word_nm[i]+FATHA+ALEF;
                i+=1;
            elif harakat[i]==ALEF_YEH_HARAKA :
                if i+1<len(word_nm):
                	word+=word_nm[i]+FATHA+ALEF;
                else :
                	word+=word_nm[i]+FATHA+ALEF_MAKSURA;
##                	word+=word_nm[i]+FATHA+"*";
                i+=1;
            elif harakat[i]==WAW_HARAKA:
                word+=word_nm[i]+DAMMA+WAW;
                i+=1;
            elif harakat[i]==YEH_HARAKA:
                word+=word_nm[i]+KASRA+YEH;
                i+=1;
            elif harakat[i]==ALTERNATIVE_YEH_HARAKA:
                word+=word_nm[i]+KASRA+YEH;
                i+=1;
            elif harakat[i]==NOT_DEF_HARAKA:
                word+=word_nm[i];
                i+=1;

            else:
                word+=word_nm[i]+harakat[i];
                i+=1;
        if word.endswith(FATHA+YEH+FATHA):
        	word=word[:-2]+ALEF_MAKSURA;
        elif word.endswith(FATHA+WAW+FATHA):
        	word=word[:-2]+ALEF;
##-	تحويل همزة القطع على الألف بعدها فتحة وهمزة القطع على الألف بعدها سكون إلى ألف ممدودة

	word=word.replace( u"%s%s%s"%(ALEF_HAMZA_ABOVE,FATHA,ALEF),ALEF_MADDA);
	word=word.replace( u"%s%s"%(ALEF_MADDA,FATHA),ALEF_MADDA);
	word=word.replace( u"%s%s"%(ALEF_MADDA,ALEF),ALEF_MADDA);
	word=word.replace( u"%s%s%s%s"%(ALEF_HAMZA_ABOVE,FATHA,ALEF_HAMZA_ABOVE,SUKUN),ALEF_MADDA);
	word=word.replace( u"%s%s%s%s"%(ALEF_HAMZA_ABOVE,FATHA,ALEF_HAMZA_ABOVE,FATHA),ALEF_MADDA);
	word=word.replace( u"%s%s%s%s"%(ALEF,KASRA,HAMZA,SUKUN),ALEF+KASRA+YEH_HAMZA+SUKUN);
	word=word.replace( u"%s%s%s%s"%(ALEF,DAMMA,HAMZA,SUKUN),ALEF+DAMMA+WAW_HAMZA+SUKUN);
	word=word.replace( u"%s%s%s%s"%(ALEF_HAMZA_ABOVE,DAMMA,WAW_HAMZA,SUKUN),ALEF_HAMZA_ABOVE+DAMMA+WAW);
	word=word.replace( u"%s%s%s%s"%(WAW_HAMZA,SUKUN,YEH_HAMZA,KASRA),YEH_HAMZA+SHADDA+KASRA);
	word=word.replace( u"%s%s%s%s"%(WAW_HAMZA,SUKUN,ALEF_HAMZA_ABOVE,FATHA),ALEF_HAMZA_ABOVE+SHADDA+FATHA);
	word=word.replace( u"%s%s%s%s"%(ALEF_HAMZA_ABOVE,SUKUN,YEH_HAMZA,KASRA),YEH_HAMZA+SHADDA+KASRA);

##  معالجة ألف التفريق
	word=word.replace( ALEF_WASLA,ALEF);
##  معالجة ألف  الوصل الزائدة عند إضافتها إلى أول الفعل المثال
	word=word.replace( u"%s%s%s%s"%(ALEF,DAMMA,YEH,SUKUN),ALEF+DAMMA+WAW);


	return word;
	# إعلال و إبدال الهمزة.
#--------------------------------------
def tahmeez2(word_nm,harakat):
    """ Transform hamza on the standard script. in entry the word without harakat and the harakat seperately
    return the word with non uniform hamza

    """
    if len(word_nm)!=len(harakat):
        return u"";
    else:
    	ha2=u"";
    	#eliminate some altenative of HARAKAT to standard.
    	for h in harakat:
		if h==NOT_DEF_HARAKA: h=FATHA;
		elif h==ALEF_YEH_HARAKA or h==ALEF_WAW_HARAKA:
			h=ALEF_HARAKA;
		ha2+=h;
	harakat=ha2;
        word=u"";
       	HAMZAT= u"إأءئؤ";
        for i in range(len(word_nm)):
            if word_nm[i] !=HAMZA and word_nm[i] !=ALEF_HAMZA_ABOVE:
                 word+=word_nm[i];
            else:
                if i==0:
                    actual=harakat[i];
                    swap= tab_tahmeez_initial[actual];
                else:
                    before=harakat[i-1];
                    actual=harakat[i];
                    if i+1<len(word_nm):
                   	if before in tab_tahmeez_middle.keys() and actual in tab_tahmeez_middle[before].keys() :
	                        swap= tab_tahmeez_middle[before][actual];
	                else :
##	                	print (u"Middle : word %s in letter %s between '%s' and '%s'"%(word_nm,word_nm[i],before,actual)).encode("utf8");
	                	swap=word_nm[i];
                    else :
                    	if before in tab_tahmeez_final.keys() and actual in tab_tahmeez_final[before].keys() :
                        	swap= tab_tahmeez_final[before][actual];
	                else :
##	                	print (u"Final :word %s in letter %s between '%s' and '%s'"%(word_nm,word_nm[i],before,actual)).encode("utf8");
	                	swap=word_nm[i];
            	word+=swap;
	return word;

#--------------------------------------
def treat_sukun2(word_nm,harakat,swaped_haraka=KASRA):
    """ Treat the rencontre of sukun. in entry the word without harakat and the harakat seperately, and the probably haraka
    return the new sequence of harakat

    """
    if len(word_nm)!=len(harakat):
        return harakat;
    else:
        new_harakat=u"";
        for i in range(len(word_nm)):
            if harakat[i]==ALEF_HARAKA and i+1<len(harakat) and harakat[i+1]==SUKUN:
#  other conditions
# إذا كان حرف الألف ثانيا مثل خاف يقلب كسرة،أما إذا كان ثالثا أو رابعا فيصبح فتحة، مثل خاف لا تخف
		if i+2<len(word_nm) and word_nm[i+1]==word_nm[i+2]:
			new_harakat+=ALEF_HARAKA;
      		elif i==0 :
      		    new_harakat+=KASRA;
      		else:
      		    new_harakat+=FATHA;
            elif harakat[i]==ALEF_YEH_HARAKA and i+1<len(harakat) and harakat[i+1]==SUKUN:
#  other conditions
      		    new_harakat+=KASRA;
            elif harakat[i]==ALEF_WAW_HARAKA and i+1<len(harakat) and harakat[i+1]==SUKUN:
#  other conditions
      		    new_harakat+=DAMMA;
            elif harakat[i]==WAW_HARAKA and i+1<len(harakat) and harakat[i+1]==SUKUN:
                #  other conditions
                new_harakat+=DAMMA;
            elif harakat[i]==YEH_HARAKA and i+1<len(harakat) and harakat[i+1]==SUKUN:
                #  other conditions
                new_harakat+=KASRA;
            elif harakat[i]==ALTERNATIVE_YEH_HARAKA and i+1<len(harakat) and harakat[i+1]==SUKUN:
                #  other conditions
                new_harakat+=DAMMA;
            else :
                new_harakat+=harakat[i];
    return new_harakat;

#--------------------------------------
def homogenize(word_nm,harakat):
    """ treat the jonctionof WAW, YEH
    """
    if len(word_nm)!=len(harakat):
        return (word_nm, harakat);
    else:
        new_harakat=u"";
        new_word=u"";
        i=0;
## دراسة حالات الياء والواو قبل النهاية
        while i<len(word_nm)-1:
            if word_nm[i]==YEH:
                if  (harakat[i]in(SUKUN,KASRA,YEH_HARAKA)) and i-1>=0 and harakat[i-1]==KASRA:
                    new_harakat=new_harakat[:-1]+YEH_HARAKA
##تحويل الياء إلى واو ساكنة
                elif (harakat[i] in (DAMMA, WAW_HARAKA))and i-1>=0 and harakat[i-1]==FATHA:
                    new_harakat+=SUKUN
                    new_word+=WAW;

                elif  (harakat[i] in(SUKUN)) and i-1>=0 and harakat[i-1]==DAMMA and (i+1<len(word_nm) and word_nm[i+1]!=YEH):
                    new_harakat=new_harakat[:-1]+WAW_HARAKA

                elif (harakat[i] in (YEH_HARAKA))and i-1>=0 and harakat[i-1]==FATHA:
                    new_harakat+=SUKUN
                    new_word+=YEH;
                elif  (harakat[i] in(WAW_HARAKA)) and i-1>=0 and harakat[i-1]==KASRA:
                    new_harakat=new_harakat[:-1]+WAW_HARAKA

                else :
                    new_harakat+=harakat[i];
                    new_word+=word_nm[i];
            elif word_nm[i]==WAW:
                if (harakat[i] in(SUKUN,DAMMA,WAW_HARAKA))and i-1>=0 and harakat[i-1]==DAMMA:
                    new_harakat=new_harakat[:-1]+WAW_HARAKA
##تحويل الواو المضمومة  أو الطويلة إلى واو ساكنة
                elif (harakat[i] in (DAMMA, WAW_HARAKA))and i-1>=0 and harakat[i-1]==FATHA:
                    new_harakat+=SUKUN
                    new_word+=word_nm[i];
                else :
                    new_harakat+=harakat[i];
                    new_word+=word_nm[i];
            else:
                new_harakat+=harakat[i];
                new_word+=word_nm[i];
            i+=1;
## دراسة حالة الحرف الأخير
##        new_harakat+=harakat[i];
##        new_word+=word_nm[i];
        if word_nm[i]==YEH:
            if  (harakat[i] in(KASRA,YEH_HARAKA,DAMMA)) and i-1>=0 and harakat[i-1]==KASRA:
                new_harakat=new_harakat[:-1]+YEH_HARAKA
            elif (harakat[i]==SUKUN):
                pass;
            elif  (harakat[i] in(KASRA,DAMMA,FATHA)) and i-1>=0 and harakat[i-1]==FATHA:
                new_harakat+=NOT_DEF_HARAKA
                new_word+=ALEF_MAKSURA;
            elif  (harakat[i] in(WAW_HARAKA)) and i-1>=0 and harakat[i-1]==KASRA:
                new_harakat=new_harakat[:-1]+WAW_HARAKA
            else :
                new_harakat+=harakat[i];
                new_word+=word_nm[i];
        elif word_nm[i]==WAW:
            if (harakat[i] in(DAMMA,WAW_HARAKA,KASRA))and i-1>=0 and harakat[i-1]==DAMMA:
                new_harakat=new_harakat[:-1]+WAW_HARAKA
            elif (harakat[i] in(ALEF_HARAKA))and i-1>=0 and harakat[i-1]==DAMMA:
##                pass;
                new_harakat=new_harakat[:-1]+YEH_HARAKA
            elif (harakat[i]==SUKUN):
                pass;
##                new_harakat=new_harakat[:-1]+WAW_HARAKA
            else :
                new_harakat+=harakat[i];
                new_word+=word_nm[i];
        else:
            new_harakat+=harakat[i];
            new_word+=word_nm[i];
        return (new_word, new_harakat);




