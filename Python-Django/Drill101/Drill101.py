import os
import time

# Open folder
path = r"C:\Users\Seann\Matrix\Drill101"
dirs = os.listdir( path )

# Loop
for file in dirs:
   if file.endswith('.txt'):
       print(file)
       p = (os.path.join(path, file))
       access_time = os.path.getmtime(p) 
       print("Last modification time since the epoch:", access_time)
