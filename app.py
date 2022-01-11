from flask import Flask, render_template, request, redirect
from datetime import datetime
import pymongo
from pymongo import MongoClient

app = Flask(__name__,template_folder='template',static_folder='static')

cluster = MongoClient("mongodb+srv://taaham:123@cluster0.imuxc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Todo"]
collection = db["Data"]

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        collection.insert_one(
                    {
                        "title":title,
                        "desc":desc
                    }
                )
        
    data_obj = collection.find({})
    return render_template('index.html', allTodo=data_obj, len=collection.count())

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = collection.find_one({"_id":sno})
        
        todo.title = title
        todo.desc = desc
        
        return redirect("/")
        
    todo = collection.find_one({"_id":sno})
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    collection.delete_one({"_id":sno})

    return redirect("/")

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)