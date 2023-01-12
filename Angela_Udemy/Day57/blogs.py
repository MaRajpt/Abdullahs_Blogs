from flask import Flask ,render_template
import requests

#------------------------- MULTIPLE statements in jinja -------------#
app = Flask(__name__)

@app.route("/")
def main():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response =  requests.get(url)
    response.raise_for_status()
    data = response.json()

    return render_template("blogs.html", blogs = data)

@app.route("/<num>")
def personal(num):

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

