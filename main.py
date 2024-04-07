import wx

class CheckboxPanel(wx.Panel):
    def __init__(self, parent):
        super(CheckboxPanel, self).__init__(parent)
        
        self.checkboxes = []  # Список для хранения чекбоксов
        self.initUI()
    
    def initUI(self):
        # Создание вертикального бокс-сайзера для упорядочивания чекбоксов
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Добавление 13 чекбоксов в бокс-сайзер
        for i in range(1, 14):
            cb = wx.CheckBox(self, label=f"Чекбокс {i}")
            self.checkboxes.append(cb)
            vbox.Add(cb, 0, wx.ALL|wx.EXPAND, 5)
        
        self.SetSizer(vbox)

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        
        panel = CheckboxPanel(self)
        self.SetTitle("13 Чекбоксов")
        self.SetSize((300, 400))

# Создание приложения и главного окна
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
