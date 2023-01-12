from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app
+
gg= create_app()

gg.config.update(dict(
    SECRET_KEY="asda3#$F#$%",
    WTF_CSRF_SECRET_KEY = 'asd3%53g$#6h4bcf%'
))


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])

@gg.route('/', methods=["POST", "GET"])
def main():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "ma.rajptt@gmail.com":
            return redirect('/success')
    return render_template("index.html", form = form)

if __name__ == '__main__':
    gg.run(debug=True)
