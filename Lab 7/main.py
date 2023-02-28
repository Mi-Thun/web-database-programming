from flask import Flask, request, render_template
import pymongo
app = Flask(__name__)
app.secret_key = 'super secret key'

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["Registration"]
users_details = mydb["users_details"]


@app.route('/registration/', methods=['GET', "POST"])
def registration():
    isPost = False
    if request.method == "POST":
        isPost = True
        user = request.form['username1']
        p1 = request.form['password1']
        p2 = request.form['password2']
        a = users_details.find_one({"username1": user})
        if p1 == p2:
            if a is not None:
                result = 'Enter different user name'
            else:
                users_details.insert_one({'username1': user, 'password1': p1})
                result = "Inserted"
        else:
            result = 'Enter same password'
    return render_template("registration.html", **locals())


@app.route('/', methods=['GET',"POST"])
def login():
    if request.method == "POST":
        name = request.form['username1']
        passw = request.form['p1assword']
        a = users_details.find({"username": name, 'password':passw})
        if a != None:
            result = "Welcome"
        else:
            result = "not match"
    return render_template("login.html", **locals())


if __name__ == "__main__":
    app.run()

