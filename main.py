from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, tzinfo, timedelta
import pytz

app = Flask(__name__)
Bootstrap(app)
 
def BuildTimezoneList(time1st, label):
    #time.strftime("%m/%d %H:%M")
    timelist = [label]
    timelist.append(time1st.strftime("%m/%d (%a) %H:00"))
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st.strftime("%m/%d (%a) %H:00"))
    return timelist

def BuildTimezoneListnoYear(time1st, label):
    #time.strftime("%m/%d %H:%M")
    timelist = [label]
    timelist.append(time1st.strftime("(%a) %H:00"))
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st.strftime("(%a) %H:00"))
    return timelist

@app.route("/")
def index():
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_van = pytz.timezone('US/Pacific')
    tz_sp = pytz.timezone('US/Eastern')
    tz_paris = pytz.timezone('Europe/Paris')
    cat1list=BuildTimezoneList(datetime.now(tz_tokyo), 'Tokyo')
    cat2list=BuildTimezoneListnoYear(datetime.now(tz_sp), 'St. Pete')
    cat3list=BuildTimezoneListnoYear(datetime.now(tz_paris), 'Paris')
    cat4list=BuildTimezoneListnoYear(datetime.now(tz_van), 'Vancouver')
    timenow=datetime.now().strftime("%m/%d %H:%M")
    return render_template('TZ_t1.html',cat1=cat1list,cat2=cat2list,cat3=cat3list,cat4=cat4list, timenow=timenow)

@app.route("/t")
def codetest():
    l1 = ['L1-1', 'L1-2', 'L1-3','L1-4']
    l2 = ['L2-1', 'L2-2', 'L2-3', 'L2-4']
    l3 = ['L3-1', 'L3-2', 'L3-3' , 'L3-4']
    return render_template('test.html',cat1=l1,cat2=l2,cat3=l3)

if __name__ == '__main__':
    app.run(debug=True)
