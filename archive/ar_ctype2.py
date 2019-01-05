#!/usr/bin/python
# -*- coding=utf-8 -*-

import re, string,sys
from arabic_const import *
from verb_const import *

#!/usr/bin/python
# -*- coding=utf-8 -*-
#---
from ar_ctype import *
#tab_pronoun=(u"أنا" ,u"أنت" ,u"أنتِ" ,u"هو" ,u"هي" ,u"أنتما" ,u"أنتما -م-" ,u"هما" ,u"هما -م-" ,u"نحن" ,u"أنتم" ,u"أنتن" ,u"هم" ,u"هن");
PronounsTable=(u"أنا" ,u"أنت" ,u"أنتِ" ,u"هو" ,u"هي" ,u"أنتما" ,u"أنتما -م-" ,u"هما" ,u"هما -م-" ,u"نحن" ,u"أنتم" ,u"أنتن" ,u"هم" ,u"هن");
ImperativePronouns=(u"أنت" ,u"أنتِ" ,u"أنتما" ,u"أنتما -م-" ,u"أنتم" ,u"أنتن" );
# const for Tense Name
TensePast=u"الماضي المعلوم";
TensePassivePast=u"الماضي المجهول";
TenseFuture=u"المضارع المعلوم"
TensePassiveFuture=u"المضارع المجهول"
TenseImperative=u"الأمر"
TableTense=[TensePast,TensePassivePast,TenseFuture, TensePassiveFuture, TenseImperative];
past={}
past[u"أنا"]=[u"",u"ْتُ"];
past[u"أنت"]=[u"",u"ْتَ"];
past[u"أنتِ"]=[u"",u"ْتِ"];
past[u"هو"]=[u"",u"َ"];
past[u"هي"]=[u"",u"َتْ"];
past[u"أنتما"]=[u"",u"ْتُما"];
past[u"أنتما -م-"]=[u"",u"ْتُما"];
past[u"هما"]=[u"",u"َا"];
past[u"هما -م-"]=[u"",u"َتَا"];
past[u"نحن"]=[u"",u"ْنَا"];
past[u"أنتم"]=[u"",u"ْتُم"];
past[u"أنتن"]=[u"",u"ْتُنَّ"];
past[u"هم"]=[u"",u"ُوا"];
past[u"هن"]=[u"",u"ْنَ"];
future={}
future[u"أنا"]=[u"أ",u"ُ"];
future[u"أنت"]=[u"ت",u"ُ"];
future[u"أنتِ"]=[u"ت",u"ِينَ"];
future[u"أنتم"]=[u"ت",u"ُونَ"];
future[u"أنتما"]=[u"ت",u"َان"];
future[u"أنتما -م-"]=[u"ت",u"َان"];
future[u"أنتن"]=[u"ت",u"ْنَ"];
future[u"نحن"]=[u"ن",u"ُ"];
future[u"هم"]=[u"ي",u"ُونَ"];
future[u"هما"]=[u"ي",u"َانِ"];
future[u"هما -م-"]=[u"ت", u"َانِ"];
future[u"هن"]=[u"ي",u"ْنَ"];
future[u"هو"]=[u"ي",u"ُ"];
future[u"هي"]=[u"ت",u"ُ"];
future_majzoom={}
future_majzoom[u"أنا"]=[u"أ",u"ْ"];
future_majzoom[u"أنت"]=[u"ت",u"ْ"];
future_majzoom[u"أنتِ"]=[u"ت",u"ِي"];
future_majzoom[u"أنتم"]=[u"ت",u"ُوا"];
future_majzoom[u"أنتما"]=[u"ت",u"َا"];
future_majzoom[u"أنتما -م-"]=[u"ت",u"َا"];
future_majzoom[u"أنتن"]=[u"ت",u"ْنَ"];
future_majzoom[u"نحن"]=[u"ن",u"ْ"];
future_majzoom[u"هم"]=[u"ي",u"ُوا"];
future_majzoom[u"هما"]=[u"ي",u"َا"];
future_majzoom[u"هما -م-"]=[u"ت", u"َا"];
future_majzoom[u"هن"]=[u"ي",u"ْنَ"];
future_majzoom[u"هو"]=[u"ي",u"ْ"];
future_majzoom[u"هي"]=[u"ت",u"ْ"];
future_mansoub={}
future_mansoub[u"أنا"]=[u"أ",u"َ"];
future_mansoub[u"أنت"]=[u"ت",u"َ"];
future_mansoub[u"أنتِ"]=[u"ت",u"ِي"];
future_mansoub[u"أنتم"]=[u"ت",u"ُوا"];
future_mansoub[u"أنتما"]=[u"ت",u"َا"];
future_mansoub[u"أنتما -م-"]=[u"ت",u"َا"];
future_mansoub[u"أنتن"]=[u"ت",u"ْنَ"];
future_mansoub[u"نحن"]=[u"ن",u"َ"];
future_mansoub[u"هم"]=[u"ي",u"ُوا"];
future_mansoub[u"هما"]=[u"ي",u"َا"];
future_mansoub[u"هما -م-"]=[u"ت", u"َا"];
future_mansoub[u"هن"]=[u"ي",u"ْنَ"];
future_mansoub[u"هو"]=[u"ي",u"َ"];
future_mansoub[u"هي"]=[u"ت",u"َ"];
imperative={}
imperative[u"أنت"]=[u"",u"ْ"];
imperative[u"أنتِ"]=[u"",u"ِي"];
imperative[u"أنتم"]=[u"",u"ُوا"];
imperative[u"أنتما"]=[u"",u"َا"];
imperative[u"أنتما -م-"]=[u"",u"َا"];
imperative[u"أنتن"]=[u"",u"ْنَ"];
TableTenseProunoun={}
TableTenseProunoun[TensePast]=past;
TableTenseProunoun[TensePassivePast]=past;
TableTenseProunoun[TenseFuture]=future;
TableTenseProunoun[TensePassiveFuture]=future;
TableTenseProunoun[TenseImperative]=imperative;

tab_sarf={};
#باب تصريف الفعل، الصفر لكل الأفعال عدا الثلاثي
tab_sarf[0]={"past":FATHA,"future":KASRA}
# فَعَل يَفْعُل

tab_sarf[1]={"past":FATHA,"future":DAMMA}
# فَعَل يَفْعِل
tab_sarf[2]={"past":FATHA,"future":KASRA}
# فَعَل يَفْعَل
tab_sarf[3]={"past":FATHA,"future":FATHA}
# فَعِل يَفْعَل
tab_sarf[4]={"past":KASRA,"future":FATHA}
# فَعِل يَفْعِل
tab_sarf[5]={"past":KASRA,"future":KASRA}
# فَعُل يَفْعُل
tab_sarf[6]={"past":DAMMA,"future":DAMMA}

HARAKAT=u"%s%s%s%s%s"%(SUKUN,FATHA,DAMMA,KASRA,SHADDA);
HARAKAT2=u"%s%s%s%s%s%s%s"%(ALEF,WAW,YEH,SUKUN,FATHA,DAMMA,KASRA);
HAMZAT=u"%s%s%s%s%s"%(ALEF_HAMZA_ABOVE, WAW_HAMZA, YEH_HAMZA , HAMZA, ALEF_HAMZA_BELOW);
BEGIN_WORD=u"^";
END_WORD=u"$";


NOT_DEF_HARAKA=TATWEEL;
STRIP_HARAKA=u"i";
ALEF_HARAKA=ALEF;
ALEF4_HARAKA=u"y";
ALEF_YEH_HARAKA=u"#";
ALEF_WAW_HARAKA=u"*";
YEH_HARAKA=YEH;
WAW_HARAKA=WAW;
LONG_HARAKAT=(ALEF_HARAKA,YEH_HARAKA,WAW_HARAKA,ALEF_YEH_HARAKA,ALEF_WAW_HARAKA);
_F=FATHA;
_D=DAMMA;
_K=KASRA;
_S=SUKUN;
_A=ALEF;
_W=WAW;
_Y=YEH

_AH=ALEF_HARAKA;
_YH=YEH_HARAKA
_WH=WAW_HARAKA
_AYH=ALEF_YEH_HARAKA
_AWH=ALEF_WAW_HARAKA
tab_change_haraka={};
tab_change_haraka[_S]={_S:_S,_F:_F,_D:_D,_K:_K,_AH:_AH,_WH:_WH,_YH:_YH}
tab_change_haraka[_F]={_S:_S,_F:_F,_D:_D,_K:_K,_AH:_AH,_WH:_WH,_YH:_YH}
tab_change_haraka[_D]={_S:_S,_F:_F,_D:_D,_K:_K,_AH:_AH,_WH:_WH,_YH:_YH}
tab_change_haraka[_K]={_S:_S,_F:_F,_D:_D,_K:_K,_AH:_AH,_WH:_WH,_YH:_YH}
tab_change_haraka[_AH]={_S:_F,_F:_AH,_D:_WH,_K:_YH,_AH:u"",_YH:u"",_WH:u"",_YH:u""}
tab_change_haraka[_WH]={_S:_D,_F:_AH,_D:_WH,_K:_YH,_AH:u"",_WH:u"",_YH:u""}
tab_change_haraka[_YH]={_S:_K,_F:_AH,_D:_WH,_K:_YH,_AH:u"",_WH:u"",_YH:u""}
tab_change_haraka[_AWH]={_S: (u"%s%s"%(_F,_S),_W),_F:(u"%s%s"%(_F,_F),_W),_D:_WH,_K:_YH,_AH:(u"%s%s"%(_F,_AH),_W),_WH:_WH,_YH:_YH}
tab_change_haraka[_AYH]={_S:(u"%s%s"%(_F,_S),_Y),_F:(u"%s%s"%(_F,_F),_Y),_D:_YH,_K:_YH,_AH:(u"%s%s"%(_F,_AH),_Y),_WH:_WH,_YH:_YH}
#HAMZAT
_AHA=ALEF_HAMZA_ABOVE
_AHB=ALEF_HAMZA_BELOW
_AM=ALEF_MADDA;
_YHA=YEH_HAMZA
_WHA=WAW_HAMZA
_HZ=HAMZA

tab_tahmeez_initial={_S:_HZ,_F:_AHA,_D:_AHA, _K:_AHB,_AH:_AM ,_WH:_AHA, _YH:_AHB};


tab_tahmeez_middle={};
tab_tahmeez_middle[_S]={_S:_HZ,_F:_AHA,_D:_WHA, _K:_YHA,_AH:_AHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_middle[_F]={_S:_AHA,_F:_AHA,_D:_WHA, _K:_YHA,_AH:_AHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_middle[_D]={_S:_WHA,_F:_WHA,_D:_WHA, _K:_YHA,_AH:_WHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_middle[_K]={_S:_YHA,_F:_YHA,_D:_YHA, _K:_YHA,_AH:_YHA,_WH:_YHA, _YH:_YHA };
tab_tahmeez_middle[_AH]={_S:_HZ,_F:_HZ,_D:_WHA, _K:_YHA,_AH:_AHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_middle[_WH]={_S:_WHA,_F:_WHA,_D:_WHA, _K:_YHA,_AH:_HZ,_WH:_WHA, _YH:_YHA };
tab_tahmeez_middle[_YH]={_S:_YHA,_F:_YHA,_D:_YHA, _K:_YHA,_AH:_YHA,_WH:_YHA, _YH:_YHA };


tab_tahmeez_final={};
tab_tahmeez_final[u"%s"%BEGIN_WORD]={_S:_HZ,_F:_AHA,_D:_AHA, _K:_AHB,_AH:_AM ,_WH:_AHA, _YH:_AHA};
tab_tahmeez_final[_S]={_S:_HZ,_F:_AHA,_D:_WHA, _K:_YHA,_AH:_AHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_final[_F]={_S:_AHA,_F:_AHA,_D:_AHA, _K:_AHB,_AH:_AHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_final[_D]={_S:_WHA,_F:_WHA,_D:_WHA, _K:_YHA,_AH:_WHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_final[_K]={_S:_YHA,_F:_YHA,_D:_YHA, _K:_YHA,_AH:_WHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_final[_AH]={_S:_HZ,_F:_HZ,_D:_HZ, _K:_HZ,_AH:_HZ,_WH:_WHA, _YH:_YHA };
tab_tahmeez_final[_WH]={_S:_HZ,_F:_HZ,_D:_HZ, _K:_HZ,_AH:_WHA,_WH:_WHA, _YH:_YHA};
tab_tahmeez_final[_YH]={_S:_HZ,_F:_HZ,_D:_HZ, _K:_HZ,_AH:_WHA,_WH:_WHA, _YH:_YHA};

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
	HAMZAT= u"إأءئؤ";
	i=0;
	while i in range(len(word)):
		if word[i] in HAMZAT:
			word=replace_pos(word,HAMZA,i);
		elif word[i]==SHADDA:
			word=replace_pos(word,SUKUN+word[i-1],i)
		elif word[i]==ALEF_MADDA:
			word=word.replace(ALEF_MADDA,HAMZA+FATHA+ALEF);
		i+=1;
	return word;
#--------------------------------------
def uniformate_alef_origin(marks,future_type=KASRA):
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
	return marks;	
		
#--------------------------------------
def uniformate2(word):
	""" separate the harakat and the letters of the given word, it return two strings ( the word without harakat and the harakat).
    If the weaked letters are reprsented as long harakat and striped from the word.
    """
	HARAKAT=(FATHA,DAMMA,KASRA,SUKUN);
	shakl=u"";
	word_nm=u""
	i=0;
	while i <len(word):
		if word[i] not in HARAKAT:
			word_nm+=word[i];
			if i+1 < len(word) and word[i+1] in HARAKAT:
				if word[i+1]==FATHA :
					if i+2<len(word) and word[i+2]==ALEF and i+3<len(word) :
						shakl+=ALEF_HARAKA;
#						shakl+=ALEF;
						i+=3;
					elif  i+2<len(word) and word[i+2]==ALEF_MAKSURA :
#						shakl+=ALEF_HARAKA;
#						i+=3
						shakl+=FATHA+FATHA;
						word_nm+=YEH;
						i+=3;
					elif  i+2<len(word) and word[i+2]==ALEF and i+3>=len(word) :
#						shakl+=ALEF_HARAKA;
#						i+=3
						shakl+=FATHA+FATHA;
						word_nm+=WAW;
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
					shakl+=YEH_HARAKA;
					i+=3;
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
                new_word+=word_nm[i]+SHADDA;
## عندما يكون الحرف السابق ساكنا فإنه يستعيعيض عن حركته بحركة الحرف الأول
                if i-1>=0 and new_harakat[i-1]==SUKUN:
                    if harakat[i]!=SUKUN:
                        new_harakat=new_harakat[:-1]+harakat[i]+NOT_DEF_HARAKA+harakat[i+1];
                    else:
                        new_harakat=new_harakat[:-1]+FATHA+NOT_DEF_HARAKA+harakat[i+1];
                        
##                    new_harakat=new_harakat[:-1]+"*"+NOT_DEF_HARAKA+harakat[i+1];
                else:
                    new_harakat+=NOT_DEF_HARAKA+harakat[i+1];
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

    word_nm,harakat=geminating(word_nm,harakat);
    if len(word_nm)!=len(harakat):
        return u"";
    else:
        word=u"";
        i=0;
## حالة عدم الابتداء بسكون
##إذا كان الحرف الثاني مضموما  تكون الحركة الأولى مضمومة، وإلا تكون مكسورة
        if len(harakat)!=0 and harakat[0]==SUKUN:
            word_nm=ALEF+word_nm
            if len(harakat)>2 and harakat[1]==DAMMA:
                harakat=DAMMA+harakat
            else:
                harakat=KASRA+harakat
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
	word=word.replace( u"%s%s%s"%(ALEF_HAMZA_ABOVE,FATHA,ALEF),ALEF_MADDA);
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
	                	print (u"Middle : word %s in letter %s between '%s' and '%s'"%(word_nm,word_nm[i],before,actual)).encode("utf8");
	                	swap=word_nm[i];
                    else :
                    	if before in tab_tahmeez_final.keys() and actual in tab_tahmeez_final[before].keys() :
                        	swap= tab_tahmeez_final[before][actual];
	                else :
	                	print (u"Final :word %s in letter %s between '%s' and '%s'"%(word_nm,word_nm[i],before,actual)).encode("utf8");
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
      		elif i==0 : new_harakat+=KASRA;
      		else:new_harakat+=FATHA;
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
            else :
                new_harakat+=harakat[i];
    return new_harakat;


