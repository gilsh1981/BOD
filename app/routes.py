from flask import Blueprint, render_template, redirect, url_for, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'bfirst' and password == '1234':
            return redirect(url_for('main.home'))
    return render_template('login.html')

@main.route('/home')
def home():
    return render_template('home.html')
