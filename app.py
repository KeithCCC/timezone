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
    cat1now=datetime.now(tz_tokyo).strftime("%m/%d %H:%M")
    cat2now=datetime.now(tz_sp).strftime("%m/%d %H:%M")
    cat3now=datetime.now(tz_paris).strftime("%m/%d %H:%M")
    timenow=datetime.now().strftime("%m/%d %H:%M")
    return render_template('cattime3.html',cat1=cat1now,cat2=cat2now,cat3=cat3now,timenow=timenow)

@app.route("/<timezone>")
def hello(timezone=None):
    TZtime = datetime.utcnow()
    return render_template('timezone.html',timezone=timezone, TZtime=TZtime)


@app.route("/test/")
def template_test():
    return render_template('timejs.html')


if __name__ == '__main__':
    app.run(debug=True)

