from flask import Flask, request, render_template, redirect
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'super secret key'

db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["Blog_Info"]
Blog_Info = db["Blog_Info"]


@app.route('/upload/', methods=['GET', "POST"])
def upload():
    result = ''
    isPost = False
    if request.args.get('id') is not None:
        id = request.args.get('id')
        find = Blog_Info.find_one({"_id": ObjectId(id)})
        pre_id = find['_id']
        pre_tittle = find['tittle']
        pre_content = find['content']
    if request.method == "POST":
        isPost = True
        id = request.form['id']
        tittle = request.form['tittle']
        content = request.form['content']
        Blog_Info.delete_one({'_id': ObjectId(id)})
        Blog_Info.insert_one({'_id': ObjectId(id),'tittle': tittle, 'content': content})
        result = "Update Done"

    return render_template("upload.html", **locals())


@app.route('/insert/', methods=['GET', "POST"])
def insert():
    result = ''
    isPost = False
    if request.method == "POST":
        isPost = True
        tittle = request.form['tittle']
        content = request.form['content']
        Blog_Info.insert_one({'tittle': tittle, 'content': content})
        result = "Insert Successfully"
    return render_template("insert.html", **locals())


@app.route('/home/', methods=['GET', 'POST'])
def home():
    if request.args.get('id') is not None:
        id = request.args.get('id')
        Blog_Info.delete_one({'_id': ObjectId(id)})
    else:
        f = "Don't have any id"
    list = []
    havePost = False
    isPost = False
    for data in Blog_Info.find():
        list.append(data)
        havePost = True
    if request.method == "POST":
        arry =[]
        isPost = True
        tittle = request.form['tittle']
        for x in Blog_Info.find({'tittle': tittle}):
            arry.append(x)
        l = len(arry)
    else:
        tittle = ""
    return render_template("home.html", **locals())


if __name__ == "__main__":
    app.run()
