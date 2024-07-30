from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from typing import Any
import os

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db: SQLAlchemy = SQLAlchemy(app)

class Todo(db.Model):
    id: Any = db.Column(db.Integer, primary_key=True)
    task: Any = db.Column(db.String(1000), nullable=False)
    complete: Any = db.Column(db.Boolean) 
    user_id: Any = db.Column(db.Integer)

@app.route('/')
def index():
    todoList = Todo.query.all()
    return render_template('base.html', todo_list=todoList)

@app.route('/add', methods=["POST"])
def add() -> Any | str:
    title: str = request.form.get("title")
    
    if title == "":
        return redirect(url_for("index"))

    newTask: Todo = Todo(task=title, complete=False)
    
    try:
        db.session.add(newTask)
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return "Hubo aun problema agregando su tarea."

@app.route('/delete/<int:todo_id>')
def delete(todo_id: int) -> Any | str:
    task = Todo.query.filter_by(id=todo_id).first()
    
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return "Hubo aun problema borrando su tarea."

@app.route('/update/<int:todo_id>')
def update(todo_id: int) -> Any | str:
    task = Todo.query.filter_by(id=todo_id).first()

    task.complete = not task.complete

    try:
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return "Hubo aun problema borrando su tarea."


if __name__ == "__main__":
    db.create_all()
    
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host = '0.0.0.0', port = port)















    '''




'''