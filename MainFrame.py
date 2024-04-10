import wx
import MainPanel

class View(wx.Frame):
    def __init__(self, parent, title):
        super(View, self).__init__(parent, title=title, size=(500, 500))
        self.SetSizeHints(minW=500, minH=500, maxW=500, maxH=500)
        panel = MainPanel.MainPanel(self)

   