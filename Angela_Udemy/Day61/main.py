from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm


def create_app():
  flask = Flask(__name__)
  Bootstrap(flask)

  return flask

app = create_app()

app.config.update(dict(
    SECRET_KEY="asda3#$F#$%",
    WTF_CSRF_SECRET_KEY = 'asd3%53g$#6h4bcf%'
))


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='submit', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST","GET"])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "ma.rajptt@gmail.com":
            return redirect('/success')
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/denied")
def denied():
    return render_template("denied.html")



if __name__ == '__main__':
    app.run(debug=True)