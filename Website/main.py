from flask import Flask, render_template

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


@app.route("/microsoft/employee/", methods=['POST', 'GET'])
def microsoft_employee():
    return render_template("microsoft_tabs/employee.html")


@app.route("/microsoft/ratings/", methods=['POST', 'GET'])
def microsoft_ratings():
    return render_template("microsoft_tabs/ratings.html")


@app.route("/microsoft/hiring/", methods=['POST', 'GET'])
def microsoft_hiring():
    return render_template("microsoft_tabs/hiring.html")


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


@app.route("/intel/employee/", methods=['POST', 'GET'])
def intel_employee():
    return render_template("intel_tabs/employee.html")


@app.route("/intel/ratings/", methods=['POST', 'GET'])
def intel_ratings():
    return render_template("intel_tabs/ratings.html")


@app.route("/intel/hiring/", methods=['POST', 'GET'])
def intel_hiring():
    return render_template("intel_tabs/hiring.html")


@app.route("/intel/questions/", methods=['POST', 'GET'])
def intel_questions():
    return render_template("intel_tabs/questions.html")


# Cisco Tabs


@app.route("/cisco/", methods=['POST', 'GET'])
def cisco():
    return render_template("cisco_tabs/mission.html")


@app.route("/cisco/mission/", methods=['POST', 'GET'])
def cisco_mission():
    return render_template("cisco_tabs/mission.html")


@app.route("/cisco/erg/", methods=['POST', 'GET'])
def cisco_erg():
    return render_template("cisco_tabs/erg.html")


@app.route("/cisco/employee/", methods=['POST', 'GET'])
def cisco_employee():
    return render_template("cisco_tabs/employee.html")


@app.route("/cisco/ratings/", methods=['POST', 'GET'])
def cisco_ratings():
    return render_template("cisco_tabs/ratings.html")


@app.route("/cisco/hiring/", methods=['POST', 'GET'])
def cisco_hiring():
    return render_template("cisco_tabs/hiring.html")


@app.route("/cisco/questions/", methods=['POST', 'GET'])
def cisco_questions():
    return render_template("cisco_tabs/questions.html")

