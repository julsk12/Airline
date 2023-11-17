from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from common.Toke import *

routes_home = Blueprint("routes_home", __name__)



@routes_home.route('/indexpagar', methods=['GET'] )
def indexpagar():
    return render_template('/main/form_pago.html')