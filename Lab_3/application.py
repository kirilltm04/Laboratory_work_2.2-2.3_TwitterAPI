from flask import Flask, request, render_template
import map_maker as mp

app = Flask(__name__)


@app.route("/")
def name():
    """
    Rendering the HTML file
    """
    return render_template('index.html')


@app.route("/create/map", methods=["GET", "POST"])
def get():
    """
    Getting the username and amount of friends
    """
    dom = request.form.get("domain")
    num = request.form.get("amount")
    return mp.main(dom, num)


if __name__ == "__main__":
    app.run(debug=True)
