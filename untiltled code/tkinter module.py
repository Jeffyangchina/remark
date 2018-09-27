#!usr/bin/env python
# -*- coding：UTF-8-*-
import tkinter as tkt
import types
import string
def DummyCommand():
    pass
scrollbarWidth=20
def pp():
    a=OkCancelWindow(root,'really cancel')
   # b=a.go()
    #print (b)

class OkCancelButtons(tkt.Frame):
    def __init__(self,Master,okcnf={},cancelcnf={}):#按钮有名字并且可以跳转程序
        tkt.Frame.__init__(self,Master)

        self.pack(expand='yes',fill='both')
        if 'text' not in okcnf:
            okcnf['text']='Ok'
        if 'text' not in cancelcnf:
            cancelcnf['text']='Cancel'
        if 'command' not in okcnf:
            okcnf['commmand']=DummyCommand()
        if 'command' not in cancelcnf:
            cancelcnf['commmand']=DummyCommand()
        self._cancelBtn=tkt.Button(self,cancelcnf,fg='red',bg='brown')
        self._cancelBtn.pack(side='right')
        self._okBtn = tkt.Button(self, okcnf, fg='blue')
        self._okBtn.pack(side='left')
class OkCancelWindow(tkt.Frame):
    def __init__(self,Master,Text,Label='Are U sure?',ytcnf={},ntcnf={}):
        tkt.Frame.__init__(self,Master)
        self.pack()
        self._top=tkt.Toplevel(Master)
        self._top.title(Label)
        ytcnf['command']=self.okBtn
        ntcnf['command']=self.noBtn
        self.createWindow(self._top,Text,ytcnf,ntcnf)
    def go(self):
        self._top.grab_set()
        try:
            self._top.mainloop()
        except SystemExit:
            self._top.destroy()
    def createWindow(self,Master,Text,ytcnf,ntcnf):
        Master.geometry('300x200')
        self._text=tkt.Label(Master,text=Text)
        self._text.pack(side='top',fill='x')
    def okBtn(self):
        raise SystemExit
    def noBtn(self):
        raise SystemExit
class ScrolledText(tkt.Frame):#文本框和滚动条框架，get获得文本内容
    def __init__(self,Master,txtcnf={},sbcnf={}):
        tkt.Frame.__init__(self,Master)
        self.pack()
        self._textArea=tkt.Text(self,txtcnf,bg='blue',fg='red')
        frame=tkt.Frame(bg='white').pack(expand='yes',fill='both')
        self._textArea.pack(side='left',fill='both',expand='yes')
        if 'width' not in sbcnf:
            sbcnf['width']=scrollbarWidth
        self._scrollbar=tkt.Scrollbar(self,sbcnf)
        #self._scrollba
        self._scrollbar.pack(side='right',fill='y',expand='yes')
        self._textArea['yscrollcommand']=(self._scrollbar,'set')#滚动条与文本框绑定
        self._scrollbar['command']=(self._textArea,'yview')
    def set(self,text):
        self._textArea.delete('1.0',tkt.END)
        self._textArea.insert(tkt.END,text)
    def get(self):
        return self._textArea.get('1.0',tkt.END)

class LabelEntry(tkt.Frame):
    def __init__(self,Master,Text,lblcnf={},txtcnf={}):
        tkt.Frame.__init__(self,Master)
        self.pack()
        lblcnf['text']=Text
        self._label=tkt.Label(self,lblcnf,bg='red',font=('Arial',10))
        self._label.pack(side='left',expand='no')
        self._entry=tkt.Entry(self,txtcnf)
        #self._entry.bind('<Return>',pp)
        self._entry.pack(side='right',expand='yes',fill='x')
    def empty(self):
        return self._entry.delete(0,tkt.END)
    def get(self):
        return self._entry.get()
    def set(self,Value=' '):
        self.empty()
        self._entry.insert(tkt.END,Value)
    def bind(self,Event,Callback):
        self._entry.bind(Event,Callback)

def test1():
    aa=root.entry.get()
    bb=root.txt.get()
    root.txt.set(aa)
    root.txt2.set(bb)


root=tkt.Tk()
#frame=tkt.Frame(background='blue')

root.entry=LabelEntry(root,'Enter')
#root.entry.bind('',pp)
test=OkCancelButtons(Master=root,okcnf={'command':test1},cancelcnf={'command':pp})
root.txt=ScrolledText(root)
root.txt.set('yang1230')
root.txt2=ScrolledText(root,{'relief':'sunken','width':20},{'width':20})
root.mainloop()
