from flask import Flask,  render_template, request, url_for, redirect, flash, send_from_directory
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import werkzeug


app = Flask(__name__)

app.config['SECRET_KEY'] = 'crt3f9py#drr5u7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD-FOLDER'] = 'static'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        data = request.form
        password = data['password']
        secure_password = werkzeug.security.generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        user = User(
                    email=data['email'],
                    name=data['name'],
                    password=secure_password
        )
        with app.app_context():
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        data = request.form
        user_email = data['email']
        user_password = data['password']

        try:
            with app.app_context():
                user = db.one_or_404(db.select(User).filter_by(email=user_email))
            db.session.commit()
        except:
            # Handle the error - e.g. flash a message to the user
            flash('Email incorrect, please try again.')
            return redirect(url_for('login'))
        if not check_password_hash(user.password, user_password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return render_template("secrets.html", logged_in=True)

        #
        # if not user:
        #     flash('THe email address is wong !')
        #     result = db.session.execute(select(User).where(User.email == user_email)).scalar()
        #     if not werkzeug.security.check_password_hash(result.password, user_password):

    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    pass

@app.route('/download')
@login_required
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf", as_attachment=False)
    # return send_from_directory(app.config['UPLOAD-FOLDER'], 'static/files/cheat_sheet.pdf', as_attachment=False)
    # return send_from_directory('static', name='cheat_sheet.pdf', path='files/cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)
