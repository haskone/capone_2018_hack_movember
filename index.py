from flask import (
    Flask,
    session,
    request,
    render_template,
    flash,
)
from flask_sqlalchemy import SQLAlchemy

from utils import (
    check_passwords,
    generate_hash,
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

db.create_all()

@app.route('/momovement')
def momovement():
    email = session.get('logged_in')
    logged = bool(email)
    if email:
        email = email.split('@')[0]

    return render_template('momovement.html', logged=logged, email=email)

@app.route('/dashboard')
def dashboard():
    email = session.get('logged_in')
    if not email:
        return render_template('login.html')

    return render_template(
        'dashboard.html',
        logged=True,
        email=email.split('@')[0],
    )

@app.route('/')
def home():
    email = session.get('logged_in')
    logged = bool(email)
    if email:
        email = email.split('@')[0]

    return render_template('index.html', logged=logged, email=email)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or password is None:
        flash('Please specify email and password')
        return render_template('login.html')

    user = User.query.filter_by(email=email).first()
    if user and check_passwords(password=password, password_hash=user.password):
        session['logged_in'] = email
    else:
        flash('The email address or password is incorrect')
        return render_template('login.html')

    return dashboard()

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or password is None:
        flash('Please specify email and password')
        return render_template('registration.html')

    if User.query.filter_by(email=email).first():
        flash('User with this email already exists')
        return render_template('registration.html')

    passed_hash = generate_hash(password)
    user = User(password=passed_hash, email=email)
    db.session.add(user)
    db.session.commit()

    return login()

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return home()
