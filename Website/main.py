from flask import Flask, render_template
from django.http import HttpResponseRedirect

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def welcome():
    return render_template("welcome.html")


@app.route("/microsoft/", methods=['POST', 'GET'])
def microsoft():
    return render_template("microsoft_tabs/mission.html")


@app.route("/microsoft/mission/", methods=['POST', 'GET'])
def microsoft_mission():
    return render_template("microsoft_tabs/mission.html")


@app.route("/microsoft/erg/", methods=['POST', 'GET'])
def microsoft_erg():
    return render_template("microsoft_tabs/erg.html")


@app.route("/microsoft/twitter/", methods=['POST', 'GET'])
def microsoft_twitter():
    return render_template("microsoft_tabs/twitter.html")


@app.route("/microsoft/employee/", methods=['POST', 'GET'])
def microsoft_employee():
    return render_template("microsoft_tabs/employee.html")


@app.route("/microsoft/ratings/", methods=['POST', 'GET'])
def microsoft_ratings():
    return render_template("microsoft_tabs/ratings.html")


@app.route("/microsoft/dei/", methods=['POST', 'GET'])
def microsoft_dei():
    return render_template("microsoft_tabs/dei.html")


@app.route("/microsoft/questions/", methods=['POST', 'GET'])
def microsoft_questions():
    return render_template("microsoft_tabs/questions.html")


@app.route("/intel", methods=['POST', 'GET'])
def intel():
    return render_template("intel.html")


@app.route("/cisco", methods=['POST', 'GET'])
def cisco():
    return render_template("cisco.html")