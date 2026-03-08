from flask import Flask,render_template,request

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

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"<h1>Name: {name}, Email: {email}</h1>"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)