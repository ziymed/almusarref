#!/usr/bin/python
# -*- coding=utf-8 -*-
from verb_const import *
from ar_ctype import *
##word=u"شددت";
##harakat=u"ََُْ"
##word=u"ظنن";
##harakat=u"ُْْ"
##w,h= geminating(word,harakat);
##print " word",len(w),w
##print " harakat",len(h),h
##new_harakat="123456"
##print new_harakat[:-1]

##l,h=geminating(l,h)
##print l,h;
##print len(h);
##print standard2(l,h)
##word=u"لاءم"
##print len(word)
##word=uniformate(word);
##print word
##print len(word)
##i=0;
####word=SAD+KASRA+FATHA+FATHA+TEH+FATHA+FATHA+LAM+KAF+ALEF_MAKSURA+DAMMA
##word=WAW+KASRA+FATHA+FATHA+TEH+FATHA+FATHA+LAM+KAF+ALEF_MAKSURA+DAMMA+TEH
##valid=is_valid_word(word);
##print valid
## ignore harakat at the began of the word
##while word[i] in HARAKAT:
##    i+=1;
##word=word[i:]
##print word,len(word);
##word=u"نَمَّى"
####valid=is_valid_word(word);
####print valid
##print word[-1:]
##word=DAL+FATHA+AIN+FATHA+ALEF
##future_type=DAMMA;
##root=DAL+AIN+WAW
##l,h=uniformate2(word);
####تُمْشَيِينَ
##print l,h;
##print len(h);
##verb=word;
##verb=verb;
##internal_verb=uniformate(verb);
##print (u" الكتابة الداخلية للفعل 1"+internal_verb).encode("utf8");
#### الوظيفة Uniformate لا تحذف الألفات، وتستعمل لحسابحساب الطول الفعلي للفعل
##future_type=future_type;
##(word_letters,word_marks)=uniformate2(verb,"verb");
##print (u" الكتابة الداخلية للفعل 1"+word_letters+" - "+word_marks).encode("utf8");
##
####word_marks=uniformate_alef_origin(word_marks,internal_verb,future_type);
####print (u" الكتابة الداخلية للفعل "+word_letters+" - "+word_marks).encode("utf8");
##root=root;
##future_type=DAMMA;
##conj_l=HAMZA+DHAD+DHAD;
##conj_m=FATHA+DAMMA;
##conj_m=treat_sukun2(conj_l,conj_m,future_type);
####		conj_l=tahmeez2(conj_l,conj_m);
####		conj_l,conj_m=homogenize(conj_l,conj_m);
##		conj=standard2(conj_l,conj_m);
tab=(
u"آجَرَ",
u"آنَسَ",
u"آدَ",
u"آضَّ",
u"آخَى",
u"آوَى",
u"آتَى",
u"آسَ",
u"آمَنَ")
for d in tab:
    print d,":", uniformate(d);
