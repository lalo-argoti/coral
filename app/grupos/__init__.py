from flask import Blueprint

grupos = Blueprint('grupos', __name__, template_folder='templates', static_folder='static')

from . import routes

