from flask import Blueprint

user_group = Blueprint('user_group', __name__, template_folder='templates', static_folder='static')

from . import routes

