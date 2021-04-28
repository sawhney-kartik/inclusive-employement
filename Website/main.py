from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/microsoft")
def languages():
    return render_template("microsoft.html")


# @app.route("/card/<int: index>")
# def card_view(index):
#     card = db[index]
#     return render_template("card.html", card=card)