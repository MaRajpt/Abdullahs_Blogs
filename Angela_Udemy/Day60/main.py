from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login", methods=["POST"])    #Notice that the methods parameter accepts a dictionary, so you can have multiple methods targeted by one route. e.g.
def recieve_data():                     # @app.route("/contact", methods=["GET", "POST"]
    name = request.form['username']
    return f"<h1>{name}</h1>"



if __name__ == "__main__":
    app.run(debug=True)

