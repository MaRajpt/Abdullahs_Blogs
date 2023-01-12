from flask import Flask, render_template
import random
import datetime
import requests

dt = datetime.datetime
current_year = dt.today().year
app = Flask(__name__)

@app.route("/")
def main_page():
    random_number = random.randint(1,100)
    # return render_template("jinja_html.html", num=random_number)      # Transferring random int created to HTMl file as **kwarg
    return render_template("index.html")


@app.route("/<name>")
def guess(name):

    name_url = f"https://api.genderize.io?name={name}"
    gender_url = f"https://api.agify.io?name={name}"

    name_response = requests.get(name_url)
    gender_response = requests.get(gender_url)

    name_response.raise_for_status()
    gender_response.raise_for_status()

    data1 = name_response.json()
    data2 = gender_response.json()

    user_gender = data1['gender']
    user_age = data2['age']


    return render_template("jinja_html.html" , gender = user_gender, age = user_age)
if __name__ == "__main__":
    app.run(debug=True)


