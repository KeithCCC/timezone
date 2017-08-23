from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, tzinfo, timedelta
import pytz

app = Flask(__name__)
Bootstrap(app)

def BuildTimezoneList(time1st):
    #time.strftime("%m/%d %H:%M")
    timelist = [time1st.strftime("%m/%d (%a) %H:%M")]
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st.strftime("%m/%d (%a) %H:%M"))
    return timelist

@app.route("/")
def index():
    return render_template('test.html')

@app.route("/div")
def CatTimeDiv():
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_sp = pytz.timezone('US/Eastern')
    tz_paris = pytz.timezone('Europe/Paris')
    cat1list=BuildTimezoneList(datetime.now(tz_tokyo))

    cat2list=BuildTimezoneList(datetime.now(tz_sp))
    cat3list=BuildTimezoneList(datetime.now(tz_paris))
    timenow=datetime.now().strftime("%m/%d %H:%M")
    return render_template('TZ_div.html',cat1=cat1list,cat2=cat2list,cat3=cat3list,timenow=timenow)

@app.route("/tbl")
def CatTimeTbl():
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_sp = pytz.timezone('US/Eastern')
    tz_paris = pytz.timezone('Europe/Paris')
    cat1list=BuildTimezoneList(datetime.now(tz_tokyo))

    cat2list=BuildTimezoneList(datetime.now(tz_sp))
    cat3list=BuildTimezoneList(datetime.now(tz_paris))
    timenow=datetime.now().strftime("%m/%d %H:%M")
    return render_template('TZ_table1.html',cat1=cat1list,cat2=cat2list,cat3=cat3list,timenow=timenow)

@app.route("/tbl1")
def CatTimeTbl1():
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_sp = pytz.timezone('US/Eastern')
    tz_paris = pytz.timezone('Europe/Paris')
    cat1list=BuildTimezoneList(datetime.now(tz_tokyo))

    cat2list=BuildTimezoneList(datetime.now(tz_sp))
    cat3list=BuildTimezoneList(datetime.now(tz_paris))
    timenow=datetime.now().strftime("%m/%d %H:%M")
    return render_template('TZ_table.html',cat1=cat1list,cat2=cat2list,cat3=cat3list,timenow=timenow)




if __name__ == '__main__':
    app.run(debug=True)
