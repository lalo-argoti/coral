from flask import Blueprint, jsonify

colegio = Blueprint('colegio', __name__, template_folder='templates', static_folder='static')

from . import routes

