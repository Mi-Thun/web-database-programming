from flask import Flask, request, render_template, session
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/reload/', methods=['GET', "POST"])
def reload():
    isPost = False
    if request.method == 'POST':
        isPost = True
        content = request.form['content']
        session['content'] = content

    return render_template("reload.html", **locals())


if __name__ == "__main__":
    app.run()
