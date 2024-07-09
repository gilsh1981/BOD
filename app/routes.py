# routes.py
from flask import Blueprint, render_template, redirect, url_for, request
from app.events import events_bp  # Import the events blueprint

blueprint = Blueprint('routes', __name__)

@blueprint.route('/')
def index():
    return redirect(url_for('routes.login'))

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login validation here
        return redirect(url_for('routes.home'))
    return render_template('login.html')

@blueprint.route('/home')
def home():
    return render_template('home.html')

@blueprint.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@blueprint.route('/events')
def events():
    return render_template('events.html')

@blueprint.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    os.makedirs('uploads', exist_ok=True)
    file.save(os.path.join('uploads', file.filename))
    return 'File successfully uploaded'

# Register the events blueprint
blueprint.register_blueprint(events_bp, url_prefix='/api')
