from flask import Flask, render_template, request, make_response, redirect
from flask_bootstrap import Bootstrap
from datetime import datetime, tzinfo, timedelta
import pytz

app = Flask(__name__)
Bootstrap(app)
tzdict = {'Tokyo':'Asia/Tokyo', 
            'St. Pete':'US/Eastern',
            'Tampa':'US/Eastern',
            'Paris':'Europe/Paris', 
            'Vancouver':'US/Pacific'} 

def BuildTimezoneList(time1st, label):
    #time.strftime("%m/%d %H:%M")
    timelist = [label]
    timelist.append(time1st.strftime("%m/%d %a %H:00"))
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st.strftime("%m/%d %a %H:00"))
    return timelist

def BuildTimezoneListnoYear(time1st, label):
    #time.strftime("%m/%d %H:%M")
    timelist = [label]
    timelist.append(time1st.strftime("%a %H:00"))
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st.strftime("%a %H:00"))
    return timelist

@app.route("/")
def index():
    redirect_to_index = redirect('/')
    cities = request.cookies.get('cities')
    if not 'cities' in request.cookies:
        resp = make_response(render_template('index.html'))
        resp.set_cookie('cities', 'Tokyo,Tampa,Paris,Vancouver')
        return resp

    citylist = cities.split(',')
    #cnt = len(citylist)
    cnt = 3
    tzlist = list()
    loopCnt = 0
    for i in citylist:
        if loopCnt == 0:
            tzlist.append(BuildTimezoneList(datetime.now(pytz.timezone(tzdict[i])),i))
        else:
            tzlist.append(BuildTimezoneListnoYear(datetime.now(pytz.timezone(tzdict[i])),i))
        loopCnt +=1

    timenow=datetime.now().strftime("%m/%d %H:%M")
    
    #return render_template('index.html',cat1=cat1list,cat2=cat2list,cat3=cat3list,cat4=cat4list, timenow=timenow, cnt=cnt, tzlist=timezonelist )
    return render_template('index.html',cat1=tzlist[0],cat2=tzlist[1],cat3=tzlist[2],cat4=tzlist[3], timenow=timenow, cnt=cnt, tzlist=citylist )

@app.route("/p")
def mysite():
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_van = pytz.timezone('US/Pacific')
    tz_sp = pytz.timezone('US/Eastern')
    cat1list=BuildTimezoneList(datetime.now(tz_tokyo), 'Tokyo')
    cat2list=BuildTimezoneListnoYear(datetime.now(tz_sp), 'St. Pete')
    cat4list=BuildTimezoneListnoYear(datetime.now(tz_van), 'Vancouver')
    timenow=datetime.now().strftime("%m/%d %H:%M")
    cnt=3
    return render_template('index.html',cat1=cat1list,cat2=cat2list,cat3=cat4list, cat4cat=cat4list,timenow=timenow, cnt=cnt, tzlist='empty' )

@app.route("/setting")
def Setting():
    cities = request.cookies.get('cities')
    citylist = cities.split(',')
    
    return render_template('setting.html',citylist=citylist)

@app.route("/t")
def codetest():
    l1 = ['L1-1', 'L1-2', 'L1-3','L1-4']
    l2 = ['L2-1', 'L2-2', 'L2-3', 'L2-4']
    l3 = ['L3-1', 'L3-2', 'L3-3' , 'L3-4']
    return render_template('test.html',cat1=l1,cat2=l2,cat3=l3)

if __name__ == '__main__':
    app.run(debug=True)
