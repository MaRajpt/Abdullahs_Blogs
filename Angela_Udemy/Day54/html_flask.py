from flask import Flask

app = Flask(__name__)       # __name__ is built in attribute  in python, ist executing code in


@app.route("/")     # "/"  is homepage eg  google.com/    @app is python decorator ( gives additional functional to existinf function)
def hello_world():          # CHECK DECORATOR FILE
    return '<h1 style="text-align : center">Hello, World!</h1>' \
           '<p> paragraphs</p>'

def make_bold(function):
    def wrapper():
        return f'<b><i><u><e>{function()}</e></u></i></b>'
    return wrapper

# Diffrent routes using the app.route decorator
@app.route("/bye")
@make_bold
def say_bye():
    return "bye"









if __name__ == "__main__":      # does same as using terminal to run

    app.run(debug=True)