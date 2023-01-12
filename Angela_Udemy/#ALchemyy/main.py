from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update, select, func

db = SQLAlchemy()

app = Flask(__name__)
#only thing from app is required is URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = 'asd6dasdasd23Siasf34efdsfe'
db.init_app(app)

# db.Model  creates the model or look of the table ###############################

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200),  nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

#///// creating tables
# with app.app_context():
#     db.create_all()



# # ////////////////////////////////////////////  ADDING USERS INTO TABLE /////////////////////////////////////////
# user = User(username='sam',
#             email='sam@gmail.com')
# with app.app_context():
#     db.session.add(user)
#     db.session.commit()

#////////////////////////////////////   INQUIRING USER / MULTIPLE USERS  (WITH)   ////////////////////////////

#///  SQLAlchemy.get_or_404() will raise a 404 if the row with the given id doesn’t exist, otherwise it will return the instance.
#  IF USER ID DOES NOT EXIST RETURNS ERROR, ELSE RETURN USER OBJECT
#      user = db.get_or_404(User, 2)


#/// SQLAlchemy.first_or_404() will raise a 404 if the query does not return any results, otherwise it will return the first result.
#       user = db.first_or_404(db.select(User).filter_by(id=2))  (can also use username  etc. )


#/// SQLAlchemy.one_or_404() will raise a 404 if the query does not return exactly one result, otherwise it will return the result
#  CHECKS IF USER (username , id etc.)  IS UNIQUE IF NOT RETURNS ERROR ELSE RETURN USER INSTANCE.
#     user = db.one_or_404(db.select(User).filter_by(username='sam'))

#//////////////   INQUIRE MULTIPLE USERS  (WITH)

#  users = db.session.execute(select(User).where(User.username == 'sam')).scalars()

# //////////////   INQUIRE ALL USERS  (WITH)

#users = db.session.execute(db.select(User).order_by(User.username)).scalars()

#/////// EXAMPLE
# with app.app_context():
#     user = db.first_or_404(db.select(User).filter_by(id=2))
#     print(user)
#     db.session.commit()



#/////////////////////////////////////////////////    MODIFYING DATA    //////////////////////////////////
# with app.app_context():
#/// METHOD ONE simply use existing syntax
     #user = db.session.execute(update(User).where(User.id == 1).values(username="bill"))

#/// METHOD TWO GET OBJECT OF USER AND SIMPLE ASSIGN NEW VALUE
      # user = db.get_or_404(User, 1)
      # user.username = 'jeff'
      #
      # user.verified = True
      # db.session.commit()


#/////////////////////////////////////////////      DELETING USERS FROM TABLE    //////////////////////////////
#/// just need user instance to delete it wither of above can be used

# with app.app_context():
    # user = db.get_or_404(User, 9)
    # user = db.first_or_404(db.select(User).filter_by(username='sam'))

    # db.session.delete(user)
    # db.session.commit()


#////////////////////////////////////////////////   COUNT ROWS     ///////////////////////////////////////////
# with app.app_context():
#     users = db.session.execute(db.select(func.count(User.id))).scalars()
#     for i in users:
#         print(i)  #   GIVES NUMBER OF ROWS
#     db.session.commit()



# @app.route('/')
# def main_page():
#
#     # users = db.session.execute(db.select(User).order_by(User.id)).scalars()
#     users = db.session.execute(db.select(User).where(User.id == 1)).scalar()  # scalars provide result , if value  not present returns empty, where as one returns one result if not present gives error
#
#     return render_template('index.html', users=users)
#
#
# with app.app_context():
#     userz = db.session.execute(db.select(func.count(User.id))).scalars()
#     user = db.get_or_404(User, 2)
#     for i in userz:
#         print(type(i))  #   GIVES NUMBER OF ROWS
#     print(user)
#     gg = User.query.get(int(1))
#     print(gg)
#     db.session.commit()
#


#
# if __name__ == '__main__':
#     app.run(debug=True)
#
