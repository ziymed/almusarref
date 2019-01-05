#!/usr/bin/python
# -*- coding=utf-8 -*-
from verb_const import *
import sys,re,string
# صف عرض التصريفات حسب الضمائر
# جدول عرض التصريفات حسب الأزمنة
# تعيينه متغيرا شاملا من أجل تقليل بناء جدول عرض التصريفات في كل عرض.
OneTensePronoun={u"أنا":"" ,u"أنت":"" ,u"أنتِ":"" ,u"هو":"" ,u"هي":"" ,u"أنتما":"" ,u"أنتما مؤ":"" ,u"هما":"" ,u"هما مؤ":"" ,u"نحن":"" ,u"أنتم":"" ,u"أنتن":"" ,u"هم":"" ,u"هن":""};
TableConjug={TensePast:OneTensePronoun.copy(),
	TensePassivePast:OneTensePronoun.copy(),
	TenseFuture:OneTensePronoun.copy(),
	TensePassiveFuture:OneTensePronoun.copy(),
	TenseImperative:OneTensePronoun.copy()
	}

class conjugatedisplay:
	tab_conjug={};
	pronouns={}
	verb=u"";
	def __init__(self,verb):
# بناء جدول عرض التصريفات
		self.tab_conjug=TableConjug.copy();

#------------------------------------------------------------------
	def add(self,tense,pronoun,verbconjugated):
		if tense not in self.tab_conjug.keys():
			self.tab_conjug[tense]={}
		self.tab_conjug[tense][pronoun]=verbconjugated;
#------------------------------------------------------------------
	def display(self,listtense=TableTense):
#		print self.tab_conjug;
##		for tense in listtense:
##			for pronoun in self.tab_conjug[tense].keys():
	   for pronoun in PronounsTable:
	       print pronoun.encode("utf-8"),
	       for tense in listtense:
				print (self.verb).encode("utf-8"),
				if pronoun in self.tab_conjug[tense].keys():
				    print ("\t"+self.tab_conjug[tense][pronoun]).encode("utf-8"),
	       print;
				
#------------------------------------------------------------------
	def display_html(self,listtense=TableTense):
	        html=[]
		html.append("<h2>")
		html.append(self.verb.encode("utf8"));
		html.append("</h2>")
		html.append("<table border=1>");
		html.append("<tr><th></th>");
		for tense in listtense:
			html.append("<th>");
			html.append(tense.encode("utf8"));
			html.append("</th>");
		html.append("</tr>");
		for pronoun in PronounsTable:
			html.append("<tr><th>%s</th>" % pronoun.encode("utf8"));
			for tense in listtense:
				html.append("<td>");
				html.append(self.tab_conjug[tense][pronoun].encode("utf8"));
				html.append("</td>");
			html.append("</tr>");
		html.append("<table>");
		return ''.join(html)
		
##		print "</body></html>";
#------------------------------------------------------------------
	def display_gui(self,listtense=TableTense):
##		text= u"<html dir='rtl'>"
##		text=text+ u"<head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head><body>";
		text=text+ "<h2>"
		text=text+ self.verb.encode("utf8");
		text=text+ "</h2>"
		text=text+ "<table border=1>";
		text=text+ "<tr><th></th>";
		for tense in listtense:
		
			text=text+ "<th>";
#			text=text+ tense.encode("utf8");
			text=text+ tense;
			text=text+ "</th>";
		text=text+ "</tr>";
		for pronoun in PronounsTable:
			text=text+ "<tr><th>"+pronoun;
			text=text+ "</th>";
			for tense in listtense:
				text=text+ "<td>";
				text=text+ self.tab_conjug[tense][pronoun];
#               text=text+ self.tab_conjug[tense][pronoun].encode("utf8");
				text=text+ "</td>";
			text=text+"</tr>";
		text=text+ "<table>";
##		text=text+ "</body></html>";
		return text;
#------------------------------------------------------------------
#	def display_grid(self,grid1,listtense=TableTense):
#	    i=0
#        j=0
#        for pronoun in PronounsTable:
#			j=0;
#			for tense in TableTense:
#				grid1.SelectCellValue(i,j,self.tab_conjug[tense][pronoun])
#				j=j+1
#			i=i+1;
	def display_table(self,listtense=TableTense):
		table={}
		i=0
		j=0
		for pronoun in PronounsTable:
		  table[i]={}
		  table[i][0]=pronoun
		  j=1;
		  for tense in listtense:
		      table[i][j]=self.tab_conjug[tense][pronoun]
		      j=j+1
		  i=i+1;
		return table;
