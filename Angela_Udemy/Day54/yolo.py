from flask import Flask

app = Flask(__name__)       # __name__ is built in attribute  in python, ist executing code in


@app.route("/")     # "/"  is homepage eg  google.com/    @app is python decorator ( gives additional functional to existinf function)
def hello_world():          # CHECK DECORATOR FILE
    return "<p>Hello, World!</p>"

# Diffrent routes using the app.route decorator
@app.route("/bye")
def say_bye():
    return "bye"

# Creating variable paths and converting the path to specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name} you are {number} years old."


if __name__ == "__main__":      # does same as using terminal to run

    app.run(debug=True)