#
# Python:   3.8.1
#
# Author:   Sean Beyer
#
# Purpose:  HTML 2


import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(480, 180))
        self.master.title('Check Files')
        self.master.config(bg='#f0f0f0')

        self.varContent = StringVar()
        

        self.lblText = Label(self.master, text="Enter Content:", width=15, height=1)
        self.lblText.grid(row=0, column=0, padx=(20,15), pady=(60,0),sticky=W)

        self.txtContent = Entry(self.master,text=self.varContent)
        self.txtContent.grid(row=0, column=1, columnspan=7, padx=(20,0), pady=(60,0), sticky=W+E)
        

        self.btnSubmit = Button(self.master, text="Submit", width=15, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=0, padx=(20,0), pady=(10,0), sticky=S+W)

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=6, padx=(200,0), pady=(0,0))

    def submit(self):
        html1 = '<html><body>'
        html2 = '</html></body>'
        Content = self.varContent.get()
        print(Content)
        f = open('webpage.html','x')

        message = "{} {} {}".format(html1,Content,html2)

        f.write(message)
        f.close()


    def cancel(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
