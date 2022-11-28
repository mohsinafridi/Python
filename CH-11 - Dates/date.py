import datetime as d 
from datetime import timezone as t

x = d.datetime.now()
x_1 = d.MAXYEAR
x_2 = t.utc


print("Current DataTime is : ",x)
print("MAX Year : ",x_1)
print("TIMEZONE : ",x_2)
print("Current DataTime is : ",x.minute)