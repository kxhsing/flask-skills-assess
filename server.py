from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "apply-to-karen-corp"

POSITIONS = ["Software Engineer", "QA Engineer", "Product Manager"]

@app.route("/")
def index():
    """Return index.html"""

    return render_template("index.html")

@app.route("/application-form", methods=["POST"])
def application_form():
    """Display application form for users to fill out"""

    return render_template("application-form.html", positions=POSITIONS)


@app.route("/application-success", methods=["POST"])
def application_success():
    """Tell applicant their application was a success and display what they submitted"""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    position = request.form.get("position")
    salary = float(request.form.get("salary"))

    salary = "${:,.2f}".format(salary)
    if ".00" in salary:
        salary = salary[:-3]

    return render_template("application-response.html", 
                            firstname=firstname, 
                            lastname=lastname, 
                            salary=salary,
                            position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
