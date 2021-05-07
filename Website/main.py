from flask import Flask, render_template
from django.http import HttpResponseRedirect

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def welcome():
    return render_template("welcome.html")

# Microsoft Tabs


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

# Intel Tabs


@app.route("/intel/", methods=['POST', 'GET'])
def intel():
    return render_template("intel_tabs/mission.html")


@app.route("/intel/mission/", methods=['POST', 'GET'])
def intel_mission():
    return render_template("intel_tabs/mission.html")


@app.route("/intel/erg/", methods=['POST', 'GET'])
def intel_erg():
    return render_template("intel_tabs/erg.html")


@app.route("/intel/twitter/", methods=['POST', 'GET'])
def intel_twitter():
    return render_template("intel_tabs/twitter.html")


@app.route("/intel/employee/", methods=['POST', 'GET'])
def intel_employee():
    return render_template("intel_tabs/employee.html")


@app.route("/intel/ratings/", methods=['POST', 'GET'])
def intel_ratings():
    return render_template("intel_tabs/ratings.html")


@app.route("/intel/dei/", methods=['POST', 'GET'])
def intel_dei():
    return render_template("intel_tabs/dei.html")


@app.route("/intel/questions/", methods=['POST', 'GET'])
def intel_questions():
    return render_template("intel_tabs/questions.html")


# Cisco Tabs


@app.route("/cisco", methods=['POST', 'GET'])
def cisco():
    return render_template("cisco.html")