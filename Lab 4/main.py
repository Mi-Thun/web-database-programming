from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/table/', methods=['GET', "POST"])
def table():
    x = {"name": "John", "age": 30,"city": "New York"}
    return render_template("table.html", **locals())

@app.route('/list/', methods=['GET', "POST"])
def list():
    l = ['Apple', 'Ball', 'Coffee', 'Dog', 'Eight', 'Fix', 'Good']
    return render_template("list.html", **locals())

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5003)
