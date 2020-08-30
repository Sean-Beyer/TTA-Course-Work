#
# Python:   3.8.1
#
# Author:   Sean Beyer
#
# Purpose:  Drill 123 - Check Files


import os
import time 
import shutil
import sqlite3
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory


conn = sqlite3.connect('db_filelog.db')

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        self.varFile = StringVar()
        self.varFile2 = StringVar()


        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(480, 180))
        self.master.title('Check Files')
        self.master.config(bg='#f0f0f0')
        

        self.btnBrowse = Button(self.master, text="Browse...", width=15, height=1, command=self.askdirectory)
        self.btnBrowse.grid(row=0, column=0, padx=(20,15), pady=(60,0),sticky=W)

        self.txtFile = Entry(self.master,text=self.varFile)
        self.txtFile.grid(row=0, column=1, columnspan=7, padx=(20,0), pady=(60,0), sticky=W+E)


        self.btnBrowse = Button(self.master, text="Browse...", width=15, height=1, command=self.askdirectory1)
        self.btnBrowse.grid(row=1, column=0, padx=(20,15), pady=(10,0), sticky=W)

        self.txtFile2 = Entry(self.master,text=self.varFile2)
        self.txtFile2.grid(row=1, column=1, columnspan=7, padx=(20,0), pady=(10,0), sticky=W+E)
        

        self.btnCheck = Button(self.master, text="Check for files...", width=15, height=2, command=self.files)
        self.btnCheck.grid(row=2, column=0, padx=(20,0), pady=(10,0), sticky=S+W)

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=6, padx=(200,0), pady=(0,0))


    def askdirectory(self):
        try:
            name = askdirectory(title='filename')
            self.txtFile.insert(END, name) 
        except:
            print("No file exists")

        
    def askdirectory1(self):
        try:
            name = askdirectory(title='filename')
            self.txtFile2.insert(END, name) 
        except:
            print("No file exists")

    def files(self):
        source = self.txtFile.get()
        print(source)   
        destination = self.txtFile2.get()
        print(destination)
        print(type(destination))
        for file in os.listdir(source):
            print(os.listdir(source))
            if file.endswith(".txt"):
                print(file)
                modification_time = os.path.getmtime(source)
                shutil.move(os.path.join(source, file), destination)  
                print("Last modification time since the epoch:", modification_time)
                self.create_db()
                print(self.create_db())
                with conn:
                    print(conn)
                    cur = conn.cursor()
                    cur.execute("INSERT INTO tbl_filelog(col_filename, col_lastmod) VALUES (?,?)" \
                            ,(file,modification_time))
                    conn.commit()
        conn.close()
                   


    def create_db(self): 
        with conn:
            print(conn)
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_filelog( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_filename TEXT, \
                col_lastmod TEXT \
                    );")
            conn.commit()
        
        
                

    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
