from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, update
# import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling', '9.3')")
# db.commit()


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db.init_app(app)
app.config['SECRET_KEY'] = 'asd6dasdasd23Siasf34efdsfe'
Bootstrap(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, unique=True, nullable=False)
    book_author = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

class Bookform(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Editform(FlaskForm):
    new_rating = StringField('New Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    with app.app_context():

        users = db.session.execute(db.select(func.count(Book.id))).scalars()
        for i in users:
            if i == 0:
                return render_template("index.html", books=i)
            else:
                books = db.session.execute(db.select(Book).order_by(Book.id)).scalars()
                return render_template("index.html", books=books)
        db.session.commit()

@app.route("/add", methods=['POST', 'GET'])
def add():
    form = Bookform()
    if form.validate_on_submit():
        name = request.form['name']
        author = request.form['author']
        ratings = request.form['rating']
        user = Book(book_name=name, book_author=author,
                    rating=ratings)
        with app.app_context():
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))

    return render_template("add.html", form=form)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    book_id = request.args.get('book_id')
    rating = request.args.get('rating')

    edit_form = Editform()
    book_name = request.args.get('book_name')
    if edit_form.validate_on_submit():
        new_rating = request.form['new_rating']
        with app.app_context():
            book = db.session.execute(update(Book).where(Book.id == book_id).values(rating=new_rating))
            db.session.commit()
        return home()

    return render_template('edit.html', number=rating, books=book_name, form=edit_form)

@app.route("/delete")
def delete():
    # FOLLOWING LINE IS IMPORTANT THINK ABOUT IT
    book_id = request.args.get('delete_id')
    with app.app_context():
        user = db.get_or_404(Book, book_id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

