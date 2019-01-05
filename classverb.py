7#!/usr/bin/python
# -*- coding=utf-8 -*-
from ar_ctype import *
from verb_const import *
from conjugatedisplay import *
import sys,re,string


# بنية جذع تصريف الجذع
#تتكون من الزمن، الحروف والحركات
# تستعمل لتخزين جذوع التصريف
class conjug_stem:
	tense=u"";
	letters=u"";
	marks=u"";
	def __init__(self,tense,letters,marks):
		self.tense=tense;
		self.letters=letters;
		self.marks=marks;

class verbclass :
	verb=u"";
#" internl verb : is the uniformate form of the verb"
	internal_verb=u"";
#" internl verb : is the uniformate form of the verb"
	word_letters=u"";
	word_marks=u"";
	root=u"";
	vtype=u"";
	future_type=u'';
	bab_sarf=0;
	transitive=u"";
	intransitive=u"";
	adjwaf=False;
	type_adjwaf=u'';
	naqis=False;
	type_naqis=u'';
	methal=False;
	mudhaaf=False;
	mahmouz_awal=False;
	teh_zaida=False;
	past_stem=u"";
	passive_past_stem=u"";
	future_stem=u"";
	passive_future_stem=u"";
	imperative_stem=u"";
	conj_display=None;
	tab_conjug_stem=None;

#---------------------------------------------------------------------------
	def __init__(self,verb,root,transitive, future_type=FATHA, intransitive=True,bab_sarf=0):
		self.verb=verb;
		self.internal_verb=uniformate(verb);
##		print (u" الكتابة الداخلية للفعل 1"+self.internal_verb).encode("utf8");
## الوظيفة Uniformate لا تحذف الألفات، وتستعمل لحسابحساب الطول الفعلي للفعل
		self.future_type=future_type;
		(self.word_letters,self.word_marks)=uniformate2(verb,"verb");
##		print (u" الكتابة الداخلية للفعل 1"+self.word_letters+" - "+self.word_marks).encode("utf8");
##		(self.word_letters,self.word_marks)=uniformate_alef_origin(self.word_marks,self.internal_verb,self.future_type);
		self.word_marks=uniformate_alef_origin(self.word_marks,self.internal_verb,self.future_type);
##		print (u" الكتابة الداخلية للفعل "+self.word_letters+" - "+self.word_marks).encode("utf8");
		self.root=root;
		self.transitive=transitive;
		self.intransitive=intransitive;
		self.bab_sarf=bab_sarf;
		self.adjwaf=False;
		self.type_adjwaf=False;
		self.naqis=False;
		self.naqis=False;
		self.methal=False;
		self.mudhaaf=False;
		self.mahmouz_awal=False;
		self.teh_zaida=False;
		self.conj_display=conjugatedisplay(self.verb);
		self.tab_conjug_stem={};
		pass;
#---------------------------------------------------------------------------
	def verb_class(self):
		verb=self.verb;
		root=self.root;
		tab_type=[u"",u"",u"",u"فعل ثلاثي",u"فعل رباعي",u"فعل خماسي",u"فعل سداسي",u"فعل سباعي",u"فعل ثماني",u"فعل تساعي"];
		verb=uniformate(verb);
		verb_nm=ar_strip_marks_keepshadda(verb);
		self.vtype=tab_type[len(verb_nm)];
## print verb.encode("utf8"),self.vtype.encode("utf8"),
#الفعل الناقص
		if verb_nm[len(verb_nm)-1]==ALEF or  verb_nm[len(verb_nm)-1]==ALEF_MAKSURA:
			if root[2]==WAW:
				self.naqis=True;
				self.type_naqis=WAW ;
## print u"ناقص واوي".encode("utf8"),
			elif root[2]==YEH:
				self.naqis=True;
				self.type_naqis=YEH ;
##                verb_nm
##				print u"ناقص يائي".encode("utf8"),
#الفعل الأجوف
		if verb_nm[len(verb_nm)-2]==ALEF :
			pos_alef=self.internal_verb.rfind(ALEF);
			if root[1]==WAW:
				self.adjwaf=True;
				self.type_adjwaf=WAW ;
##				print u"أجوف واوي".encode("utf8"),
			elif root[1]==YEH:
				self.adjwaf=True;
				self.type_adjwaf=YEH ;
##				print u"أجوف يائي".encode("utf8"),
#الفعل الثلاثي المثال
		if  len(verb_nm)==3 and len(root)==3 and verb_nm.startswith(WAW ) and root.startswith(WAW):
				self.methal=True;
##				print u"مثال".encode("utf8"),
		if verb_nm.endswith(SHADDA) and root[len(root)-1]==root[len(root)-2]:
				self.mudhaaf=True;
##				print u"مضعف".encode("utf8"),
		if (verb_nm.startswith(ALEF_HAMZA_ABOVE) or verb_nm.startswith(HAMZA)) and root[0]in (ALEF_HAMZA_ABOVE,HAMZA):
				self.mahmouz_awal=True;
##				print u"مهموز الأول".encode("utf8"),
		else:self.mahmouz_awal=False;
# التاء الزائدة
# يمكن التعرف على التاء الزائدة باستعمال الجذر
# تعتبر التاء في أول الفعل زائدة إذا لم يبتدئ الجذر بها
#إذا كان أول الجذر تاء، وابتدأ الفعل بتاءين فالأولى زائدة

		if (verb_nm.startswith(u"%s%s"%(TEH,TEH)) and root[0]==TEH)or (verb_nm.startswith(TEH) and root[0]!=TEH):
			self.teh_zaida=True;
##			print u"تاء زائدة".encode("utf8"),
##		print;
		self.prepare_future_and_imperative_stem();
		self.prepare_past_stem();
		self.prepare_passive_past_stem();


#معالجة الإعلال
#---------------------------------------------------------------------------
	def join(self,stem_l,stem_m,pre_val,suf_val):

		if pre_val!=u"":
			pre_val_l=pre_val;
#			pre_val_m=self.future_stem_marks[0];
##مشكلة عند تصريف الفعل المضارع المجهول
##			pre_val_m=self.tab_conjug_stem[TenseFuture].marks[0]
			pre_val_m=stem_m[0];
			stem_m=stem_m[1:];
		else:
			pre_val_l=u"";
			pre_val_m=u"";

		suf_val=TATWEEL+suf_val;
		(suf_val_l,suf_val_m)=uniformate2(suf_val);
		conj_l=pre_val_l+stem_l+suf_val_l;
		if suf_val_l.startswith(TATWEEL):
			conj_m=pre_val_m+stem_m[:-1]+suf_val_m;
			# مع افتراض أنّ الفعل لا ينتهي بحركة طويلة، الحرف الأخير من الفعل الناقص هو حرف كامل
			#يجب فقط حذف الياء والواو إذا كانا بين فتحتين.
#			(stem_l,conj_m)=join_marks(stem_l,stem_m,val_m,self.future_type);
			conj_l=pre_val_l+stem_l+suf_val_l[1:];
		else :
			conj_l=pre_val+stem_l+suf_val_l;
			conj_m=pre_val_m+stem_m+suf_val_m;


		conj_m=treat_sukun2(conj_l,conj_m,self.future_type);
##		conj_l=tahmeez2(conj_l,conj_m);
##		conj_l,conj_m=homogenize(conj_l,conj_m);
		conj=standard2(conj_l,conj_m);
		return conj;
#-------------------------------------------------------------------------------------
	def engin_swap(self,theword):
		return convert_orthograph(theword,self.future_type);

# التصريف
# التصريف في المضارع المعلوم
#---------------------------------------------------------------------------
	def prepare_future_and_imperative_stem(self):
		verb=self.internal_verb;
		verb_nm=ar_strip_marks_keepshadda(verb)
		marks=self.word_marks;
		letters=self.word_letters;
		future_letter_mark=FATHA;
		passive_future_letter_mark=DAMMA;
		if not self.teh_zaida and len(verb_nm)==4:
			future_letter_mark=DAMMA;
		before_last_mark=marks[-2:-1];
		passive_before_last_mark=marks[-2:-1];
		if not self.teh_zaida and len(verb_nm)>=4:
			if before_last_mark in HARAKAT:
				before_last_mark=KASRA;

			elif before_last_mark in LONG_HARAKAT:
			#  حالة انفال ينفال وافتال يفتال وافطال يفطال.
				if len(verb_nm)==5 :before_last_mark=ALEF_HARAKA;
				else: before_last_mark=YEH_HARAKA;
		elif len(verb_nm)==3:
			if before_last_mark in HARAKAT:
				before_last_mark=self.future_type;
				passive_before_last_mark=FATHA;
			elif before_last_mark in LONG_HARAKAT:
				if self.future_type==FATHA :before_last_mark=ALEF_HARAKA;
				elif self.future_type==DAMMA:before_last_mark=WAW_HARAKA;
				elif self.future_type==KASRA :before_last_mark=YEH_HARAKA;
##معالجة حالة الفعل المبدوء بهمزة قطع المهموز الأول
##والفعل المبدوء بهمزة وصل
		if letters.startswith(ALEF) or ((letters.startswith(HAMZA)or letters.startswith(ALEF_HAMZA_ABOVE))  and not self.mahmouz_awal):
			letters=letters[1:];
			marks=marks[1:];
## معالجة حالة الفعل المثال الواوي الذي عين مضارعه مكسورة
		first_mark=marks[0];
		if len(verb_nm)==3:
##		    print "1";
		    first_mark=SUKUN;
##		    passive_marks=DAMMA+first_mark+marks[1:-2]+passive_before_last_mark+marks[-1:];
		if len(marks)==2:
##			print "2";
##			passive_marks=DAMMA+passive_before_last_mark+marks[-1:];
##إذا كان الفعل الثلاثي أجوفا، كان عدد حركاته اثنين، ويكون عند البناء للمجهول ألفا على الدوام
			passive_marks=DAMMA+ALEF_HARAKA+marks[-1:];
			new_marks=future_letter_mark+before_last_mark+marks[-1:];
##حالة الفلع المثال الواوي، ذو حركة عين مضارعه كسرة
##وحركة واوه سكون
##من أجل منع حالة الواو ذو الحركة الطويلة
		elif len(letters)==3 and  first_mark==SUKUN and letters.startswith(WAW) and self.future_type==KASRA:
##  يحذف الواو في كلتا الحالتين وتصبح حركة طويلة في المبني للمجهول
			letters=letters[1:];
##			marks=marks[1:];
## يحذف الواو في أول المضارع المعلوم
			new_marks=future_letter_mark+before_last_mark+marks[-1:];
## يحذف الواو في أول المضارع المجهول، ويصبح حركة طويلة لحرف المضارعة
			passive_marks=WAW_HARAKA+passive_before_last_mark+marks[-1:];
##			new_marks=future_letter_mark+before_last_mark+marks[-1:];
		else:
##			print "3";
			passive_marks=DAMMA+first_mark+marks[1:-2]+passive_before_last_mark+marks[-1:];
			new_marks=future_letter_mark+first_mark+marks[1:-2]+before_last_mark+marks[-1:];

### تحضير جذع الأمر
		imp_letters=self.word_letters;
##حالة الفعل الثلاثي المثال الواوي، الذي حركته ساكنة في المضارع، وحركة  عينه كسرة
##تحذف الواو
		if len(self.word_letters)==3 and  first_mark==SUKUN and self.word_letters.startswith(WAW) and self.future_type==KASRA:
			imp_letters=self.word_letters[1:];
			imp_marks=KASRA+marks[-1:];
		elif len(letters)!=len(self.word_letters):
		    imp_marks=self.word_marks;
		else:
		    imp_marks=new_marks[1:];
## معالجة الفعل الناقص عند تصريفه في المجهول
## تستبدل واو التاقص الذي حركة عين ماضيه فتحة بياء
		passive_letters=letters;
		if len(self.word_letters)==3 and self.word_letters.endswith(WAW) and marks[1]==FATHA:
		  passive_letters=passive_letters[:-1]+YEH;
##  القعل الأمر يأخذ نفس حركات الفعل المضارع دون حركة حرف المضارعة
		imp_marks=imp_marks[:-2]+before_last_mark+imp_marks[-1:];
## معلجة إضافة حرف ألف الوصل في الأفعال المسبوقة بالسكون
##
##		if len(imp_letters)==3 and len(verb_nm)==3:
##			imp_letters=ALEF+imp_letters;
##			if self.future_type==DAMMA:
##				imp_marks=DAMMA+imp_marks;
##			else :imp_marks=KASRA+imp_marks;

		self.tab_conjug_stem[TenseFuture]=conjug_stem(TenseFuture,letters,new_marks);
		self.tab_conjug_stem[TensePassiveFuture]=conjug_stem(TensePassiveFuture,passive_letters,passive_marks);
		self.tab_conjug_stem[TenseImperative]=conjug_stem(TenseImperative,imp_letters,imp_marks);
#	--------------------------------------------------------------------------
	def prepare_past_stem(self):
		self.past_stem=self.internal_verb;
		self.tab_conjug_stem[TensePast]=conjug_stem(TensePast,self.word_letters,self.word_marks);

#التصريف في الماضي المجهول.
#---------------------------------------------------------------------------
	def prepare_passive_past_stem(self):
		verb=self.internal_verb;
		letters=self.word_letters;
		marks=self.word_marks;
## من أجل معالجة الفعل الثلاثي الناقص الواوي، نعتبر واوه ياء
## شرط أن تكون حركة عينه في الماضي فتحة
		if len(letters)==3 and letters.endswith(WAW) and marks[1]==FATHA:
##		if len(letters)==3 and letters.endswith(WAW):
		    letters=letters[:-1]+YEH;
		first_mark=marks[0];
		# treat first_mark
## حالة فاعل فوعل
##مع استبعاد حلة الثلاثي
##الثلاثي المعتل
##الذي يكون طوله هنا حرفين، مع اعتبار حرف العلة الأوسط حركة
		if first_mark in LONG_HARAKAT and len(marks)>2:
			first_mark=WAW_HARAKA;
		else :
			first_mark=DAMMA;
		before_last_mark=marks[-2:-1];
## -	حالة الفعل الأجوف الذي حركة مضارعه فتحة أو كسرة،
##-	فيصبح في الماضي عند التقاء الساكنين كسرة، لذا يجب تعديل ذلك في الماضي المجهول، بجعلها تتحول إلى ضمة عند التقاء الساكنين.
		if len(marks)==2 and marks[0] in (ALEF4_HARAKA,ALEF_WAW_HARAKA,ALEF_YEH_HARAKA,ALEF_HARAKA)and  self.future_type in(FATHA,KASRA):
		    before_last_mark=ALTERNATIVE_YEH_HARAKA;
## إذا كان الحرف ما قبل الخير حركة طويلة، تصبح ياء
		elif before_last_mark in LONG_HARAKAT:
			before_last_mark=YEH_HARAKA;
		else :
			before_last_mark=KASRA;
		if len(marks)==2:
			marks=before_last_mark+marks[-1:];
## -	حالة الفعل الأجوف الذي حركة مضارعه فتحة أو كسرة،
##-	فيصبح في الماضي عند التقاء الساكنين كسرة، لذا يجب تعديل ذلك في الماضي المجهول، بجعلها تتحول إلى ضمة عند التقاء الساكنين.

		else:
			mm=marks[1:-2];
			middle_marks=u"";
# يتم ضم كل الحركات غير السكون في ماتبقى من الكلمة
# حالة تفاعل تُفوعِل
#حالة افتعل افتُعِل
#حالة اُسْتُفعِل
			for c in mm:
				if c !=SUKUN:
					if c in LONG_HARAKAT:
						middle_marks+=WAW_HARAKA;
					else :middle_marks+=DAMMA;
				else: middle_marks+=SUKUN;
			marks=first_mark+middle_marks+before_last_mark+marks[-1:];
##		self.tab_conjug_stem[TensePassivePast]=conjug_stem(TensePassivePast,self.word_letters,marks);
		self.tab_conjug_stem[TensePassivePast]=conjug_stem(TensePassivePast,letters,marks);

#---------------------------------------------------------------------

	def conjugate_tense_pronoun(self,tense,pronoun):
##		print "tense",tense,"pronoun",pronoun;
		prefix=TableTensePronoun[tense][pronoun][0];
		suffix=TableTensePronoun[tense][pronoun][1];
		stem_l=self.tab_conjug_stem[tense].letters;
		stem_m=self.tab_conjug_stem[tense].marks;
		return self.join(stem_l,stem_m,prefix,suffix);
#--------------------------------------------------------------------------------
# التصريف في الأزمنة المختلفة،
# عند وضع قائمة خاصة بالأزمنة المختارة،
# تلقائيا كافة الأزمنة
#--------------------------------------------------------------------------------
	def conjugate_all_tenses2(self,listtense=TableTense):
#		if listtense==None: listtense=TableTense;
		for tense in listtense:
			if tense !=TenseImperative:
				for pron in PronounsTable:
					conj=self.conjugate_tense_pronoun(tense,pron);
					self.conj_display.add(tense,pron,conj);
			else:
				for pron in  ImperativePronouns:
					conj=self.conjugate_tense_pronoun(TenseImperative,pron);
					self.conj_display.add(tense,pron,conj);
##		self.conj_display.display_html(listtense);
		self.conj_display.display_html(listtense);


#-
#--------------------------------------------------------------------------------
# التصريف في الأزمنة المختلفة،
# عند وضع قائمة خاصة بالأزمنة المختارة،
# تلقائيا كافة الأزمنة
#--------------------------------------------------------------------------------
	def conjugate_all_tenses(self,listtense=TableTense):
#		if listtense==None: listtense=TableTense;
		for tense in listtense:
			if tense ==TensePast:
					conj_ana=self.conjugate_tense_pronoun(tense,PronounAna);
					self.conj_display.add(tense,PronounAna,conj_ana);
					conj_ana_without_last_mark=conj_ana[:-1];
					self.conj_display.add(tense,PronounAnta,conj_ana_without_last_mark+FATHA);
					self.conj_display.add(tense,PronounAnti,conj_ana_without_last_mark+KASRA);
					self.conj_display.add(tense,PronounAntuma,conj_ana+MEEM+FATHA+ALEF);
					self.conj_display.add(tense,PronounAntuma_f,conj_ana+MEEM+FATHA+ALEF);
					self.conj_display.add(tense,PronounAntum,conj_ana+MEEM);
					self.conj_display.add(tense,PronounAntunna,conj_ana+NOON+SHADDA+FATHA)
					self.conj_display.add(tense,PronounAna,conj_ana);

					conj_nahnu=self.conjugate_tense_pronoun(tense,PronounNahnu);
					self.conj_display.add(tense,PronounNahnu,conj_nahnu);

					conj_hunna=self.conjugate_tense_pronoun(tense,PronounHunna);
					self.conj_display.add(tense,PronounHunna,conj_hunna);

					conj_huma=self.conjugate_tense_pronoun(tense,PronounHuma);
					self.conj_display.add(tense,PronounHuma,conj_huma);

					conj_hum=self.conjugate_tense_pronoun(tense,PronounHum);
					self.conj_display.add(tense,PronounHum,conj_hum);

					conj_hunna=self.conjugate_tense_pronoun(tense,PronounHunna);
					self.conj_display.add(tense,PronounHunna,conj_hunna);

					conj_huwa=self.conjugate_tense_pronoun(tense,PronounHuwa);
					self.conj_display.add(tense,PronounHuwa,conj_huwa);
##					conj_ana_without_last_mark=conj_ana[:-1];
					if conj_huwa.endswith(ALEF_MAKSURA) or conj_huwa.endswith(ALEF):
					   self.conj_display.add(tense,PronounHya,conj_huwa[:-1]+TEH+SUKUN);
					   self.conj_display.add(tense,PronounHuma_f,conj_huwa[:-1]+TEH+FATHA+ALEF);
					else :
					   self.conj_display.add(tense,PronounHya,conj_huwa+TEH+SUKUN);
					   self.conj_display.add(tense,PronounHuma_f,conj_huwa+TEH+FATHA+ALEF);

			elif tense ==TensePassivePast:
					conj_ana=self.conjugate_tense_pronoun(tense,PronounAna);
					self.conj_display.add(tense,PronounAna,conj_ana);
					conj_ana_without_last_mark=conj_ana[:-1];
					self.conj_display.add(tense,PronounAnta,conj_ana_without_last_mark+FATHA);
					self.conj_display.add(tense,PronounAnti,conj_ana_without_last_mark+KASRA);
					self.conj_display.add(tense,PronounAntuma,conj_ana+MEEM+FATHA+ALEF);
					self.conj_display.add(tense,PronounAntuma_f,conj_ana+MEEM+FATHA+ALEF);
					self.conj_display.add(tense,PronounAntum,conj_ana+MEEM);
					self.conj_display.add(tense,PronounAntunna,conj_ana+NOON+SHADDA+FATHA)
					self.conj_display.add(tense,PronounAna,conj_ana);

					conj_nahnu=self.conjugate_tense_pronoun(tense,PronounNahnu);
					self.conj_display.add(tense,PronounNahnu,conj_nahnu);

					conj_hunna=self.conjugate_tense_pronoun(tense,PronounHunna);
					self.conj_display.add(tense,PronounHunna,conj_hunna);

					conj_huma=self.conjugate_tense_pronoun(tense,PronounHuma);
					self.conj_display.add(tense,PronounHuma,conj_huma);

					conj_hum=self.conjugate_tense_pronoun(tense,PronounHum);
					self.conj_display.add(tense,PronounHum,conj_hum);

					conj_hunna=self.conjugate_tense_pronoun(tense,PronounHunna);
					self.conj_display.add(tense,PronounHunna,conj_hunna);

					conj_huwa=self.conjugate_tense_pronoun(tense,PronounHuwa);
					self.conj_display.add(tense,PronounHuwa,conj_huwa);
##					conj_ana_without_last_mark=conj_ana[:-1];
##					if conj_huwa.endswith(ALEF_MAKSURA) or conj_huwa.endswith(ALEF):
##					   self.conj_display.add(tense,PronounHya,conj_huwa[:-1]+TEH+SUKUN);
##					   self.conj_display.add(tense,PronounHuma_f,conj_huwa[:-1]+TEH+FATHA+ALEF);
##					else :
					self.conj_display.add(tense,PronounHya,conj_huwa+TEH+SUKUN);
					self.conj_display.add(tense,PronounHuma_f,conj_huwa+TEH+FATHA+ALEF);

##				for pron in PronounsTable:
##					conj=self.conjugate_tense_pronoun(tense,pron);
##					self.conj_display.add(tense,pron,conj);
			elif tense ==TenseFuture or tense==TensePassiveFuture:
					conj_ana=self.conjugate_tense_pronoun(tense,PronounAna);
					self.conj_display.add(tense,PronounAna,conj_ana);

					conj_anta=self.conjugate_tense_pronoun(tense,PronounAnta);
					self.conj_display.add(tense,PronounAnta,conj_anta);
					conj_anta_without_future_letter=conj_anta[1:];
##					self.conj_display.add(tense,PronounAnta,TEH+conj_ana_without_future_letter);
					self.conj_display.add(tense,PronounNahnu,NOON+conj_anta_without_future_letter);
					self.conj_display.add(tense,PronounHuwa,YEH+conj_anta_without_future_letter);
					self.conj_display.add(tense,PronounHya,TEH+conj_anta_without_future_letter);

					conj_anti=self.conjugate_tense_pronoun(tense,PronounAnti);
					self.conj_display.add(tense,PronounAnti,conj_anti);

					conj_antuma=self.conjugate_tense_pronoun(tense,PronounAntuma);
					self.conj_display.add(tense,PronounAntuma,conj_antuma);
					self.conj_display.add(tense,PronounAntuma_f,conj_antuma);
					self.conj_display.add(tense,PronounHuma_f,conj_antuma);
					self.conj_display.add(tense,PronounHuma,YEH+conj_antuma[1:]);

					conj_antum=self.conjugate_tense_pronoun(tense,PronounAntum);
					self.conj_display.add(tense,PronounAntum,conj_antum);
					self.conj_display.add(tense,PronounHum,YEH+conj_antum[1:]);

					conj_antunna=self.conjugate_tense_pronoun(tense,PronounAntunna);
					self.conj_display.add(tense,PronounAntunna,conj_antunna);
					self.conj_display.add(tense,PronounHunna,YEH+conj_antunna[1:]);


##			elif tense ==TensePassiveFuture:
##				for pron in PronounsTable:
##					conj=self.conjugate_tense_pronoun(tense,pron);
##					self.conj_display.add(tense,pron,conj);
			elif tense ==TenseImperative:
				for pron in  ImperativePronouns:
					conj=self.conjugate_tense_pronoun(TenseImperative,pron);
					self.conj_display.add(tense,pron,conj);
##		self.conj_display.display_html(listtense);
		return self.conj_display.display_html(listtense);

