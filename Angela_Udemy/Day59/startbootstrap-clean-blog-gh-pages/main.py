from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/post")
def blog():
    return render_template("post.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

if __name__ == "__main__":
    app.run(debug=True)
