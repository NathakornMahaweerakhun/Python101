from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #program main page
GUI.title ('informationprogram') #program name
GUI.geometry('500x400') #program size

L1 = Label(GUI,text='knowledgeprogram',font=('Angsana New',30),fg='blue')
L1.place(x=30,y=20)
##################################
def Button2():
    text = '300bahtinbankaccount'
    messagebox.showinfo('moneyinbank',text)

FB1 = Frame(GUI) #similar to whiteboard
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='showmoney',command=Button2)
B2.pack(ipadx=20,ipady=20)
###################################

def Button3():
    text = 'Python 101, Math'
    messagebox.showinfo('learn on tuesday',text)

FB2 = Frame(GUI) #similar to whiteboard
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='learningsubject',command=Button3)
B3.pack(ipadx=20,ipady=20)


GUI.mainloop()
