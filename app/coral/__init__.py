from flask import Blueprint, jsonify

coral = Blueprint('coral', __name__, template_folder='templates', static_folder='static')

from . import routes

