from datetime import datetime, tzinfo, timedelta
import pytz


def BuildTimezoneList(time1st):
    #time.strftime("%m/%d %H:%M")
    timelist = [time1st]
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st)
    return timelist


tz_tokyo = pytz.timezone('Asia/Tokyo')
oneday=datetime.now(tz_tokyo)
ondaytimelist = BuildTimezoneList(oneday)

for j in ondaytimelist:
    print(j)


