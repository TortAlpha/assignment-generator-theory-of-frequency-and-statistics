import wx

class View(wx.Frame):
    def __init__(self, parent, title):
        super(View, self).__init__(parent, title=title, size=(700, 500))
        
        self.panel = wx.Panel(self)
        self.checkboxes = []
        self.initUI()
        
        self.SetSize((400, 300))
        
    def initUI(self):
        vbox1 = wx.BoxSizer(wx.VERTICAL) #9 заданий
        vbox2 = wx.BoxSizer(wx.VERTICAL) #9 заданий
        
        for i in range(9):
            cb1 = wx.CheckBox(self, label=f"checkbox {i}")    
            cb2 = wx.CheckBox(self, label=f"checkbox {9 + i}")    
            
            self.checkboxes.append(cb1)
            self.checkboxes.append(cb2)
            
            vbox1.Add(cb1, 0, wx.All|wx.EXPAND, 5)
            vbox2.Add(cb1, 150, wx.All|wx.EXPAND, 5)

        self.SetSizer(vbox1)
        