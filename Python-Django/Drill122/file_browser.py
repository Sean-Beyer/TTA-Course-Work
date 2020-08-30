#
# Python:   3.8.1
#
# Author:   Sean Beyer
#
# Purpose:  Drill 122 - Check Files


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

        self.varFile = StringVar()
        self.varFile2 = StringVar()
        

        self.btnBrowse = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse.grid(row=0, column=0, padx=(20,15), pady=(60,0),sticky=W)

        self.txtFile = Entry(self.master,text=self.varFile)
        self.txtFile.grid(row=0, column=1, columnspan=7, padx=(20,0), pady=(60,0), sticky=W+E)

        self.btnBrowse = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse.grid(row=1, column=0, padx=(20,15), pady=(10,0), sticky=W)

        self.txtFile2 = Entry(self.master,text=self.varFile2)
        self.txtFile2.grid(row=1, column=1, columnspan=7, padx=(20,0), pady=(10,0), sticky=W+E)
        

        self.btnCheck = Button(self.master, text="Check for files...", width=15, height=2)
        self.btnCheck.grid(row=2, column=0, padx=(20,0), pady=(10,0), sticky=S+W)

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=6, padx=(200,0), pady=(0,0))


    def cancel(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
