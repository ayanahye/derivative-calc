from flask import Flask, request, render_template, url_for
from second import second
from sympy import *
from sympy.abc import x,y

app = Flask(__name__)
app.register_blueprint(second)

@app.route("/home")
@app.route("/index.html")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/instructions.html")
@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/about.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/answer', methods = ['POST', 'GET'])
def answer():
    if request.method == 'GET':
        return "The url is accessed directly try going to /answer to submit."
    if request.method == "POST":
        equation = request.form.get("equation")
    
        try:
            answer = diff(equation)
        except:
            answer = "Sorry this cannot be computed please review the instructions tab for support."
        
        return render_template("index.html", answer=answer)


if __name__ == "__main__":
    # i love python with all my heart mate
    app.run(debug=True)
