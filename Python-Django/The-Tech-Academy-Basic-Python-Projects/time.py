import datetime
import time
import pytz

now = datetime.datetime.now()



pdx = pytz.timezone('US/Pacific')
Portland = now.astimezone(pdx)


nyc = pytz.timezone('US/Eastern')
New_York = now.astimezone(nyc)

lcy = pytz.timezone('Europe/London')
London = now.astimezone(lcy)


if Portland.hour > 9 or Portland.hour < 17:
    print("Portland is Open") 
else:
    print("Portland is Closed")

if New_York.hour > 9 or New_York.hour < 17:
    print("New York is Open") 
else:
    print("New York is Closed")

if London.hour > 9 or London.hour < 17:
    print("London is Open") 
else:
    print("London is Closed")
