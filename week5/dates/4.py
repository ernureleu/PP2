from datetime import datetime, timedelta, time

date1 = datetime.strptime("21 December 2004, 07:00:00", "%d %B %Y, %H:%M:%S") 
date2 = datetime.now() 


def diff(d2, d1):
   
    t = d2 - d1 

    return (t.days * 24 * 60 * 60 + t.seconds)

print(f'seconds: {diff(date2, date1)}')