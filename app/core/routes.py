from flask import render_template
from . import core
from .views import *


@core.route('/')
def r_portal():
    resultados=portal()
    return render_template('core/portal.html', resultados= resultados)

