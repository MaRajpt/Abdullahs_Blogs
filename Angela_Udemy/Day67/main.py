from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, update
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    with app.app_context():
        # requested_post = db.session.execute(select(BlogPost).where(BlogPost.id == index)).first()
        requested_post = db.get_or_404(BlogPost, index)

        post_structure = dict(id=requested_post.id,
                        title=requested_post.title,
                        subtitle=requested_post.subtitle,
                        date=requested_post.date,
                        body=requested_post.body,
                        author=requested_post.author,
                        img_url=requested_post.img_url)
        db.session.commit()
        print(requested_post.title)
    return render_template("post.html", post=post_structure)


@app.route('/add', methods=['GET','POST'])
def new_post():
    add_form = CreatePostForm()
    x = datetime.datetime.now()

    if add_form.validate_on_submit():
        add_post = BlogPost(
                    title=add_form.title.data,
                    subtitle=add_form.subtitle.data,
                    author=add_form.author.data,
                    img_url=add_form.img_url.data,
                    body=add_form.body.data,
                    date=f"{x.strftime('%B')} {x.day}, {x.year}")
        with app.app_context():
            db.session.add(add_post)
            db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=add_form, edit=False)


@app.route('/edit/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    selected_post = db.get_or_404(BlogPost, post_id)

    edit_form = CreatePostForm(
        title=selected_post.title,
        subtitle=selected_post.subtitle,
        img_url=selected_post.img_url,
        author=selected_post.author,
        body=selected_post.body)

    if edit_form.validate_on_submit():
        with app.app_context():
            user = db.session.execute(update(BlogPost).where(BlogPost.id == post_id).values(
                title=edit_form.title.data,
                subtitle=edit_form.subtitle.data,
                author=edit_form.author.data,
                img_url=edit_form.img_url.data,
                body=edit_form.body.data))
            user.verified = True
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', edit=True, form=edit_form)

@app.route('/delete/<int:delete_id>')
def del_post(delete_id):
    with app.app_context():
        deleted_post = db.get_or_404(BlogPost, delete_id)
        print(deleted_post.title)
        db.session.delete(deleted_post)
        db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)