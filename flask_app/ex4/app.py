from flask import Flask, render_template, session, redirect, flash, url_for
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    grade = StringField('grade', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    import pdb
    pdb.set_trace()
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        print(dir(form))
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/physics')
def physics_page():
    return render_template(
       'physics.html', current_time=datetime.datetime.now() 
    )

@app.route('/maths')
def maths_page():
    return render_template(
       'maths.html', current_time=datetime.datetime.now() 
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
