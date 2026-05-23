# jinja2 is a templating engine for Python, which allows you to create dynamic HTML pages by embedding Python code within your HTML templates. In Flask, Jinja2 is the default templating engine, and it provides a powerful way to generate HTML content based on data passed from your Flask routes.

'''
{{ result }} -> this is a variable that we are passing from our Flask route to the Jinja2 template. In this case, we are passing the variable 'result' which contains the value "Pass" or "Fail" based on the score.
{% if result == "Pass" %}
    <h1>Congratulations! You passed the exam.</h1>
{% else %}
    <h1>Sorry! You failed the exam. Better luck next time.</h1>
{% endif %} 

{# This is a comment in Jinja2. It will not be rendered in the final HTML output. #}
'''



from flask import Flask,render_template,request,redirect, url_for
from numpy import exp

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to flask app!</h1></html>"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about",methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"<h1>Name: {name}, Email: {email}</h1>"
    return render_template("form.html")

# variable rule
@app.route('/success/<int:score>', methods=['GET', 'POST'])
def success(score):
    res="Pass" if score >= 50 else "Fail"
    return render_template("success.html", result=res)


@app.route('/successres/<int:score>', methods=['GET', 'POST'])
def successres(score):
    res="Pass" if score >= 50 else "Fail"
    exp={"score":score,"result":res}
    # return render_template("success1.html", **exp)
    return render_template("success1.html", result = exp)

@app.route('/successif/<int:score>', methods=['GET', 'POST'])
def successif(score):
    return render_template("success2.html", score=score)

@app.route('/failif/<int:score>', methods=['GET', 'POST'])
def failif(score):
    return render_template("success2.html", score=score)

    
@app.route('/getresult', methods=['GET', 'POST'])
def get_result():
    total_mark = 0
    if request.method == 'POST':
        math_mark = int(request.form['name'])
        science_mark = int(request.form['email'])
        total_mark = math_mark + science_mark
    else:
        return render_template("getresult.html")
    return redirect(url_for('success', score= total_mark))

if __name__ == "__main__":
    app.run(debug=True)