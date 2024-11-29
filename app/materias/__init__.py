from flask import Blueprint

materias = Blueprint('materias', __name__, template_folder='templates', static_folder='static')

from . import routes

