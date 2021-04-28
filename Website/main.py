from flask import Flask, render_template
from django.http import HttpResponseRedirect

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def welcome():
    return render_template("welcome.html")


@app.route("/microsoft", methods=['POST', 'GET'])
def microsoft():
    return render_template("microsoft.html")


@app.route("/intel", methods=['POST', 'GET'])
def intel():
    return render_template("intel.html")


@app.route("/cisco", methods=['POST', 'GET'])
def cisco():
    return render_template("cisco.html")