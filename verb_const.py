#!/usr/bin/python
# -*- coding=utf-8 -*-
#---
from arabic_const import *
#tab_pronoun=(u"أنا" ,u"أنت" ,u"أنتِ" ,u"هو" ,u"هي" ,u"أنتما" ,u"أنتما مؤ" ,u"هما" ,u"هما مؤ" ,u"نحن" ,u"أنتم" ,u"أنتن" ,u"هم" ,u"هن");
PronounsTable=(u"أنا" ,u"نحن" ,u"أنت" ,u"أنتِ" ,u"أنتما" ,u"أنتما مؤ" ,u"أنتم" ,u"أنتن" ,u"هو" ,u"هي" ,u"هما" ,u"هما مؤ" ,u"هم" ,u"هن");
PronounAna=u"أنا";
PronounNahnu=u"نحن";
PronounAnta=u"أنت";
PronounAnti=u"أنتِ";
PronounAntuma=u"أنتما";
PronounAntuma_f=u"أنتما مؤ";
PronounAntum=u"أنتم";
PronounAntunna=u"أنتن";
PronounHuwa=u"هو";
PronounHya=u"هي";
PronounHuma=u"هما";
PronounHuma_f=u"هما مؤ";
PronounHum=u"هم";
PronounHunna=u"هن";


ImperativePronouns=(u"أنت" ,u"أنتِ" ,u"أنتما" ,u"أنتما مؤ" ,u"أنتم" ,u"أنتن" );
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
past[u"أنتما مؤ"]=[u"",u"ْتُما"];
past[u"هما"]=[u"",u"َا"];
past[u"هما مؤ"]=[u"",u"َتَا"];
past[u"نحن"]=[u"",u"ْنَا"];
past[u"أنتم"]=[u"",u"ْتُم"];
past[u"أنتن"]=[u"",u"ْتُنَّ"];
##past[u"هم"]=[u"",u"ُوا"];
past[u"هم"]=[u"",DAMMA+WAW+ALEF_WASLA];
past[u"هن"]=[u"",u"ْنَ"];
future={}
future[u"أنا"]=[u"أ",u"ُ"];
future[u"أنت"]=[u"ت",u"ُ"];
future[u"أنتِ"]=[u"ت",u"ِينَ"];
future[u"أنتم"]=[u"ت",u"ُونَ"];
future[u"أنتما"]=[u"ت",FATHA+ALEF+NOON+KASRA];
future[u"أنتما مؤ"]=[u"ت",FATHA+ALEF+NOON+KASRA];
future[u"أنتن"]=[u"ت",SUKUN+NOON+FATHA];
future[u"نحن"]=[u"ن",u"ُ"];
future[u"هم"]=[u"ي",u"ُونَ"];
future[u"هما"]=[u"ي",u"َانِ"];
future[u"هما مؤ"]=[u"ت", u"َانِ"];
future[u"هن"]=[u"ي",u"ْنَ"];
future[u"هو"]=[u"ي",u"ُ"];
future[u"هي"]=[u"ت",u"ُ"];
future_majzoom={}
future_majzoom[u"أنا"]=[u"أ",u"ْ"];
future_majzoom[u"أنت"]=[u"ت",u"ْ"];
future_majzoom[u"أنتِ"]=[u"ت",u"ِي"];
future_majzoom[u"أنتم"]=[u"ت",DAMMA+WAW+ALEF_WASLA];
##future_majzoom[u"أنتم"]=[u"ت",DAMMA+WAW+ALEF];
future_majzoom[u"أنتما"]=[u"ت",u"َا"];
future_majzoom[u"أنتما مؤ"]=[u"ت",u"َا"];
future_majzoom[u"أنتن"]=[u"ت",u"ْنَ"];
future_majzoom[u"نحن"]=[u"ن",u"ْ"];
##future_majzoom[u"هم"]=[u"ي",DAMMA+WAW+ALEF];
future_majzoom[u"هم"]=[u"ي",DAMMA+WAW+ALEF_WASLA];
future_majzoom[u"هما"]=[u"ي",u"َا"];
future_majzoom[u"هما مؤ"]=[u"ت", u"َا"];
future_majzoom[u"هن"]=[u"ي",u"ْنَ"];
future_majzoom[u"هو"]=[u"ي",u"ْ"];
future_majzoom[u"هي"]=[u"ت",u"ْ"];
future_mansoub={}
future_mansoub[u"أنا"]=[u"أ",u"َ"];
future_mansoub[u"أنت"]=[u"ت",u"َ"];
future_mansoub[u"أنتِ"]=[u"ت",u"ِي"];
future_mansoub[u"أنتم"]=[u"ت",DAMMA+WAW+ALEF_WASLA];
##future_mansoub[u"أنتم"]=[u"ت",DAMMA+WAW+ALEF];
future_mansoub[u"أنتما"]=[u"ت",u"َا"];
future_mansoub[u"أنتما مؤ"]=[u"ت",u"َا"];
future_mansoub[u"أنتن"]=[u"ت",u"ْنَ"];
future_mansoub[u"نحن"]=[u"ن",u"َ"];
##future_mansoub[u"هم"]=[u"ي",DAMMA+WAW+ALEF];
future_mansoub[u"هم"]=[u"ي",DAMMA+WAW+ALEF_WASLA];
future_mansoub[u"هما"]=[u"ي",u"َا"];
future_mansoub[u"هما مؤ"]=[u"ت", u"َا"];
future_mansoub[u"هن"]=[u"ي",u"ْنَ"];
future_mansoub[u"هو"]=[u"ي",u"َ"];
future_mansoub[u"هي"]=[u"ت",u"َ"];
imperative={}
imperative[u"أنت"]=[u"",u"ْ"];
imperative[u"أنتِ"]=[u"",u"ِي"];
imperative[u"أنتم"]=[u"",DAMMA+WAW+ALEF_WASLA];
##imperative[u"أنتم"]=[u"",DAMMA+WAW+ALEF];

imperative[u"أنتما"]=[u"",u"َا"];
imperative[u"أنتما مؤ"]=[u"",u"َا"];
imperative[u"أنتن"]=[u"",u"ْنَ"];
TableTensePronoun={}
TableTensePronoun[TensePast]=past;
TableTensePronoun[TensePassivePast]=past;
TableTensePronoun[TenseFuture]=future;
TableTensePronoun[TensePassiveFuture]=future;
TableTensePronoun[TenseImperative]=imperative;

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


NOT_DEF_HARAKA=TATWEEL;

STRIP_HARAKA=u"i";
ALEF_HARAKA=SMALL_ALEF;
ALEF4_HARAKA=u"y";
ALEF_YEH_HARAKA=u"#";
ALEF_WAW_HARAKA=u"*";
YEH_HARAKA=SMALL_YEH;
ALTERNATIVE_YEH_HARAKA=u"t"
WAW_HARAKA=SMALL_WAW;

HARAKAT=u"%s%s%s%s%s"%(SUKUN,FATHA,DAMMA,KASRA,SHADDA);
HARAKAT2=u"%s%s%s%s%s%s%s"%(ALEF_HARAKA,WAW_HARAKA,YEH_HARAKA,SUKUN,FATHA,DAMMA,KASRA);
HAMZAT=u"%s%s%s%s%s"%(ALEF_HAMZA_ABOVE, WAW_HAMZA, YEH_HAMZA , HAMZA, ALEF_HAMZA_BELOW);
BEGIN_WORD=u"^";
END_WORD=u"$";

LONG_HARAKAT=(ALEF_HARAKA,YEH_HARAKA,WAW_HARAKA,ALEF_YEH_HARAKA,ALEF_WAW_HARAKA);
_F=FATHA;
_D=DAMMA;
_K=KASRA;
_S=SUKUN;
_A=ALEF_HARAKA;
_W=WAW_HARAKA;
_Y=YEH_HARAKA

_AH=ALEF_HARAKA;
_YH=YEH_HARAKA
_WH=WAW_HARAKA
_AYH=ALEF_YEH_HARAKA
_AWH=ALEF_WAW_HARAKA
_YHALT=ALTERNATIVE_YEH_HARAKA
##tab_change_haraka={};
##tab_change_haraka[_S]={_S:_S,_F:_F,_D:_D,_K:_K,_AH:_AH,_WH:_WH,_YH:_YH}
##tab_change_haraka[_F]={_S:_S,_F:_F,_D:_D,_K:_K,_AH:_AH,_WH:_WH,_YH:_YH}
##tab_change_haraka[_D]={_S:_S,_F:_F,_D:_D,_K:_K,_AH:_AH,_WH:_WH,_YH:_YH}
##tab_change_haraka[_K]={_S:_S,_F:_F,_D:_D,_K:_K,_AH:_AH,_WH:_WH,_YH:_YH}
##tab_change_haraka[_AH]={_S:_F,_F:_AH,_D:_WH,_K:_YH,_AH:u"",_YH:u"",_WH:u"",_YH:u""}
##tab_change_haraka[_WH]={_S:_D,_F:_AH,_D:_WH,_K:_YH,_AH:u"",_WH:u"",_YH:u""}
##tab_change_haraka[_YH]={_S:_K,_F:_AH,_D:_WH,_K:_YH,_AH:u"",_WH:u"",_YH:u""}
##tab_change_haraka[_AWH]={_S: (u"%s%s"%(_F,_S),_W),_F:(u"%s%s"%(_F,_F),_W),_D:_WH,_K:_YH,_AH:(u"%s%s"%(_F,_AH),_W),_WH:_WH,_YH:_YH}
##tab_change_haraka[_AYH]={_S:(u"%s%s"%(_F,_S),_Y),_F:(u"%s%s"%(_F,_F),_Y),_D:_YH,_K:_YH,_AH:(u"%s%s"%(_F,_AH),_Y),_WH:_WH,_YH:_YH}
#HAMZAT
_AHA=ALEF_HAMZA_ABOVE
_AHB=ALEF_HAMZA_BELOW
_AM=ALEF_MADDA;
_YHA=YEH_HAMZA
_WHA=WAW_HAMZA
_HZ=HAMZA


tab_tahmeez_initial={_S:_HZ,_F:_AHA,_D:_AHA, _K:_AHB,_AH:_AM ,_WH:_AHA, _YH:_AHB,_YHALT:_AHB};


tab_tahmeez_middle={};
tab_tahmeez_middle[_S]={_S:_HZ,_F:_AHA,_D:_WHA, _K:_YHA,_AH:_AHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_middle[_F]={_S:_AHA,_F:_AHA,_D:_WHA, _K:_YHA,_AH:_AHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_middle[_D]={_S:_WHA,_F:_WHA,_D:_WHA, _K:_YHA,_AH:_WHA,_WH:_WHA, _YH:_YHA };
tab_tahmeez_middle[_K]={_S:_YHA,_F:_YHA,_D:_YHA, _K:_YHA,_AH:_YHA,_WH:_YHA, _YH:_YHA };
tab_tahmeez_middle[_AH]={_S:_HZ,_F:_HZ,_D:_WHA, _K:_YHA,_AH:_HZ,_WH:_WHA, _YH:_YHA };
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
