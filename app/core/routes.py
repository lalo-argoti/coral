from flask import render_template, session
from . import core
from .views import *


@core.route('/')
def r_portal():
    resultados=portal()
    return render_template('core/portal.html', resultados= resultados,  username=session.get('username'))

