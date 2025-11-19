from flask import Blueprint, render_template, abort, redirect, url_for
from jinja2 import TemplateNotFound

web_bp = Blueprint('web', __name__, template_folder='../web_client/templates', static_folder='../web_client/static')

@web_bp.route('/')
def index():
    try:
        return redirect(url_for('web.login'))
    except TemplateNotFound:
        abort(404)

"""@web_bp.route('/')
def index():
    return render_template('index.html')"""

@web_bp.route('/login')
def login():
    return render_template('login.html')

@web_bp.route('/place')
def place():
    return render_template('place.html')

@web_bp.route('/reviews')
def reviews():
    return render_template('add_review.html')