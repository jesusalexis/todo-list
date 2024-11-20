from flask import Blueprint,render_template, request, redirect, url_for, g

from todor.auth import login_required

from .models import Todo, User
from todor import db

bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('/list')
@login_required
def index():
    todos = Todo.query.all()
    return render_template('todo/index.html', todos = todos)


@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(g.user.id, title, desc)

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')

def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo

@bp.route('/update/<int:id>', methods=('GET','POST'))
@login_required
def update(id):

    todo = get_todo(id)
    
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.state = True if request.form.get('state') == 'on' else False

        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/update.html', todo = todo)


@bp.route('/delete/<int:id>')
@login_required
def delete(id):

    todo = get_todo(id)
    
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))
    
@bp.route('/home')
@login_required
def home():
    user = g.user

    total_todos = Todo.query.filter_by(created_by=user.id).count()
    # Contar las tareas del usuario actual
    success_todos = Todo.query.filter_by(created_by=user.id, state=True).count()
    pending_todos = Todo.query.filter_by(created_by=user.id, state=False).count()

    print(f"Total Tareas: {success_todos}")
    print(f"Tareas Pendientes: {pending_todos}")

    return render_template('todo/home.html', user=user, success_todos=success_todos, pending_todos=pending_todos,total_todos = total_todos)