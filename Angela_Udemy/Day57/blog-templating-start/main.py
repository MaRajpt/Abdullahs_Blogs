from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url)
response.raise_for_status()
data = response.json()



@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route('/blog/<int:num>')
def blog(num):
    return render_template("post.html", numb=num, posts=data)

if __name__ == "__main__":
    app.run(debug=True)
