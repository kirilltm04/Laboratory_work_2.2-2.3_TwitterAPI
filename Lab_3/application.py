import map_maker
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/name")
def name():
    return "Program to know the location of the Twitter friends."

@app.route("/get_data")
def get():
    map_maker.map_maker("kirilltm04", 10)


if __name__ == "__main__":
    app.run(debug=True, )
