from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    new = 123
    return render_template("welcome.html", ab=new)

# @app.route("/languages")
# def languages():
#     return render_template("languages.html")


# @app.route("/card/<int: index>")
# def card_view(index):
#     card = db[index]
#     return render_template("card.html", card=card)