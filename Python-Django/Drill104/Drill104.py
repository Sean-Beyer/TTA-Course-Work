
import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('FileTypes.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        File_Name TEXT \
        )")
    conn.commit()    

with conn:
    for item in fileList:
        if item.endswith('txt'):
            cur.execute("INSERT INTO tbl_files(File_Name) VALUES (?)" \
                 ,(item,))
        conn.commit()
cur.execute("SELECT File_Name FROM tbl_files")
msg = cur.fetchall()
print('txt files in db'+str(msg))
conn.commit()
conn.close()
