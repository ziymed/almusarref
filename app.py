#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Dec 18 10:49:49 2002

import wx
from MyFrame2 import MyFrame2

if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_3 = MyFrame2(None, -1, "")
    app.SetTopWindow(frame_3)
    frame_3.Show()
    app.MainLoop()
