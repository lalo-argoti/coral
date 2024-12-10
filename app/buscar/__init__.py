from flask import Blueprint

buscar = Blueprint('buscar', __name__, template_folder='templates', static_folder='static')

from . import routes

