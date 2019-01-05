# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Dec 18 10:49:49 2002

import wx
from conjugate import *
# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class MyFrame2(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame2.__init__
#-----------------Special Vars to conjugate----------
        self.verb=u"";
        self.root=u"";
        self.future_type=FATHA;
        self.transitive=True;
        self.bab_sarf=0;
        self.verb_obj=None;
        self.listetenses=[];
#-----------------------------------------
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.myTitle = wx.StaticText(self, -1, _("Arabic Verb Conjugtion"), style=wx.ALIGN_CENTRE)
        self.label_1 = wx.StaticText(self, -1, _("Verb"), style=wx.ALIGN_CENTRE)
        self.BoxVerb = wx.TextCtrl(self, -1, u"رَجَعَ")
        #self.BoxVerb.Value=u"رَجَعَ";
        self.BConjugate = wx.Button(self, -1, _("Conjugate"))
        self.RTransitive = wx.RadioBox(self, -1, _("Transitive"), choices=[_("Transitive"), _("Intransitive")], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.CActiveFuture = wx.CheckBox(self, -1, _("Active Future Tense"))
        self.CActivePast = wx.CheckBox(self, -1, _("Active Past Tense"))
        self.label_2 = wx.StaticText(self, -1, _("Root"))
        self.TRoot = wx.TextCtrl(self, -1, u"رجع")
        self.CPassiveFuture = wx.CheckBox(self, -1, _("Passive Future Tense"))
        self.CPassivePast = wx.CheckBox(self, -1, _("Passive Past Tense"))
        self.TFutureMode = wx.StaticText(self, -1, _("Conjugation future Mode"))
        self.ListFutureMode = wx.ComboBox(self, -1, choices=[_("FATHA"), _("DAMMA"), _("KASRA"), _("SUKUN")], style=wx.CB_DROPDOWN)
        self.CImperative = wx.CheckBox(self, -1, _("ImperativeTense"))
        self.CAllTense = wx.CheckBox(self, -1, _("All Tense"))
        self.grid_1 = wx.grid.Grid(self, -1, size=(1, 1))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.ConjugateOneVerb, self.BConjugate)
        self.Bind(wx.EVT_RADIOBOX, self.SetTransitive, self.RTransitive)
        self.Bind(wx.EVT_CHECKBOX, self.SetActiveFuture, self.CActiveFuture)
        self.Bind(wx.EVT_CHECKBOX, self.SetActivePaste, self.CActivePast)
        self.Bind(wx.EVT_TEXT_ENTER, self.SetRoot, self.TRoot)
        self.Bind(wx.EVT_TEXT, self.SetRoot, self.TRoot)
        self.Bind(wx.EVT_CHECKBOX, self.SetPassiveFuture, self.CPassiveFuture)
        self.Bind(wx.EVT_CHECKBOX, self.SetPassivePast, self.CPassivePast)
        self.Bind(wx.EVT_CHECKBOX, self.SetImperative, self.CImperative)
        self.Bind(wx.EVT_CHECKBOX, self.SetAllTense, self.CAllTense)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame2.__set_properties
        self.SetTitle(_("frame_3"))
        self.myTitle.SetMinSize((392, 50))
        self.myTitle.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_1.SetMinSize((41, 24))
        self.label_1.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.RTransitive.SetSelection(0)
        self.CActiveFuture.SetValue(1)
        self.CActivePast.SetValue(1)
        self.CPassiveFuture.SetValue(1)
        self.CPassivePast.SetValue(1)
        self.ListFutureMode.SetSelection(1)
        self.CImperative.SetValue(1)
        self.CAllTense.SetValue(1)
        self.grid_1.CreateGrid(14, 6)
        self.grid_1.SetColLabelValue(0, _(u"الضمائر"))
        self.grid_1.SetColSize(0, 14)
        self.grid_1.SetColLabelValue(1, _(u"الماضي"))
        self.grid_1.SetColSize(1, 14)
        self.grid_1.SetColLabelValue(2, _(u"الماضي المبني للمجهول"))
        self.grid_1.SetColSize(2, 14)
        self.grid_1.SetColLabelValue(3, _(u"المضارع "))
        self.grid_1.SetColSize(3, 14)
        self.grid_1.SetColLabelValue(4, _(u"المضارع المبني للمجهول"))
        self.grid_1.SetColSize(4, 14)
        self.grid_1.SetColLabelValue(5, _(u"الأمر"))
        self.grid_1.SetColSize(5, 14)
        self.grid_1.SetMinSize((700,400))
        self.grid_1.SetFont(wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "ABO SLMAN Alomar  منقط ومسطر  2"))

        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame2.__do_layout
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(self.myTitle, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_7.Add(self.label_1, 0, wx.BOTTOM, 0)
        sizer_7.Add(self.BoxVerb, 0, 0, 0)
        sizer_7.Add(self.BConjugate, 0, 0, 0)
        sizer_6.Add(sizer_7, 0, 0, 0)
        grid_sizer_1.Add(self.RTransitive, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.CActiveFuture, 0, wx.LEFT, 0)
        grid_sizer_1.Add(self.CActivePast, 0, wx.LEFT, 0)
        sizer_10.Add(self.label_2, 0, wx.EXPAND, 0)
        sizer_10.Add(self.TRoot, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_10, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.CPassiveFuture, 3, wx.LEFT, 0)
        grid_sizer_1.Add(self.CPassivePast, 0, wx.LEFT, 0)
        sizer_11.Add(self.TFutureMode, 0, wx.EXPAND, 0)
        sizer_11.Add(self.ListFutureMode, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_11, 1, 0, 0)
        grid_sizer_1.Add(self.CImperative, 0, wx.LEFT, 0)
        grid_sizer_1.Add(self.CAllTense, 0, wx.LEFT, 0)
        sizer_9.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_8.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_8.Add(self.grid_1, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_RIGHT, 0)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_6, 1, 0, 0)
        self.SetSizer(sizer_5)
        sizer_5.Fit(self)
        self.Layout()
        # end wxGlade
    def SetVerb(self, event): # wxGlade: MyFrame2.<event_handler>
        self.verb=self.BoxVerb.Value;

    def SetTransitive(self, event): # wxGlade: MyFrame2.<event_handler>
        self.transitive=True;

    def SetActiveFuture(self, event): # wxGlade: MyFrame2.<event_handler>
        self.listetenses.append(TenseFuture)

    def SetActivePaste(self, event): # wxGlade: MyFrame2.<event_handler>
        self.listetenses.append(TensePast)

    def SetRoot(self, event): # wxGlade: MyFrame2.<event_handler>
        self.root=self.TRoot.Value;

    def SetPassiveFuture(self, event): # wxGlade: MyFrame2.<event_handler>
        self.listetenses.append(TensePassiveFuture)

    def SetPassivePast(self, event): # wxGlade: MyFrame2.<event_handler>
        self.listetenses.append(TensePassivePast)

    def SetImperative(self, event): # wxGlade: MyFrame2.<event_handler>
        self.listetenses.append(TenseImperative)

    def SetAllTense(self, event): # wxGlade: MyFrame2.<event_handler>
        self.listetenses=[TensePassiveFuture,TenseFuture,TenseImperative,TensePassivePast,TensePast]

    def ConjugateOneVerb(self, event): # wxGlade: MyFrame2.<event_handler>
##        self.TConjugation.Value=self.BoxVerb.Value;
        self.verb=self.BoxVerb.Value;
        self.verb_obj=verbclass(self.verb,self.root,self.transitive,self.future_type,self.bab_sarf);
        self.verb_obj.verb_class();
        self.verb_obj.conjugate_all_tenses(self.listetenses);
        self.listetenses=[TensePast,TensePassivePast,TenseFuture,TensePassiveFuture,TenseImperative]
##        self.TConjugation.Value=self.verb_obj.conj_display.display_gui(self.listetenses);
##        self.verb_obj.conj_display.display_html(self.listetenses);
##        self.TConjugation.AppendText("verb"+self.verb+"\troot:"+self.root+"\tfuture_tyep:"+self.future_type)
##        self.verb_obj.conj_display.display_grid(self.GridConjugation,self.listetenses);
        table=self.verb_obj.conj_display.display_table(self.listetenses);
        for i in range(14):
            for j in range(6):
                self.grid_1.SetCellValue(i,j,table[i][j])

# end of class MyFrame2


