import wx
import CheckBoxPanel

class MainPanel(wx.Panel):
    
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        
        #Main titles
        self.mainTitle = wx.StaticText(self, label="Задания формируются согласно варианту №3 типовых расчетов"
                                       , pos=(50, 20))
        
        #CheckBoxes
        self.checkBoxPanel = CheckBoxPanel.CheckBoxPanel(self)

        self.checkBoxPanel.SetPosition((10, 100))
        self.checkBoxPanel.SetSize((500, 500))
        
            #Setting active all checkboxes
        for i in range(18):
            self.checkBoxPanel.checkboxes[i].SetValue(True)
        
        #Count of variants
        self.countVariantsTextBox = wx.TextCtrl(self, pos=(325, 60), size=(30, -1))
        self.countVariantsTextBox.Bind(wx.EVT_TEXT, self.onTextChange)
        
        self.variantsLabel = wx.StaticText(self, label="Введите количество вариантов: ", pos=(120, 62))
        
        self.generateButton = wx.Button(self, label="Сгенерировать варианты и ответы", pos=(100,420), size=(300, 25))
        self.generateButton.Bind(wx.EVT_BUTTON, self.onClickGenerateButton)

        
    def onTextChange(self, event):
        content = self.countVariantsTextBox.GetValue()
        
        if len(content) > 2:
            self.countVariantsTextBox.SetValue(content[:2])
            self.countVariantsTextBox.SetInsertionPointEnd()
        event.Skip() 
        
    def onClickGenerateButton(self, event):
        pass
    
        