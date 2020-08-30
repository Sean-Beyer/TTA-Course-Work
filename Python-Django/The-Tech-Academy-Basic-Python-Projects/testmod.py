import os

os.chdir(r"C:\Users\Seann\Matrix\The-Tech-Academy-Basic-Python-Projects")

with open('test2.txt', 'r') as f:
    data = f.read()
    print(data)
    f.close()
