from flask import render_template, Flask
from flask_wtf import Form
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'development key'
bootstrap = Bootstrap(app)

class NameForm(Form):
 name = StringField('What is your name?', validators=[Required()])
 Pets = RadioField('Pets', choices = [('M','Mie'),('F','Mori'),('K','Kou')])
 submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
 name = None
 radiodata = None
 form = NameForm()
 if form.validate_on_submit():
    name = form.name.data
    radiodata = form.Pets.data
    form.name.data = ''
 return render_template('FTest4.html', form=form, name=name,radio=radiodata)

if __name__ == '__main__':
   app.run(debug = True)