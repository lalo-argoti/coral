from flask import render_template
from . import core

@core.route('/')
def home():
    return render_template('core/home.html')

