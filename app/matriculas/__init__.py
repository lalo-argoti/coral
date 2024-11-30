from flask import Blueprint

matriculas = Blueprint('matriculas', __name__, template_folder='templates', static_folder='static')

from . import routes

