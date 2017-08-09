from flask import Flask
from flask import render_template
from datetime import datetime, tzinfo
import pytz

app = Flask(__name__)

@app.route("/")
def cattime():
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_sp = pytz.timezone('US/Eastern')
    tz_paris = pytz.timezone('Europe/Paris')
    cat1now=datetime.now(tz_tokyo).strftime("%m/%d %H:%M:%S")
    cat2now=datetime.now(tz_sp).strftime("%m/%d %H:%M:%S")
    cat3now=datetime.now(tz_paris).strftime("%m/%d %H:%M:%S")
    timenow=datetime.now().strftime("%m/%d %H:%M:%S")
    return render_template('cattime2.html',cat1=cat1now,cat2=cat2now,cat3=cat3now,timenow=timenow)

@app.route("/<timezone>")
def hello(timezone=None):
    TZtime = datetime.utcnow()
    return render_template('timezone.html',timezone=timezone, TZtime=TZtime)
