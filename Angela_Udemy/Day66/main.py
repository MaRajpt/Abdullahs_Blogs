from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, func, update

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = 'asd6dasdasd23Siasf34efdsfe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
top_secret_key = 'abcd1234#'


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/random')
def random_cafe():
    num = 3
    with app.app_context():
        result = db.session.execute(select(Cafe).where(Cafe.id == num)).first()
        for i in result:
            cafe_json = jsonify(name=i.name,
                                map_url=i.map_url,
                                img_url=i.img_url,
                                location=i.location,
                                seats=i.seats,
                                has_toilet=i.has_toilet,
                                has_wifi=i.has_wifi,
                                has_sockets=i.has_sockets,
                                can_take_calls=i.can_take_calls,
                                coffee_price=i.coffee_price)
        db.session.commit()
    return cafe_json


@app.route('/all')
def all_cafes():
    with app.app_context():
        all_cafes = []
        cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars()
        for i in cafes:
            cafe = dict(name=i.name,
                                map_url=i.map_url,
                                img_url=i.img_url,
                                location=i.location,
                                seats=i.seats,
                                has_toilet=i.has_toilet,
                                has_wifi=i.has_wifi,
                                has_sockets=i.has_sockets,
                                can_take_calls=i.can_take_calls,
                                coffee_price=i.coffee_price)
            all_cafes.append(cafe)
        db.session.commit()
    return jsonify(all_cafes)


@app.route('/search')
def search():
    search = request.args.get('loc')
    searches = []
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars()
        for i in cafes:
            if i.location.lower() == search.lower():
                 cafe = dict(name=i.name,
                        map_url=i.map_url,
                        img_url=i.img_url,
                        location=i.location,
                        seats=i.seats,
                        has_toilet=i.has_toilet,
                        has_wifi=i.has_wifi,
                        has_sockets=i.has_sockets,
                        can_take_calls=i.can_take_calls,
                        coffee_price=i.coffee_price)
                 searches.append(cafe)
    db.session.commit()
    if len(searches) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    else:
        return jsonify(searches)

@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(name=request.form.get('name'),
                        map_url=request.form.get('map_url'),
                        img_url=request.form.get('img_url'),
                        location=request.form.get('location'),
                        seats=request.form.get('seats'),
                        has_toilet=bool(int(request.form.get('has_toilet'))),
                        has_wifi=bool(int(request.form.get('has_wifi'))),
                        has_sockets=bool(int(request.form.get('has_sockets'))),
                        can_take_calls=bool(int(request.form.get('can_take_calls'))),
                        coffee_price=request.form.get('coffee_price'))
    with app.app_context():
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response={"success": "New cafe added."})

@app.route('/update/<cafe_id>', methods=['PATCH'])
def edit(cafe_id):
    new_name = request.args.get('new_name')
    with app.app_context():
        user = db.session.execute(update(Cafe).where(Cafe.id == int(cafe_id)).values(name=new_name))
        user.verified = True
        db.session.commit()
    return jsonify(response={"success": "New name added."})


@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def remove(cafe_id):
    secret_key = request.args.get('api_key')
    if secret_key == top_secret_key:
        with app.app_context():
            cafe = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe)
            db.session.commit()
        return jsonify(response={"success": "New name added."})



## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
