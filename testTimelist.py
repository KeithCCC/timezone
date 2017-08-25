from datetime import datetime, tzinfo, timedelta
import pytz
import numpy as np

def BuildTimezoneList(time1st):
    #time.strftime("%m/%d %H:%M")
    timelist = [time1st]
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st)
    return timelist


tz_tokyo = pytz.timezone('Asia/Tokyo')
timetokyo=datetime.now(tz_tokyo)
Tokyolist = BuildTimezoneList(timetokyo)
tz_sp = pytz.timezone('US/Eastern')
timesp=datetime.now(tz_sp)
splist = BuildTimezoneList(timesp)

#for j in ondaytimelist:
#    print(j)

a = np.array(Tokyolist)
a = np.append(a, splist)
