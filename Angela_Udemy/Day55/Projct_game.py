from flask import Flask
import random

rand_num = random.randint(0,10)

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<h1 style='text-align: center'>Guess the the number between 0 to 10 ?</h1>" \
           "<p style='text-align: center'><img style='item-align: center' src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'  width='500' height='600'></p>"


@app.route("/<int:number>")
def user_input(number):
    if number > rand_num:
        return "<h1 style='text-align: center'>Too HIGH !</h1>" \
           "<p style='text-align: center'><iframe src='https://giphy.com/embed/3o7abAHdYvZdBNnGZq' width='480' height='480' frameBorder='0' class='giphy-embed' allowFullScreen></iframe><p><a href='https://giphy.com/gifs/dog-puppy-dottie-3o7abAHdYvZdBNnGZq'></a></p></p>"
    elif number < rand_num:
        return "<h1 style='text-align: center'>Too LOW !</h1>" \
           "<p style='text-align: center'><iframe src='https://giphy.com/embed/URoLoCo1s9jm8' width='480' height='313' frameBorder='0' class='giphy-embed' allowFullScreen></iframe><p><a href='https://giphy.com/gifs/dog-puppy-URoLoCo1s9jm8'></a></p></p>"
    else:
        return "<h1 style='text-align: center'>YOU GOT IT !</h1>" \
           "<p style='text-align: center'><iframe src='https://giphy.com/embed/4T7e4DmcrP9du' width='458' height='480' frameBorder='0' class='giphy-embed' allowFullScreen></iframe><p><a href='https://giphy.com/gifs/puppy-biscuit-emerging-4T7e4DmcrP9du'></a></p></p>"

print(rand_num)

if __name__ == "__main__":
    app.run(debug=True)

