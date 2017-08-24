from datetime import datetime, tzinfo, timedelta
import pytz
import numpy as np

def BuildTimezoneList(time1st):
    #time.strftime("%m/%d %H:%M")
    timelist = [time1st.strftime("%m/%d (%a) %H:%M")]
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st.strftime("%m/%d (%a) %H:%M"))
    return timelist

tz_tokyo = pytz.timezone('Asia/Tokyo')
cat1list=BuildTimezoneList(datetime.now(tz_tokyo))
tz_sp = pytz.timezone('US/Eastern')
cat2list=BuildTimezoneList(datetime.now(tz_sp))


