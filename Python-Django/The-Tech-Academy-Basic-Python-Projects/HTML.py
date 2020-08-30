#
# Python:   3.8.1
#
# Author:   Sean Beyer
#
# Purpose:  HTML Write


f = open('sale.html','x')

message = """<html> 
<body> 
Stay tuned for our amazing summer sale! 
</body> 
</html>"""

f.write(message)
f.close()
