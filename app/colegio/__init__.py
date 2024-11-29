from flask import Blueprint

colegio = Blueprint('colegio', __name__, template_folder='templates', static_folder='static')

from . import routes

