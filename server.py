from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)


@app.route('/')
def index():
    users = User.get_all()
    return render_template('create.html', users=users)


@app.route('/users')
def all_users():
    users = User.get_all()
    return render_template('create.html', users=users)


@app.route('/users/new/<int:id>')
def new_user(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template('read(all).html', user=user)


@app.route('/create', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    users_id = User.save(data)
    return redirect(f'/users/new/{users_id}')


if __name__ == '__main__':  
    app.run(debug=True)   