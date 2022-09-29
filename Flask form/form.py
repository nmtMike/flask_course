from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):
    
    your_name = StringField("What's your name?")
    submit = SubmitField('Click This')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        session['your_name'] = form.your_name.data

        flash(f"Be aware of changing your name, your current name is {session['your_name']}")
        return redirect(url_for('index'))

    return render_template('home_page.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)